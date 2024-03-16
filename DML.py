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

            for row in rows:
                print(row)

def addStudent(first_name, last_name, email, enrollment_date):
    pass
    

if __name__ == '__main__':
    getAllStudents()