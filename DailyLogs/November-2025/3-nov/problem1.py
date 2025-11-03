# use class variable

class Student:

    class_year = 2025       # class variable

    def __init__(self, name, age):
        self.name = name 
        self.age = age


student1 = Student("shoaib", 20)
student2 = Student("rafian", 22)

# used class variable to get the output
print(f"Student {student1.name} is {student1.age} years old and he is in class {Student.class_year}")
print(f"Student {student2.name} is {student2.age} years old and he is in class {Student.class_year}")
 