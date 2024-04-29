import mysql.connector
conn = mysql.connector.connect(
    host="localhost",       
    user="root",      
    password="root_db",  
    database="Book"   
)
cur=conn.cursor()
cur.execute("UPDATE MCA_STUDENT SET MARK=33 WHERE id=156")
conn.commit()

