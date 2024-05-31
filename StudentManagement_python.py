Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class StudentManagementSystem:
...     def __init__(self):
...         self.students = {}
... 
...     def add_student(self, id, name, age, grade):
...         self.students[id] = {'name': name, 'age': age, 'grade': grade}
... 
...     def remove_student(self, id):
...         if id in self.students:
...             del self.students[id]
...             print("Student removed successfully!")
...         else:
...             print("Student not found!")
... 
...     def display_student(self, id):
...         if id in self.students:
...             print("Student ID:", id)
...             print("Name:", self.students[id]['name'])
...             print("Age:", self.students[id]['age'])
...             print("Grade:", self.students[id]['grade'])
...         else:
...             print("Student not found!")
... 
...     def display_all_students(self):
...         print("All Students:")
...         for id, student in self.students.items():
...             print("Student ID:", id)
...             print("Name:", student['name'])
...             print("Age:", student['age'])
...             print("Grade:", student['grade'])
...             print()
... 
... sms = StudentManagementSystem()
... 
... while True:
...     print("\nMenu:")
...     print("1. Add Student")
...     print("2. Remove Student")
...     print("3. Display Student")
...     print("4. Display All Students")
...     print("5. Exit")
...     choice = input("Enter your choice: ")
... 
...     if choice == '1':
...         id = int(input("Enter student ID: "))
...         name = input("Enter student name: ")
...         age = int(input("Enter student age: "))
...         grade = input("Enter student grade: ")
...         sms.add_student(id, name, age, grade)
...         print("Student added successfully!")
... 
...     elif choice == '2':
...         id = int(input("Enter student ID to remove: "))
...         sms.remove_student(id)
... 
...     elif choice == '3':
...         id = int(input("Enter student ID to display: "))
...         sms.display_student(id)
... 
...     elif choice == '4':
...         sms.display_all_students()
... 
...     elif choice == '5':
...         print("Exiting...")
...         break
... 
    else:
        print("Invalid choice! Please choose a number from 1 to 5.")
