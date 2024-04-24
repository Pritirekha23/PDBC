import mysql.connector
conn = mysql.connector.connect(
    host="localhost",       
    user="root",      
    password="root_db",  
    database="Book"   
)
cur=conn.cursor()
cur.execute("DELETE FROM BTECH WHERE id=158")
conn.commit()