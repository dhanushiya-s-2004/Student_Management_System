import sqlite3

print("===== STUDENT MANAGEMENT SYSTEM =====")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Delete Student")

choice = input("Enter your choice: ")

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

if choice == "1":
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")

    cursor.execute(
        "INSERT INTO students(name, age, department) VALUES (?, ?, ?)",
        (name, age, department)
    )

    conn.commit()
    print("Student Added Successfully!")

elif choice == "2":
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    for student in students:
        print(student)
        
elif choice == "3":
    search_name = input("Enter Student Name: ")

    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (search_name,)
    )

    students = cursor.fetchall()

    if students:
        for student in students:
            print(student)
    else:
        print("Student Not Found!")

elif choice == "4":
    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    print("Student Deleted Successfully!")

else:
    print("Invalid Choice!")

conn.close()