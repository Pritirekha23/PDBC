
# database name:IPL

# table name:IPLDATA

### Table creation 

```
import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root_db',
    database='IPL'
)
cur=conn.cursor()
cur.execute(' CREATE TABLE IPLDATA(ID INT PRIMARY KEY,  TEAM VARCHAR(50), NAME VARCHAR(50), MATCHES INT, INNINGS INT, OVERS DECIMAL(4,1),  RUNS INT,WICKETS INT,BBI INT,AVG DECIMAL(4,2),ECONOMY DECIMAL(4,2),SR DECIMAL(4,2),`4w` INT,`5w` INT)');




```

data insertions:
```
import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root_db',
    database='IPL'
)

cur=conn.cursor()
sql_code="INSERT INTO IPLDATA(ID,TEAM,NAME,MATCHES,INNINGS,OVERS,RUNS,WICKETS,BBI,AVG,ECONOMY,SR,4w,5w) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s)"
data=[
    (1,  "MI",  "Jasprit Bumrah",9, 9, 36, 239, 14, 21/5, 17.07, 6.63, 15.42, 0,1),
    (2,  "MI",  "Gerald Coetzee", 8, 8, 28.3, 288, 12,4/34 , 24.00, 10.10, 14.25, 1, 0),
    (3,  "MI",  "Akash Madhwal", 5, 5, 18.1, 205, 5, 3/20, 41.00, 11.28, 21.80, 0, 0),
    (4,  "MI",  "Piyush Chawla", 6, 6, 18.0, 184, 4, 1/31, 46.00, 10.22, 27.00, 0, 0),
    (5,  "MI",  "Hardik Pandya", 9, 7, 19.0, 227, 4, 2/43, 56.75, 11.94, 28.50, 0, 0),
    (6,  "CSK",  "Mustafizur Rahman", 8, 8, 30.2, 296, 14, 29/4, 21.14, 9.75, 13.00, 1, 0),
    (7,  "CSK",  "Matheesha Pathirana", 6, 6, 22.0, 169, 13, 28/4, 13.00, 7.68, 10.15, 1, 0),
    (8,  "CSK",  "Tushar Deshpande", 9, 9, 32.0, 277, 10, 27/4, 27.70, 8.65, 19.20, 1, 0),
    (9,  "CSK",  "Ravindra Jadeja", 9, 9, 31.0, 234, 5, 18/3, 46.80, 7.54, 37.20, 0, 0),
    (10, "CSK", "Deepak Chahar", 7, 7, 23.1, 198, 5, 28/2, 39.60, 8.54, 27.80, 0, 0),
    (11,  "PBKS",  "Harshal Patel", 9, 9, 32.0, 326, 14, 15/3, 23.28, 10.18, 13.71, 0, 0),
    (12,  "PBKS",  "Arshdeep Singh", 9, 9, 31.2, 302, 12, 29/4, 25.16, 9.63, 15.66, 1, 0),
    (13,  "PBKS",  "Sam Curran", 9, 9, 28.0, 271, 12, 28/3, 22.58, 9.67, 14.00, 0, 0),
    (14,  "PBKS",  "Kagiso Rabada", 9, 9, 35.0, 325, 10, 18/2, 32.50, 9.28, 21.00, 0, 0),
    (15,  "PBKS",  "Harpreet Brar", 9, 9, 29.0, 221, 4, 13/2, 55.25, 7.62, 43.50, 0, 0),
    (16,  "RR",   "Yuzvendra Chahal", 9, 9, 34.0, 306, 13, 11/3, 23.53, 9.00, 15.69, 0, 0),
    (17,  "RR",  "Trent Boult", 9, 9, 32.0, 250, 10, 22/3, 25.00, 7.81, 19.20, 0, 0),
    (18,  "RR",  "Avesh Khan", 9, 9, 35.0, 334, 9, 34/2, 37.11, 9.54, 23.33, 0, 0),
    (19,  "RR",  "Sandeep Sharma", 4, 4, 15.0, 107, 8, 18/5, 13.37, 7.13, 11.25, 0, 1),
    (20,  "RR",  "Nandre Burger", 4, 4, 14.0, 124, 6, 29/2, 20.66, 8.85, 14.00, 0, 0),
    (21,  "SRH",  "T Natarajan", 7, 7, 28.0, 252, 13, 4/19, 19.38, 9.00, 12.92,  0, 0),
    (22,  "SRH",  "Pat Cummins", 9, 9, 36.0, 328, 10, 3/43, 32.80, 9.11, 21.60,  0, 0),
    (23,  "SRH",  "Jaydev Unadkat", 7, 7, 25.1, 263, 8, 3/30, 32.87, 10.45, 18.87, 0, 0),
    (24,  "SRH",  "Mayank Markande", 7, 7, 22.0, 259, 8, 2/26, 32.37, 11.77, 16.50,  0, 0),
    (25,  "SRH",  "Bhuvneshwar Kumar", 9, 9, 33.0, 336, 5, 2/32, 67.20, 10.18, 39.60, 0, 0),
    (26,  "DC",  "Mukesh Kumar", 7, 7, 25.3, 282, 13, 14/3, 21.69, 11.05, 11.76, 0, 0),
    (27,  "DC",   "Kuldeep Yadav", 7, 7, 27.0, 230, 12, 55/4, 19.16, 8.51, 13.50, 1, 0),
    (28,  "DC",  "Khaleel Ahmed", 10, 10, 37.0, 351, 12, 21/2, 29.25, 9.48, 18.50, 0, 0),
    (29,  "DC",  "Axar Patel", 10, 10, 33.0, 243, 7, 35/2, 34.71, 7.36, 28.28, 0, 0),
    (30,  "DC",  "Anrich Nortje", 6, 6, 22.0, 294, 7, 59/3, 42.00, 13.36, 18.85, 0, 0),
    (31,  "KKR",  "Sunil Narine", 8, 8, 32.0, 223, 10, 30/2, 22.30, 6.96, 19.20, 0, 0),
    (32,  "KKR",  "Harshit Rana", 7, 6, 24.0, 246, 9, 33/3, 27.33, 10.25, 16.00, 0, 0),
    (33,  "KKR",  "Andre Russell", 8, 8, 15.2, 170, 9, 25/3, 18.88, 11.08, 10.22, 0, 0),
    (34,  "KKR",  "Varun Chakaravarthy", 8, 8, 29.0, 282, 8, 33/3, 35.25, 9.72, 21.75, 0, 0),
    (35,  "KKR",  "Vaibhav Arora", 4, 4, 14.0, 134, 7, 27/3, 19.14, 9.57, 12.00, 0, 0),
    (36,  "LSG",  "Yash Thakur", 8, 8, 28.5, 309, 10, 30/5, 30.90, 10.71, 17.30, 1, 0),
    (37,  "LSG",  "Mohsin Khan", 6, 6, 24.0, 247, 7, 29/2, 27.42, 10.29, 20.57, 0, 0),
    (38,  "LSG",  "Mayank Yadav", 3, 3, 9.0, 54, 6, 14/3, 9.00, 6.00, 9.00, 0, 0),
    (39,  "LSG",  "Naveen-Ul-Haq", 5, 5, 18.4, 170, 6, 25/2, 28.33, 9.10, 18.66, 0, 0),
    (40,  "LSG",  "Krunal Pandya", 9, 9, 25.0, 180, 5, 11/3, 36.00, 7.20, 30.00, 0, 0),
    (41,  "GT",   "Mohit Sharma", 10, 9, 33.0, 362, 10, 25/3, 36.20, 10.96, 19.80, 0, 0),
    (42,  "GT",   "Rashid Khan", 10, 10, 38.0, 304, 8, 49/2, 38.00, 8.00, 28.50, 0, 0),
    (43,  "GT",   "Sai Kishore", 5, 5, 15.0, 137, 7, 33/4, 19.57, 9.13, 12.85, 1, 0),
    (44,  "GT",   "Umesh Yadav", 6, 6, 18.0, 190, 7, 22/2, 27.14, 10.55, 15.42, 0, 0),
    (45,  "GT",   "Noor Ahmad", 8, 8, 28.5, 242, 6, 20/2, 40.33, 8.39, 28.83, 0, 0),
    (46,  "RCB",  "Yash Dayal", 9, 9, 34.0, 317, 8, 56/2, 39.62, 9.32, 25.50, 0, 0),
    (47,  "RCB",  "Mohammed Siraj", 9, 9, 34.0, 323, 6, 26/2, 53.83, 9.50, 34.00, 0, 0),
    (48,  "RCB",  "Cameron Green", 8, 8, 20.1, 194, 6, 12/2, 32.33, 9.61, 20.16, 0, 0),
    (49,  "RCB",  "Glenn Maxwell", 7, 5, 12.0, 104, 5, 23/2, 20.80, 8.66, 14.40, 0, 0),
    (50,  "RCB",  "Reece Topley", 4, 4, 15.0, 168, 4, 27/2, 42.00, 11.20, 22.50, 0, 0)
    
    ]

cur.executemany(sql_code,data)
conn.commit()

```
