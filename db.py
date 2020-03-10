import psycopg2

con= psycopg2.connect(
    host= 'localhost',
    database='postgres',
    user='user',
    password='pass'
)
cur= con.cursor()

cur.exe

con.close()