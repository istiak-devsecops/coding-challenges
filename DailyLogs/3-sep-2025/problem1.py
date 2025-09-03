#Grade checker
def grade_checker(score):
    if 90 <= score <= 100:
        return "Your grade is: A"
    elif 80<= score <= 89:
        return "Your grade is: B"
    elif 70<= score <= 79:
        return "Your grade is: C"
    elif 60<= score <= 69:
        return "Your grade is: D"
    elif score < 60:
        return "Your have Failed."

# Error handeling
while True:
    try:
        user_input = int(input("What is your score: "))
        if user_input > 100:
            print("Score can not be greater than 100.")
            continue
        elif user_input < 0:
            print("Score can not be negative value...")
            continue
        break

    except ValueError:
        print("Put a valid positive number...")

result = grade_checker(user_input)
print(result)