students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        student = {}
        student["id"] = int(input("Enter ID: "))
        student["name"] = input("Enter Name: ")
        student["age"] = int(input("Enter Age: "))
        student["course"] = input("Enter Course: ")

        marks = []
        for i in range(3):
            mark = int(input(f"Enter Mark {i+1}: "))
            marks.append(mark)

        student["marks"] = marks
        students.append(student)

        print("Student Added Successfully!")

    # View All Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                average = sum(student["marks"]) / len(student["marks"])
                print("----------------------------")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                print("Average:", average)

    # Update Student
    elif choice == "3":
        id = int(input("Enter Student ID to Update: "))
        found = False

        for student in students:
            if student["id"] == id:
                student["name"] = input("Enter New Name: ")
                student["age"] = int(input("Enter New Age: "))
                student["course"] = input("Enter New Course: ")

                marks = []
                for i in range(3):
                    mark = int(input(f"Enter New Mark {i+1}: "))
                    marks.append(mark)

                student["marks"] = marks
                print("Student Updated Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found.")

    # Delete Student
    elif choice == "4":
        id = int(input("Enter Student ID to Delete: "))
        found = False

        for student in students:
            if student["id"] == id:
                students.remove(student)
                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found.")

    # Search Student
    elif choice == "5":
        name = input("Enter Student Name: ").lower()
        found = False

        for student in students:
            if student["name"].lower() == name:
                average = sum(student["marks"]) / len(student["marks"])
                print("----------------------------")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                print("Average:", average)
                found = True

        if not found:
            print("Student Not Found.")

    # Exit
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice! Please try again.")