import psycopg2
from config import load_config
from connect import connect

def getAllStudents():
    config = load_config()
    connection = connect(config)

    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select student_id, first_name, last_name, email, enrollment_date from Students")
            rows = cur.fetchall()

            print("\nListing all Students")
            print("-----------------------------------------")
            for row in rows:
                print(row)
    print("")
    connection.close()

def addStudent(first_name: str, last_name: str, email: str, enrollment_date: str):
    config = load_config()
    connection = connect(config)
    print("\nAdding a student")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into Students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date))
            connection.commit()
            connection.close()
    
    print("New student successfully added with data:", first_name, last_name, email, enrollment_date)
    print("")

def updateStudentEmail(student_id: int, new_email: str):
    config = load_config()
    connection = connect(config)
    print("\nUpdating student data:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("update Students set email=%s where student_id=%s;", (new_email, student_id))
            connection.commit()

            print("Student email successdaully updated\n")

            connection.close()
    

if __name__ == '__main__':
    getAllStudents()
    #addStudent('Student D', 'Student D', 'D@email.com', '2002-02-22')
    updateStudentEmail(3,'jim.beam@example.com')
    getAllStudents()
