from config import load_config
from connect import connect

def getAllStudents(): #Function to print all students
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select student_id, first_name, last_name, email, enrollment_date from Students") #Execute SQL statement
            rows = cur.fetchall() #Get all rows/entries of data

            print("\nListing all Students")
            print("-----------------------------------------")
            for row in rows:
                print(row)
                #print(row[0]) Can get IDs like this and put them in an array to check before deletion? But then will we iterate through the array each time? Or make it a global variable?
                # Dont need to for this assignment, beyond scope I think
    print("")
    connection.close()

def addStudent(first_name, last_name, email, enrollment_date): #Add student to database
    config = load_config()
    connection = connect(config)
    print("\nAdding a student")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into Students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("New student successfully added with data:", first_name, last_name, email, enrollment_date)
    print("")

def updateStudentEmail(student_id, new_email): #Update student EMAIL
    config = load_config()
    connection = connect(config)
    print("\nUpdating student data:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("update Students set email=%s where student_id=%s;", (new_email, student_id)) #SQL Statement to update
            connection.commit() #Commit any pending transaction to the database.

            print("Student email successfully updated\n")

            connection.close()
    
def deleteStudent(student_id): #DELETE student data row from table
    config = load_config()
    connection = connect(config)
    print("\nDeleting student data:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("delete from Students where student_id=%s;", (student_id)) #SQL statement to delete
            connection.commit() #Commit any pending transaction to the database.

            print("Delete Student Operation Successfully Recieved by Database\n")

            connection.close()

if __name__ == '__main__':
    getAllStudents()
    #addStudent('Student D', 'Student D', 'D@email.com', '2002-02-22')
    #updateStudentEmail('3', 'jim.beam@example.com')
    getAllStudents()
