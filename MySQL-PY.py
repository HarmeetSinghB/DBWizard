# IMPORT NECESSARY LIBRARIES:

import mysql.connector
from datetime import datetime
'''(In this code, we have established a connection with the MySQL database and imported 'datetime' from the standard library to handle date and time operations.)'''



# 1. ESTABLISH A DATA CONNECTION:

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="meet290800",
    database= "Lambton_College"
)

mycursor= mydb.cursor()
'''(This code CONNECTS to the MySQL server running on the local machine with the provided credentials such as host, user, password, and database name.)'''



# 2. CREATE A DATABASE:

database_name= 'Lambton_College'

mycursor.execute("CREATE DATABASE %s" % database_name)
'''(It CREATES a new database named "Lambton_College" using the 'CREATE DATABASE' statement.)'''


mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
'''(Here, we retrieve a list of all databases using the 'SHOW DATABASES' statement.)'''



# 3. CREATE A TABLE:

mycursor.execute("CREATE TABLE Student_Details (Student_ID int PRIMARY KEY NOT NULL AUTO_INCREMENT, Student_Name VARCHAR(50) not null, Created DATETIME, Student_Age smallint UNSIGNED, Gender ENUM('M', 'F', 'O'), Student_Address VARCHAR(100))")
'''(It CREATES a table named "Student_Details" with the specified columns and their data types in the "Lambton_College" database which has columns for
    Student_ID, an integer column (that serves as the primary key) and is set to auto-increment,
    Student_Name, a string column upto 50 characters and cannot be null,
    Created, a datetime column (that stores the date and time the record was created),
    Student_Age, a small integer column,
    Gender, an enumeration column and can have three possible values: 'M' (Male), 'F' (Female), or 'O' (Other),
    Student_Address, a string column upto 100 characters.)'''


mycursor.execute("DESCRIBE Student_Details")
for x in mycursor:
    print(x)
'''(After creating the table, it retrieves the table structure using the 'DESCRIBE' statement)'''



# 4. INSERT DATA NTO THE TABLE:

query1="INSERT INTO Student_Details (Student_Name, Created, Student_Age, Gender, Student_Address) VALUES (%s, %s, %s, %s,%s)"

values1=[
    ("Harmeet Singh", datetime.now(), 22, "M", "Mississauga, ON"),
    ("Mihir Chaudhary", datetime.now(), 21, "M", "Mississauga, ON"),
    ("Tanvi Patel", datetime.now(), 23, "F", "Mississauga, ON"),
    ("Vineet Pinjrotia", datetime.now(), 23, "M", "Brampton, ON")
]
'''(It is a list containing tuples representing the values to be inserted into the table.)'''

mycursor.executemany(query1,values1)
'''(It INSERTS multiple rows of student details with the 'executemany' method into the "Student_Details" table using the 'INSERT INTO' statement and a list of values.)'''

mydb.commit()
'''(It COMMITS the changes made to the database)'''



# 5. EXECUTE SELECT QUERIES:

mycursor.execute("SELECT * FROM Student_Details")
'''(It retrieves ALL data from the "Student_Details" table.)'''


mycursor.execute("SELECT * FROM Student_Details WHERE Gender = 'M' ORDER BY Student_ID DESC")
'''(It includes retrieving all rows and filtering by gender and ordering by "Student_ID".)'''


mycursor.execute("SELECT Student_Name FROM Student_Details WHERE Gender = 'M' ORDER BY Student_ID DESC")
'''(It includes retrieving "Student_Name" column and filtering by gender and ordering by "Student_ID".)'''



# 6. MODIFY THE TABLE:

mycursor.execute("ALTER TABLE Student_Details ADD COLUMN Student_Qualification VARCHAR(100)")
'''(It ADDS a new column named "Student_Qualification" of datatype VARCHAR(100).)'''


mycursor.execute("ALTER TABLE Student_Details DROP Student_Qualification")
'''(It DROPS the "Student_Qualification" column.)'''


mycursor.execute("ALTER TABLE Student_Details CHANGE Student_Age Age smallint")
'''(It changes the data type of the "Student_Age" column to "Age" (smallint).)'''


mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
'''(It retrieves a list of all tables in the database using the 'SHOW TABLES' statement.)'''



# 7. DELETE DATA FROM THE TABLE:

mycursor.execute("DELETE FROM Student_Details")
'''(It DELETES ALL rows from the "Student_Details" table using the 'DELETE FROM' statement.)'''



# 8. CREATE ANOTHER TABLE WITH A FOREIGN KEY:

mycursor.execute("CREATE TABLE Total_Assessment (Exam_ID INT PRIMARY KEY, FOREIGN KEY(Exam_ID) REFERENCES Student_Details(Student_ID), Subject_1 int DEFAULT 0, Subject_2 int DEFAULT 0)")
'''(It CREATES a NEW TABLE named "Total_Assessment" with columns for 
    Exam_ID, an integer column (that serves as the primary key) and specifies that the Exam_ID column references the Student_ID column in the "Student_Details" table,
    Subject_1 and Subject_2, an integer column (with default values of 0).)'''


query2="INSERT INTO Total_Assessment (Exam_ID, Subject_1, Subject_2) VALUES (%s, %s, %s)"

value2=[
    (75,89),
    (85,90),
    (92,79),
    (80,92)
]

for x, y in enumerate(values1):
    mycursor.execute(query1,y)
    last_id=mycursor.lastrowid      # (It retrieves the last inserted row ID (last_id) using mycursor.lastrowid.)
    mycursor.execute(query2, (last_id,) + value2[x])
'''(We have used a 'for' loop to iterate over the values in 'values1' and for each iteration, the 'query1' with the current values is executed from 'values1'.)'''


mycursor.execute("SELECT * FROM Student_Details")

mycursor.execute("SELECT * FROM Total_Assessment")

for x in mycursor:
    print(x)
'''(It retrieves data from both the "Student_Details" and "Total_Assessment" tables.)'''