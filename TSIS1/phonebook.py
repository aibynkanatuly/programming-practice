import psycopg2
import csv
import json
from config import load_config


def connect():
    config = load_config()
    return psycopg2.connect(**config)


def show_rows(rows):
    for row in rows:
        new_row = []

        for item in row:
            if hasattr(item, "strftime"):
                new_row.append(item.strftime("%Y-%m-%d"))
            else:
                new_row.append(item)

        print(tuple(new_row))


def add_contact():
    username = input("Username: ")
    email = input("Email: ")
    birthday = input("Birthday YYYY-MM-DD: ")
    group_name = input("Group: ")
    phone = input("Phone: ")
    phone_type = input("Type home/work/mobile: ")

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT(name) DO NOTHING", (group_name,))
        cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
        group_id = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO contacts(username, email, birthday, group_id) VALUES(%s, %s, %s, %s)",
            (username, email, birthday, group_id)
        )

        cur.execute("SELECT id FROM contacts WHERE username = %s", (username,))
        contact_id = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO phones(contact_id, phone, type) VALUES(%s, %s, %s)",
            (contact_id, phone, phone_type)
        )

        conn.commit()
        cur.close()
        conn.close()

        print("Contact added")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def list_contacts():
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.id, c.username, c.email, c.birthday, g.name, p.phone, p.type
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
            ORDER BY c.id
        """)

        rows = cur.fetchall()
        show_rows(rows)

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def search_all():
    query = input("Search: ")

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        rows = cur.fetchall()

        show_rows(rows)

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def search_by_email():
    email = input("Email pattern: ")

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.id, c.username, c.email, c.birthday, g.name
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            WHERE c.email ILIKE %s
            ORDER BY c.id
        """, ('%' + email + '%',))

        rows = cur.fetchall()
        show_rows(rows)

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def filter_by_group():
    group_name = input("Group: ")

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.id, c.username, c.email, c.birthday, g.name
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            WHERE g.name = %s
            ORDER BY c.id
        """, (group_name,))

        rows = cur.fetchall()
        show_rows(rows)

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def sort_contacts():
    print("1. Sort by username")
    print("2. Sort by birthday")
    print("3. Sort by created_at")

    choice = input("Choose: ")

    if choice == "1":
        order = "c.username"
    elif choice == "2":
        order = "c.birthday"
    elif choice == "3":
        order = "c.created_at"
    else:
        print("Invalid")
        return

    try:
        conn = connect()
        cur = conn.cursor()

        sql = f"""
            SELECT c.id, c.username, c.email, c.birthday, c.created_at, g.name
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            ORDER BY {order}
        """

        cur.execute(sql)
        rows = cur.fetchall()

        show_rows(rows)

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def pagination():
    limit = int(input("Limit: "))
    offset = 0

    while True:
        try:
            conn = connect()
            cur = conn.cursor()

            cur.execute("SELECT * FROM get_contacts_page(%s, %s)", (limit, offset))
            rows = cur.fetchall()

            print("\nPAGE")
            show_rows(rows)

            cur.close()
            conn.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error:", error)

        command = input("next/prev/quit: ")

        if command == "next":
            offset += limit
        elif command == "prev":
            offset -= limit
            if offset < 0:
                offset = 0
        elif command == "quit":
            break
        else:
            print("Invalid command")


def add_phone():
    username = input("Contact username: ")
    phone = input("New phone: ")
    phone_type = input("Type home/work/mobile: ")

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("CALL add_phone(%s, %s, %s)", (username, phone, phone_type))
        conn.commit()

        cur.close()
        conn.close()

        print("Phone added")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def move_to_group():
    username = input("Contact username: ")
    group_name = input("New group: ")

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("CALL move_to_group(%s, %s)", (username, group_name))
        conn.commit()

        cur.close()
        conn.close()

        print("Moved")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def delete_contact():
    username = input("Username: ")

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("DELETE FROM contacts WHERE username = %s", (username,))
        conn.commit()

        cur.close()
        conn.close()

        print("Deleted")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def import_csv():
    filename = input("CSV filename: ")

    try:
        conn = connect()
        cur = conn.cursor()

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                username = row["username"]
                email = row["email"]
                birthday = row["birthday"]
                group_name = row["group"]
                phone = row["phone"]
                phone_type = row["type"]

                cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT(name) DO NOTHING", (group_name,))
                cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
                group_id = cur.fetchone()[0]

                cur.execute("SELECT id FROM contacts WHERE username = %s", (username,))
                result = cur.fetchone()

                if result is None:
                    cur.execute(
                        "INSERT INTO contacts(username, email, birthday, group_id) VALUES(%s, %s, %s, %s)",
                        (username, email, birthday, group_id)
                    )
                    cur.execute("SELECT id FROM contacts WHERE username = %s", (username,))
                    contact_id = cur.fetchone()[0]
                else:
                    contact_id = result[0]

                cur.execute(
                    "INSERT INTO phones(contact_id, phone, type) VALUES(%s, %s, %s)",
                    (contact_id, phone, phone_type)
                )

        conn.commit()
        cur.close()
        conn.close()

        print("CSV imported")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def export_json():
    filename = input("JSON filename: ")

    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.id, c.username, c.email, c.birthday, g.name
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            ORDER BY c.id
        """)

        contacts = cur.fetchall()
        data = []

        for contact in contacts:
            contact_id = contact[0]

            cur.execute("SELECT phone, type FROM phones WHERE contact_id = %s", (contact_id,))
            phones = cur.fetchall()

            item = {
                "username": contact[1],
                "email": contact[2],
                "birthday": str(contact[3]),
                "group": contact[4],
                "phones": []
            }

            for phone in phones:
                item["phones"].append({
                    "phone": phone[0],
                    "type": phone[1]
                })

            data.append(item)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        cur.close()
        conn.close()

        print("Exported")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def import_json():
    filename = input("JSON filename: ")

    try:
        conn = connect()
        cur = conn.cursor()

        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            username = item["username"]
            email = item["email"]
            birthday = item["birthday"]
            group_name = item["group"]

            cur.execute("SELECT id FROM contacts WHERE username = %s", (username,))
            old = cur.fetchone()

            if old is not None:
                action = input(username + " exists. skip/overwrite: ")

                if action == "skip":
                    continue

                if action == "overwrite":
                    cur.execute("DELETE FROM contacts WHERE username = %s", (username,))

            cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT(name) DO NOTHING", (group_name,))
            cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
            group_id = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO contacts(username, email, birthday, group_id) VALUES(%s, %s, %s, %s)",
                (username, email, birthday, group_id)
            )

            cur.execute("SELECT id FROM contacts WHERE username = %s", (username,))
            contact_id = cur.fetchone()[0]

            for phone in item["phones"]:
                cur.execute(
                    "INSERT INTO phones(contact_id, phone, type) VALUES(%s, %s, %s)",
                    (contact_id, phone["phone"], phone["type"])
                )

        conn.commit()
        cur.close()
        conn.close()

        print("JSON imported")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


def main():
    while True:
        print("\n[1] Add contact")
        print("[2] List contacts")
        print("[3] Search all")
        print("[4] Search by email")
        print("[5] Filter by group")
        print("[6] Sort contacts")
        print("[7] Pagination")
        print("[8] Add phone")
        print("[9] Move to group")
        print("[10] Delete contact")
        print("[11] Import CSV")
        print("[12] Export JSON")
        print("[13] Import JSON")
        print("[0] Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_all()
        elif choice == "4":
            search_by_email()
        elif choice == "5":
            filter_by_group()
        elif choice == "6":
            sort_contacts()
        elif choice == "7":
            pagination()
        elif choice == "8":
            add_phone()
        elif choice == "9":
            move_to_group()
        elif choice == "10":
            delete_contact()
        elif choice == "11":
            import_csv()
        elif choice == "12":
            export_json()
        elif choice == "13":
            import_json()
        elif choice == "0":
            break
        else:
            print("Invalid")


if __name__ == "__main__":
    main()