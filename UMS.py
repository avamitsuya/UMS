# User Management System (UMS) - Administration, Lecturer, and Student 

import random
#1.
def add_new_module():
  module_code = "MOD" + str(random.randint(100, 999))
  moudle_name = input("Enter the module name: ")
  module_creidits = int(input("Enter the module credits: "))
  assigned_lecturer = input("Enter lecturer ID: ")
  with open ("modules.txt", "a") as file:
      file.write(f"{module_code},{moudle_name},{module_creidits},{assigned_lecturer}\n")
  print("Module added successfully!")

#2.
def add_student():
    student_id = "STU" + str(random.randint(1000, 9999))
    student_name = input("Enter the student name: ")
    student_email = input("Enter the student email: ")
    student_GPA = float(input("Enter the student GPA: "))
    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if student_name == data[1] or student_email == data[2]:
                print("Student already exists.")
                return
    with open ("students.txt", "a") as file:
        file.write(f"{student_id},{student_name},{student_email},{student_GPA}\n")
    
    print("Student added successfully!")

    
        
#3.
def remove_student():
    student_id = input("Enter the student ID to remove: ")
    with open("students.txt", "r") as file:
        lines = file.readlines()
        found = False

        for line in lines:
            if line.startswith(student_id):
                lines.remove(line)
                found = True
                break
        if found:
            with open("students.txt", "w") as file:
                file.writelines(lines)
                print("Student removed successfully!")
                return
        else:
         print("Student ID not found.")


#4.
def add_lecturer(): #Add/remove/update
    lecturer_id = "LEC" + str(random.randint(100, 999))
    lecturer_name = input("Enter the lecturer name: ")
    lecturer_email = input("Enter the lecturer email: ")
    with open ("lecturers.txt", "a") as file:
        file.write(f"{lecturer_id},{lecturer_name},{lecturer_email}\n")
        print("Lecturer added successfully!")

#5
def remove_lecturer():
    lecturer_id = input("Enter the lecturer ID to remove: ")
    with open("lecturers.txt", "r") as file:
        lines = file.readlines()
        found = False
        for line in lines:
            if line.startswith(lecturer_id):
                lines.remove(line)
                found = True
                break
        if found:
                with open("lecturers.txt", "w") as file:
                    file.writelines(lines)
                print("Lecturer removed successfully!")
                return
        else:
            print("Lecturer ID not found.")

#6 
def update_lecturer():
    lecturer_id = input("Enter the lecturer ID to update: ")
    with open("lecturers.txt", "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith(lecturer_id):
            data = line.strip().split(",")
            lecturer_name = data [1]
            lecturer_email = input("Enter the new lecturer email: ")
            lines[i] = f"{lecturer_id},{lecturer_name},{lecturer_email}\n"
            with open("lecturers.txt", "w") as file:
                file.writelines(lines)
            print("Lecturer updated successfully!")
            return


#7.
def generate_reports():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        total_students = len(students)

        total_gpa = 0
        for line in students:
            data = line.strip().split(",")
            gpa = float(data[3])  # GPA is the 4th value
            total_gpa += gpa

        if total_students > 0:
            average_gpa = total_gpa / total_students
        else:
            average_gpa = 0

    except FileNotFoundError:
        total_students = 0
        average_gpa = 0

    # Count modules
    try:
        with open("modules.txt", "r") as file:
            modules = file.readlines()
        total_modules = len(modules)
    except FileNotFoundError:
        total_modules = 0

    # Count lecturers
    try:
        with open("lecturers.txt", "r") as file:
            lecturers = file.readlines()
        total_lecturers = len(lecturers)
    except FileNotFoundError:
        total_lecturers = 0

    # Display report
    print("\n--- System Report ---")
    print(f"Total Students: {total_students}")
    print(f"Total Modules: {total_modules}")
    print(f"Total Lecturers: {total_lecturers}")
    print(f"Average Student GPA: {average_gpa:.2f}")
    print("---------------------\n")
    

#8.
def view_data ():
    while True:
        print("\nView Data Menu")
        print("1. View Students")
        print("2. View Lecturers")
        print("3. View Modules")
        print("4. Back to Administration Menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_students()
        elif choice == '2':
            view_lecturers()
        elif choice == '3':
            view_modules()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
#8.1
def view_students():
    with open("students.txt", "r") as f:
        print("\nStudents: ")
        for line in f:
            print(line.strip())

#8.2
def view_lecturers():
    with open("lecturers.txt", "r") as f:
        print("\nLecturers: ")
        for line in f:
            print(line.strip())

#8.3
def view_modules():
    with open("modules.txt", "r") as f:
        print("\nModules: ")
        for line in f:
            print(line.strip())

#9. Add users

def add_user():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    role = input("Enter role (admin/lecturer/student): ")
    with open("users.txt", "a") as file:
        file.write(f"{username},{password},{role}\n")
    print("User added successfully!")

def adminstartor_menu():
    while True:
        print("\nUser Management System - Administration Menu")
        print("1. Add New Module")
        print("2. Add Student")
        print("3. Remove Student")
        print("4. Add Lecturer")
        print("5. Remove Lecturer")
        print("6. Update Lecturer")
        print("7. Generate Reports")
        print("8. View Data")
        print("9. Add User")
        print("10. Back to Main Menu")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == '1':
            add_new_module()
        elif choice == '2':
            add_student()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            add_lecturer()
        elif choice == '5':
            remove_lecturer()
        elif choice == '6':
            update_lecturer()
        elif choice == '7':
            generate_reports()
        elif choice == '8':
            view_data()
        elif choice == '9':
            add_user()
        elif choice == '10':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")


#This is the lecturer's sections 
#1.
def view_assigned_modules():
    ID = input("Enter your ID to view assigned modules: ")
    with open ("modules.txt", "r") as f:
        lines = f.readlines()
        found = False
        for line in lines:
            data = line.strip().split(",")
            ID = data[3]
            if ID == data[3]:
                print(f"Module Code: {data[0]}, Module Name: {data[1]}, Module Credits: {data[2]}")
                found = True
        if not found:
            print("No modules assigned to this lecturer ID.")


#2.
def record_grades():
    student_id = input("Enter the student ID to record grade: ")
    module_code = input("Enter the module code: ")
    grade = input("Enter the grade: ")
    with open("grades.txt", "a") as file:
        file.write(f"{student_id},{module_code},{grade}\n")
    print("Grade recorded successfully!")

def track_attendance():
    student_id = input("Enter the student ID to track attendance: ")
    module_code = input("Enter the module code: ")
    attendance_status = input("Enter attendance status (Present/Absent): ")
    with open("attendance.txt", "a") as file:
        file.write(f"{student_id},{module_code},{attendance_status}\n")
    print("Attendance recorded successfully!")

def view_students_grades():
    module_code = input("Enter the module code to view student grades: ")
    with open("grades.txt", "r") as file:
        lines = file.readlines()
        found = False
        for line in lines:
            data = line.strip().split(",")
            if data[1] == module_code:
                print(f"Student ID: {data[0]}, Grade: {data[2]}")
                found = True
        if not found:
            print("No grades found for this module code.")
    
def lecturer_menu():
    while True:
        print("\nUser Management System - Lecturer Menu")
        print("1. View Assigned Modules")
        print("2. Record Grades")
        print("3. Track Attendance")
        print("4. View Students' Grades")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_assigned_modules()
        elif choice == '2':
            record_grades()
        elif choice == '3':
            track_attendance()
        elif choice == '4':
            view_students_grades()
        elif choice == '5':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
    
               
#This is the student section
#1.
def view_available_modules():
    with open("modules.txt", "r") as file:
        print("\nAvailable Modules: ")
        for line in file:
            print(line.strip())

#2.
def enroll_in_module():
    student_id = input("Enter your student ID: ")
    module_code = input("Enter the module code to enroll: ")
    with open("enrollments.txt", "a") as file:
        file.write(f"{student_id},{module_code}\n")
    print("Enrolled in module successfully!")

def view_grades():
    student_id = input("Enter your student ID to view grades: ")
    with open("grades.txt", "r") as file:
        lines = file.readlines()
        found = False
        for line in lines:
            data = line.strip().split(",")
            if data[0] == student_id:
                print(f"Module Code: {data[1]}, Grade: {data[2]}")
                found = True
        if not found:
            print("No grades found for this student ID.")

def unenroll_from_module():
    student_id = input("Enter your student ID: ")
    module_code = input("Enter the module code to unenroll: ")
    with open("enrollments.txt", "r") as file:
        lines = file.readlines()
    with open("enrollments.txt", "w") as file:
        found = False
        for line in lines:
            data = line.strip().split(",")
            if data[0] == student_id and data[1] == module_code:
                found = True
                continue
            file.write(line)
        if found:
            print("Unenrolled from module successfully!")
        else:
            print("Enrollment record not found.")

def student_menu():
    while True:
        print("\nUser Management System - Student Menu")
        print("1. View Available Modules")
        print("2. Enroll in Module")
        print("3. View Grades")
        print("4. Unenroll from Module")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_available_modules()
        elif choice == '2':
            enroll_in_module()
        elif choice == '3':
            view_grades()
        elif choice == '4':
            unenroll_from_module()
        elif choice == '5':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")


#Login
def login():
    while True:
     username = input("Enter your username:")
     password = input("Enter your password: ")
     with open("users.txt", "r") as file:
        for line in file:
            user = line.strip().split(",")
            if username == user[0] and password == user[1]:
                print(f"Login successful! Welcome, {username}.")
                role = user[2]
                if role == "admin":
                    adminstartor_menu()
                elif role == "lecturer":
                    lecturer_menu()
                elif role == "student":
                    student_menu()
            else:
                print("Invalid username or password. Please try again.")
            


login()
            
        
