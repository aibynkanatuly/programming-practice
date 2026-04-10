from connect import conn, cur

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Added!\n")


def show_contacts():
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    print()


def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("New phone: ")

    cur.execute(
        "UPDATE contacts SET phone=%s WHERE name=%s",
        (new_phone, name)
    )
    conn.commit()
    print("Updated!\n")


def delete_contact():
    name = input("Enter name to delete: ")

    cur.execute(
        "DELETE FROM contacts WHERE name=%s",
        (name,)
    )
    conn.commit()
    print("Deleted!\n")


def search_by_prefix():
    prefix = input("Phone starts with: ")

    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s",
        (prefix + "%",)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)
    print()


def menu():
    while True:
        print("1. Add contact")
        print("2. Show contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Search by phone prefix")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            search_by_prefix()
        elif choice == "6":
            break
        else:
            print("Invalid choice\n")


menu()

