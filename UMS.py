#Implementing a CLI university system 
#Each role has its own menu and functionalities



#This is hthe main menu 
def main_menu():
 while True:
  print(" -- Wlcome to UMS --")
  print("1.Administrator")
  print("2.Lecturer")
  print("3.Student")
  print("4. Registerar")
  print("5. Accountant")
  print("6.Exit")
  choice = input("Select your role (1-6): ")
  if choice == '1':
        administrator_menu()
  elif choice == '2':
        lecturer_menu()
  elif choice == '3':
        student_menu()
  elif choice == '4':
        registrar_menu()
  elif choice == '5':
        accountant_menu()
  elif choice == '6':
        print("Exiting the system. Goodbye!")
        break
  else:
        print("Invalid choice. Please try again.")

main_menu