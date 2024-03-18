import DML

def takeInput():
    print("What operation would you like to perform on the database?")
    print("---------------------------------------------------------")
    print("1. Get all students\n2. Add a student\n3. Update a student's email\n4. delete a student\n")
    print("Type 'quit' to quit the program\n")
    action = input("Action: ")

    return action

def actionLoop():
    action = takeInput()

    while (action.lower() != 'quit'):
        if (action == '1'):
            DML.getAllStudents()

        
        elif (action == '2'):
            print("You chose to add a student, please input the desired data")
            first_name = input("Student's first name: ")
            last_name = input("Student's last name: ")
            email = input("Student's email: ")
            enrollment_date = input("Enrollment Date (YYYY-MM-DD): ")

            DML.addStudent(first_name, last_name, email, enrollment_date)

        elif (action == '3'):
            print("You chose to update a student's email, please input the desired data")
            id = input("ID of student to update: ")
            email = input("Desired new email: ")

            DML.updateStudentEmail(id,email)
        
        elif (action == '4'):
            print("You chose to delete a student, please input the desired data")
            id = input("ID of student to delete: ")

            DML.deleteStudent(id)

        else:
            print("Invalid action, please try again")
        
        action = takeInput()
    
    print("Shutting down...")



if __name__ == '__main__':
    actionLoop()
