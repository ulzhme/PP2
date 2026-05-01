import psycopg2
import csv
import json
import os
from datetime import datetime
from config import load_config

class PhoneBookApp:
    def __init__(self):
        self.config = load_config()

    def get_connection(self):
        return psycopg2.connect(**self.config)

    def add_contact(self, first_name, last_name, email=None, birthday=None, group_name=None):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                group_id = None
                if group_name:
                    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
                    row = cur.fetchone()
                    if row:
                        group_id = row[0]
                    else:
                        cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,))
                        group_id = cur.fetchone()[0]

                cur.execute(
                    "INSERT INTO contacts (first_name, last_name, email, birthday, group_id) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                    (first_name, last_name, email, birthday, group_id)
                )
                return cur.fetchone()[0]

    def add_phone(self, first_name, last_name, phone, phone_type):
        # Strip whitespace and convert to lowercase
        phone_type = phone_type.strip().lower() 
        
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_phone(%s, %s, %s, %s)", (first_name, last_name, phone, phone_type))
            conn.commit()

    def move_to_group(self, first_name, last_name, group_name):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL move_to_group(%s, %s, %s)", (first_name, last_name, group_name))
            conn.commit()

    def search(self, query):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_contacts(%s)", (query,))
                return cur.fetchall()

    def get_contacts(self, group_name=None, sort_by='name', limit=10, offset=0):
        sort_map = {
            'name': 'c.first_name, c.last_name',
            'birthday': 'c.birthday',
            'date': 'c.created_at'
        }
        order_by = sort_map.get(sort_by, 'c.first_name, c.last_name')
        
        sql = f"""
            SELECT 
                c.id, c.first_name, c.last_name, c.email, c.birthday, g.name, 
                string_agg(p.phone || ' (' || p.type || ')', ', ')
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
        """
        params = []
        if group_name:
            sql += " WHERE g.name = %s"
            params.append(group_name)
        
        sql += f" GROUP BY c.id, g.name ORDER BY {order_by} LIMIT %s OFFSET %s"
        params.extend([limit, offset])

        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(params))
                return cur.fetchall()

    def export_to_json(self, filename):
        # Resolve path
        if not os.path.isabs(filename):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(script_dir, filename)

        contacts = self.get_contacts(limit=10000) # Get all
        data = []
        for c in contacts:
            data.append({
                'id': c[0],
                'first_name': c[1],
                'last_name': c[2],
                'email': c[3],
                'birthday': str(c[4]) if c[4] else None,
                'group': c[5],
                'phones': c[6]
            })
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Exported to {filename}")

    def import_from_json(self, filename):
        # Resolve path
        if not os.path.isabs(filename) and not os.path.exists(filename):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(script_dir, filename)

        if not os.path.exists(filename):
            print(f"Error: File {filename} not found.")
            return

        with open(filename, 'r') as f:
            data = json.load(f)
        
        for item in data:
            first_name = item.get('first_name')
            last_name = item.get('last_name')
            email = item.get('email') or None
            birthday = item.get('birthday') or None
            group = item.get('group') or None
            
            # Check for duplicate
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT id FROM contacts WHERE first_name = %s AND last_name = %s", 
                                (first_name, last_name))
                    row = cur.fetchone()
                    if row:
                        ans = input(f"Contact {first_name} {last_name} exists. Overwrite? (y/n): ")
                        if ans.lower() != 'y':
                            continue
                        # Delete existing to overwrite
                        cur.execute("DELETE FROM contacts WHERE id = %s", (row[0],))
            
            # Insert new
            self.add_contact(first_name, last_name, email, birthday, group)
            # Import phones if any
            if item.get('phones'):
                phone_list = item['phones'].split(', ')
                for p_str in phone_list:
                    if ' (' in p_str:
                        phone, p_type = p_str.replace(')', '').split(' (')
                        self.add_phone(first_name, last_name, phone, p_type)
        print(f"Imported from {filename}")

    def import_from_csv(self, filename):
        # Resolve path
        if not os.path.isabs(filename) and not os.path.exists(filename):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(script_dir, filename)

        if not os.path.exists(filename):
            print(f"Error: File {filename} not found.")
            return

        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                first_name = row.get('first_name')
                last_name = row.get('last_name')
                email = row.get('email') or None
                birthday = row.get('birthday') or None
                group = row.get('group') or None
                phone = row.get('phone')
                phone_type = row.get('phone_type') or 'mobile'

                # Check for duplicate
                with self.get_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT id FROM contacts WHERE first_name = %s AND last_name = %s", 
                                    (first_name, last_name))
                        if cur.fetchone():
                            print(f"Skipping existing contact: {first_name} {last_name}")
                            continue

                # Insert
                self.add_contact(first_name, last_name, email, birthday, group)
                if phone:
                    self.add_phone(first_name, last_name, phone, phone_type)
        print(f"Imported from {filename}")

def main():
    app = PhoneBookApp()
    
    while True:
        print("\n--- PhoneBook Extended ---")
        print("1. Add Contact")
        print("2. Add Phone to Contact")
        print("3. Search (Name/Email/Phone)")
        print("4. View All (Paginated/Sort/Filter)")
        print("5. Move to Group")
        print("6. Export to JSON")
        print("7. Import from JSON")
        print("8. Import from CSV")
        print("0. Exit")
        
        choice = input("Choice: ")
        
        if choice == '0':
            break
        elif choice == '1':
            fn = input("First Name: ")
            ln = input("Last Name: ")
            em = input("Email: ")
            bd = input("Birthday (YYYY-MM-DD): ")
            gr = input("Group: ")
            app.add_contact(fn, ln, em, bd if bd else None, gr if gr else None)
        elif choice == '2':
            fn = input("First Name: ")
            ln = input("Last Name: ")
            ph = input("Phone: ")
            pt = input("Type (home/work/mobile): ")
            try:
                app.add_phone(fn, ln, ph, pt)
            except Exception as e:
                print(e)
        elif choice == '3':
            q = input("Search query: ")
            results = app.search(q)
            for r in results:
                print(r)
        elif choice == '4':
            group = input("Filter by group (Enter for none): ")
            sort = input("Sort by (name/birthday/date): ") or 'name'
            
            page = 0
            page_size = 5
            while True:
                contacts = app.get_contacts(group if group else None, sort, page_size, page * page_size)
                print(f"\n--- Page {page + 1} ---")
                for c in contacts:
                    print(f"{c[1]} {c[2]} | {c[3]} | {c[4]} | Group: {c[5]} | Phones: {c[6]}")
                
                nav = input("\n[n] Next, [p] Prev, [q] Quit pagination: ")
                if nav == 'n':
                    page += 1
                elif nav == 'p' and page > 0:
                    page -= 1
                elif nav == 'q':
                    break
        elif choice == '5':
            fn = input("First Name: ")
            ln = input("Last Name: ")
            gr = input("New Group Name: ")
            try:
                app.move_to_group(fn, ln, gr)
            except Exception as e:
                print(e)
        elif choice == '6':
            app.export_to_json('contacts.json')
        elif choice == '7':
            app.import_from_json('contacts.json')
        elif choice == '8':
            app.import_from_csv('contacts.csv')

if __name__ == '__main__':
    main()
