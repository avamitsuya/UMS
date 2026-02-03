#A branch for the administration of the User Management System (UMS)
#7 functions are required from the administration 
import random
#1.
def add_new_module():
  module_code = "MOD" + str(random.randint(100, 999))
  moudle_name = input("Enter the module name: ")
  module_creidits = int(input("Enter the module credits: "))
  with open ("modules.txt", "a") as file:
      file.write(f"{module_code},{moudle_name},{module_creidits}\n")
  print("Module added successfully!")

#2.
def add_student():
    student_id = "STU" + str(random.randint(1000, 9999))
    student_name = input("Enter the student name: ")
    student_email = input("Enter the student email: ")
    student_GPA = float(input("Enter the student GPA: "))
    with open ("students.txt", "a") as file:
        file.write(f"{student_id},{student_name},{student_email},{student_GPA}\n")
    print("Student added successfully!")
#3.
def remove_student():
    student_id = input("Enter the student ID to remove: ")
    with open("students.txt", "r") as file:
        lines = file.readlines()
        try:
         for line in lines:
            if line.startswith(student_id):
                lines.remove(line)
                with open("students.txt", "w") as file:
                    file.writelines(lines)
                print("Student removed successfully!")
                return
        except:
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
def Remove_lecturer():
    lecturer_id = input("Enter the lecturer ID to remove: ")
    with open("lecturers.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(lecturer_id):
                lines.remove(line)
                with open("lecturers.txt", "w") as file:
                    file.writelines(lines)
                print("Lecturer removed successfully!")
                return

#6 
def update_lecturer():
    lecturer_id = input("Enter the lecturer ID to update: ")
    with open("lecturers.txt", "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith(lecturer_id):
            lecturer_name = input("Enter the new lecturer name: ")
            lecturer_email = input("Enter the new lecturer email: ")
            lines[i] = f"{lecturer_id},{lecturer_name},{lecturer_email}\n"
            with open("lecturers.txt", "w") as file:
                file.writelines(lines)
            print("Lecturer updated successfully!")
            return


#7.
def generate_reports():
    pass
    

#8.
def view_data():
    pass

#9. Back to main menu 

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
        print("9. Back to Main Menu")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            add_new_module()
        elif choice == '2':
            add_student()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            add_lecturer()
        elif choice == '5':
            Remove_lecturer()
        elif choice == '6':
            update_lecturer()
        elif choice == '7':
            generate_reports()
        elif choice == '8':
            view_data()
        elif choice == '9':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")

adminstartor_menu() 