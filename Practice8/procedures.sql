
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;



CREATE OR REPLACE PROCEDURE bulk_insert()
LANGUAGE plpgsql
AS $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN SELECT * FROM temp_contacts LOOP
        
        IF rec.phone ~ '^[0-9]{11}$' THEN
            CALL upsert_contact(rec.name, rec.phone);
        ELSE
            RAISE NOTICE 'Invalid: % %', rec.name, rec.phone;
        END IF;

    END LOOP;
END;
$$;



CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;