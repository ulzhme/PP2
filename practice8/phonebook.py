import psycopg2
from connect import get_connection

def search_by_pattern():
    pattern = input("Введите часть имени или телефона для поиска: ")
    conn = get_connection()
    cur = conn.cursor()
    # Вызываем функцию find_contacts
    cur.execute("SELECT * FROM find_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    
    print("\n--- Результаты поиска ---")
    if not rows:
        print("Ничего не найдено.")
    for row in rows:
        print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
    
    cur.close()
    conn.close()

def get_paginated():
    limit = int(input("Сколько записей показать (LIMIT)? "))
    offset = int(input("Сколько записей пропустить (OFFSET)? "))
    conn = get_connection()
    cur = conn.cursor()
    # Вызываем функцию get_contacts
    cur.execute("SELECT * FROM get_contacts(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    
    print("\n--- Страница контактов ---")
    if not rows:
        print("Пусто.")
    for row in rows:
        print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
        
    cur.close()
    conn.close()

def upsert_user():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    conn = get_connection()
    cur = conn.cursor()
    # Вызываем процедуру upsert_contact
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print(f"✅ Контакт {name} успешно добавлен или обновлен.")
    cur.close()
    conn.close()

def bulk_insert():
    # Тестовые данные для проверки (Алиса правильная, Боб с ошибкой в номере)
    names = ["Алиса", "Боб", "Чарли", "Дейв"]
    phones = ["11111", "abc", "33333", "number44"]
    
    conn = get_connection()
    cur = conn.cursor()
    
    # Очищаем старые уведомления
    del conn.notices[:]
    
    # Вызываем процедуру insert_many_contacts
    cur.execute("CALL insert_many_contacts(%s, %s)", (names, phones))
    conn.commit()
    print("\n✅ Запрос на массовую вставку выполнен.")
    
    # Ловим RAISE NOTICE из твоей процедуры
    if conn.notices:
        print("⚠️ Сообщения от базы данных:")
        for notice in conn.notices:
            print("  ->", notice.strip())
            
    cur.close()
    conn.close()

def delete_user():
    val = input("Введите имя или телефон для удаления: ")
    conn = get_connection()
    cur = conn.cursor()
    
    del conn.notices[:]
    
    # Вызываем процедуру delete_contact
    cur.execute("CALL delete_contact(%s)", (val,))
    conn.commit()
    
    if conn.notices:
        for notice in conn.notices:
            print("✅", notice.strip())
            
    cur.close()
    conn.close()

def main():
    while True:
        print("\n=== PhoneBook v2 (Procedures & Functions) ===")
        print("1. Поиск по паттерну")
        print("2. Добавить/Обновить контакт (Upsert)")
        print("3. Массовая вставка (List test)")
        print("4. Показать контакты (Пагинация)")
        print("5. Удалить контакт")
        print("0. Выход")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            search_by_pattern()
        elif choice == "2":
            upsert_user()
        elif choice == "3":
            bulk_insert()
        elif choice == "4":
            get_paginated()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            print("До встречи!")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()