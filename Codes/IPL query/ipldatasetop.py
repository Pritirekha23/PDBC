import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root_db',
    database='IPL'
)
cur=conn.cursor()
cur.execute(' CREATE TABLE IPLDATA(ID INT PRIMARY KEY,  TEAM VARCHAR(50), NAME VARCHAR(50), MATCHES INT, INNINGS INT, OVERS DECIMAL(4,1),  RUNS INT,WICKETS INT,BBI INT,AVG DECIMAL(4,2),ECONOMY DECIMAL(4,2),SR DECIMAL(4,2),`4w` INT,`5w` INT)');



