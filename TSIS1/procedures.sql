CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE username = p_contact_name;

    IF v_contact_id IS NULL THEN
        RAISE NOTICE 'Contact not found';
    ELSE
        INSERT INTO phones(contact_id, phone, type)
        VALUES(v_contact_id, p_phone, p_type);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_group_id INTEGER;
BEGIN
    INSERT INTO groups(name)
    VALUES(p_group_name)
    ON CONFLICT(name) DO NOTHING;

    SELECT id INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE username = p_contact_name;
END;
$$;

CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(
    id INTEGER,
    username VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phone VARCHAR,
    type VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.username, c.email, c.birthday, g.name, p.phone, p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.username ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%'
       OR g.name ILIKE '%' || p_query || '%'
    ORDER BY c.id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts_page(p_limit INTEGER, p_offset INTEGER)
RETURNS TABLE(
    id INTEGER,
    username VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.username, c.email, c.birthday, g.name
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;