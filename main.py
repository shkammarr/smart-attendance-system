import os

while True:

    os.system("cls")  # Windows

    print("=" * 50)
    print("     UNIVERSAL FACE ATTENDANCE SYSTEM")
    print("=" * 50)

    print("1. Register New Person")
    print("2. Train Face Model")
    print("3. Mark Attendance")
    print("4. View Registered Persons")
    print("5. Attendance Report")
    print("6. Edit Person")
    print("7. Delete Person")
    print("8. Exit")

    print("-" * 50)

    choice = input("Enter your choice : ")

    if choice == "1":
        os.system("python register_person.py")

    elif choice == "2":
        os.system("python train_model.py")

    elif choice == "3":
        os.system("python attendance.py")

    elif choice == "4":
        os.system("python view_persons.py")

    elif choice == "5":
        os.system("python attendance_report.py")

    elif choice == "6":
        os.system("python edit_person.py")

    elif choice == "7":
        os.system("python delete_person.py")

    elif choice == "8":
        print("\nThank you for using Universal Face Attendance System.")
        break

    else:
        print("\nInvalid Choice!")

    input("\nPress Enter to continue...")