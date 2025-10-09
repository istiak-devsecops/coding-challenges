# Task 4: Write a function that takes a dictionary of student names and their scores,
# and returns a list of names who scored above 80.


#without list comprehention
def top_students(score_dict):
    student_scored_above_80 = []
    for student_name, score in score_dict.items():
        if score > 80:
            student_scored_above_80.append(student_name)
    return student_scored_above_80

students = {
    "Istiak": 95,
    "Rafi": 88,
    "Nadia": 92,
    "Sakib": 76,
    "Tania": 85
}

top_students_list = top_students(students)
print(top_students_list)

#with list comprehention
def top_student(score_dict):
    return [student_name for student_name,score in score_dict.items() if score > 80]

top_student_name = top_student(students)
print(top_student_name)