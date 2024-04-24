import mysql.connector

# Establish a database connection
db = mysql.connector.connect(
    host="localhost",         # Your database host (e.g., 'localhost', '127.0.0.1', or remote address)
    user="root",      # Your MySQL username
    password="root_db",  # Your MySQL password
    database="Book"   # The database you want to connect to
)

# Create a cursor object
cur = db.cursor()


cur.execute('SHOW DATABASES')
for i in cur:
    print(i)