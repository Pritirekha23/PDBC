import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root_db",
    database="Book"
)

cur = conn.cursor()

sql_code = 'INSERT INTO BTECH (id, name, mark, address) VALUES (%s, %s, %s, %s)'
data = [(157, "KIRTII", 98, "kdp"), (158, "SRTII", 48, "bdk"), (159, "Aman", 78, "Blr"), (160, "Suman", 48, "bbsr")]

cur.executemany(sql_code, data)
conn.commit()