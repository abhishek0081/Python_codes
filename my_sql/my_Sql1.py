import mysql.connector as msq

conn = msq.connect(host="localhost",username="root",password="Fuck@off728304",database = "new_database")
# query ="USE new_database"
# print(conn)
my_cursor = conn.cursor()
# query = "CREATE DATABASE new_database"
# query = "SHOW DATABASES"
# my_cursor.execute(query)
# query= "CREATE TABLE student(name VARCHAR(255),age INT)"
# my_cursor.execute(query)
# query = "SELECT * FROM new_database.(CREATE TABLE student(name VARCHAR(255),age INT))"
# query = "INSERT INTO student(name,age) VALUES (%s,%s)"

values = [("Abhishek",21),
          ("sonu",22),
          ("JAYANT",21),
          ("Robin",21),
          ("Sujal Kumar Choudhary",18)
    ]
# my_cursor.execute(query)

# my_cursor.executemany(query,values)
query = "SELECT * FROM student"

# for row in my_cursor:
#     print(row)
# my_cursor.execute(query)
# print(my_cursor.fetchall())

# for database_name in my_cursor:
#     print(database_name)

# print(my_cursor.fetchall())
get_dup = "SELECT name,age from student WHERE HAVING COUNT(name)>1"
query = "UPDATE student SET age=age-10 WHERE age>21"
my_cursor.execute(query)
s = "DELETE FROM student WHERE "
conn.commit()
conn.close()



