
with open("example.txt", "w") as file:
    file.write("This is the 1st line.\nthis is the 2nd line.\nThis is the 3rd line.")

with open("example.txt", "r") as file:
    lines = file.readlines()

lines[2] = "This is the new 3rd line\n"

with open("example.txt", "r+") as file:
    file.writelines(lines)
    file.seek(0)
    print(file.read())
