import mysql.connector

# Establish a database connection
conn = mysql.connector.connect(
    host="localhost",       
    user="root",      
    password="root_db",  
    database="Book"   
)


cur = conn.cursor()
sql_code='INSERT INTO BTECH (id,name,mark,address) VALUES(%s,%s,%s)'
data=(156,"priti",65)
cur.execute(sql_code,data)
conn.commit()
