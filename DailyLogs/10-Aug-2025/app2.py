students = {
    "John": 85,
    "Sara": 92,
    "Mike": 76,
    "Emma": 59,
    "Tom": 68,
    "Anna": 95
}

passing_score = int(input("What will be the min passing score? "))

passed_student = {}

for student, score in students.items():
    if score >= passing_score:
        passed_student[student] = score

for student, score in passed_student.items():
    print(f"{student} - {score}")