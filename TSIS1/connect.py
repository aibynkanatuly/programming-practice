import psycopg2
from config import load_config


def run_sql_file(filename):
    config = load_config()

    try:
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        with open(filename, "r", encoding="utf-8") as file:
            sql = file.read()

        cur.execute(sql)
        conn.commit()

        cur.close()
        conn.close()

        print(filename, "executed")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


if __name__ == "__main__":
    run_sql_file("schema.sql")
    run_sql_file("procedures.sql")