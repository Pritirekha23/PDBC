import mysql.connector

# Establish a database connection
db = mysql.connector.connect(
    host="localhost",         
    user="root",      
    password="root_db", 
    database="Book"  
)

cur = db.cursor()

cur.execute(' CREATE TABLE BTECH( id INT,  name VARCHAR(20),  mark INT, address VARCHAR(20))')

