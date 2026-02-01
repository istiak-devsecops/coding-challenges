# use class variable

class Student:

    class_year = 2025       # class variable
    num_students = 0

    def __init__(self, name, age):
        self.name = name 
        self.age = age
        Student.num_students += 1


student1 = Student("shoaib", 20)
student2 = Student("rafian", 22)
student3 = Student("rafsan", 24)
student4 = Student("raian", 18)

# used class variable to get the output
print(f"Total number of student in the class was {Student.num_students} in year {Student.class_year}")
print(f"Student {student1.name} was {student1.age} years old.")
print(f"Student {student2.name} was {student2.age} years old.")
print(f"Student {student3.name} was {student3.age} years old.")
print(f"Student {student4.name} was {student4.age} years old.")


 