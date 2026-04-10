import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="ajbyn",
    password=""
)

cur = conn.cursor()
