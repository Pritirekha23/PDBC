import mysql.connector

# Establish a database connection
db = mysql.connector.connect(
    host="localhost",       
    user="root",      
    password="root_db",  
    database="Book"   
)


cur = db.cursor()

cur.execute(' UPDATE  BTECH SET name="jasmin" WHERE id=101')
db.commit()

