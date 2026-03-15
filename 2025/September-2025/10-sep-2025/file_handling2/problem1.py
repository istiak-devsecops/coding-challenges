#creating a new file with 5 line text

with open("notes.txt", "w") as file:
    file.write("Hello python.\nthis is the 2nd line.\nthis is the 3rd line.\nthis is the 4th line.\nthis is the 5th line.")
    file.close()

with open("notes.txt", "a") as file:
    file.write("\nThis is the 6th line.\nThis is the 7th line")

try:
    with open("notes.txt", 'r') as file:
        for lines in file:
            print(lines)

except FileNotFoundError:
    print("File not found")