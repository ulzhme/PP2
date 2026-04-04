CREATE OR REPLACE FUNCTION find_contacts(pattern TEXT)
RETURNS TABLE(id INT, first_name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.first_name::TEXT, phonebook.phone::TEXT
    FROM phonebook
    WHERE phonebook.first_name ILIKE '%' || pattern || '%'
       OR phonebook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, first_name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.first_name::TEXT, phonebook.phone::TEXT
    FROM phonebook
    ORDER BY phonebook.id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;
