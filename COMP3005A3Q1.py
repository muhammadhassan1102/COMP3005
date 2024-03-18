#Name: Muhammad Hassan
#Carleton Student ID: 101181439
#Course: COMP3005

import psycopg2

hostname = 'localhost'
databasename = 'COMP3005A3Q1'
username = 'postgres'
password = '1102'
port_id = 5432

try:
        conn = psycopg2.connect(
                host = hostname,
                dbname = databasename,
                user = username,
                password = password,
                port = port_id)
        cur = conn.cursor()
        print("Successfully connected to Postgres Database")
except Exception as error:
        print("Database connection was unsuccessful")


def getAllStudents():
        try:
                query = '''SELECT * FROM students'''
                cur.execute(query)
                conn.commit()
                
                students = cur.fetchall()
                for s in students:
                        print(s)
                print("\n")
        except Exception as error:
                print(error)

def addStudent(first_name, last_name, email, enrollment_date):
        try:
                query = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES \
                        ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');"
                cur.execute(query)
                conn.commit()
                
                print("Student added successfully")
        except Exception as error:
                print("Student not added successfully")
                
def updateStudentEmail(student_id, new_email):
        try:
                query = f"UPDATE students SET email = '{new_email}' \
                        WHERE student_id = '{student_id}';"
                cur.execute(query)
                conn.commit()
                
                print("Student Email updated successfully")
        except Exception as error:
                print("Student Email did not update successfully")

def deleteStudent(student_id):
        try:
                query = f"DELETE FROM students \
                        WHERE student_id = '{student_id}';"
                cur.execute(query)
                conn.commit()
                
                print("Student deleted successfully")
        except Exception as error:
                print("Student did not delete successfully")
                
     
        
#Step 1

#getAllStudents()

#Step 2

#addStudent("Muhammad", "Hassan", "muhammadhassan3@gmail.com", "2020-09-01")
#getAllStudents()

#Step 3

#updateStudentEmail("4", "newemail@gmail.com")
#getAllStudents()

#Step 4

#deleteStudent("4")
#getAllStudents()
                
cur.close()
conn.close()

