import mysql.connector
conn = mysql.connector.connect(
    host="localhost",       
    user="root",      
    password="root_db",  
    database="IPL"   
)
cur=conn.cursor()
# update command
cur.execute("UPDATE IPLDATA SET SR=15.43 WHERE id=1")
conn.commit()