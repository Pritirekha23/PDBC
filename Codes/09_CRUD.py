import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root_db',
    database='Book'
    )

cur=conn.cursor()

#table creation
def create_table():
    sql_code='CREATE TABLE STUDENTS(id INT,name VARCHAR(20),mark INT)'
    cur.execute(sql_code)
    print('table created successsfully')

#Record insertions
def insert_record(id,name,mark):
    sql_code='INSERT INTO STUDENTS(id,name,mark) VALUES (%s,%s,%s)'
    data=(id,name,mark)
    cur.execute(sql_code,data)
    conn.commit()
    print('One Record inserted successfully')

# Retrive all the records
def display_data():
    sql_code='SELECT * FROM STUDENTS'
    cur.execute(sql_code)
    records=cur.fetchall()
    for i in records:
        print(i)


#fetchall will give all records in the form of tuple.

#update records
def update_record(id,newname,newmark):
    sql_code='UPDATE STUDENTS SET name=%s, mark=%s WHERE id=%s'
    data=(newname,newmark,id)
    cur.execute(sql_code,data)
    conn.commit()
    print('RECORD updated successfully')


#delete records
def delete_record(id):
    sql_code='DELETE FROM STUDENTS WHERE id=%s'
    data=(id,)
    cur.execute(sql_code,data)
    conn.commit()
    print('Record deleted succcessfully.........')


while True:
    print('*************CRUD OPERATION*****************')
    print('Please select any option ')
    print('press 1 for : CREATIONS')
    print('press 2 for : INSERTIONS ')
    print('press 3 for : RETRIVE ')
    print('press 4 for : UPDATION ')
    print('press 5 for : DELETIONS ')
    print('press 6 for : EXIT ')
    choice=int(input('Enter your choice:'))
    if choice==1:
        create_table()
    elif choice==2:
        id=int(input('enter the id:'))
        name=input('Enter name:')
        mark=int(input('enter mark:'))
        insert_record(id,name,mark)
    elif choice==3:
        display_data()
    elif choice==4:
        id=int(input('enter the id:'))
        newname=input('Enter name:')
        newmark=int(input('enter mark:'))
        update_record(id,newname,newmark)
    elif choice==5:
        id=int(input('enter the id:'))
        delete_record(id,)
    elif choice==6:
        print("Thanks for using our applications")
        break
    else:
        print("Invalid option please select valid options")
