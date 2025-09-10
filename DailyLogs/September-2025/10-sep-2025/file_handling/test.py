# testing file handling

with open("notes.txt", "w") as file:
    file.write("Hello world.\nThe world is evolving fast.\nThere is no time to waste")

with open("notes.txt", "a") as file:
    file.write("\nHello guys this is the 4th line")

with open("notes.txt", "a+") as file:
    file.write("\nThis is the 5th line.")
    file.seek(0)
    print(file.read())

with open("notes2.txt", "r+") as f:
    f.write("This is the new note.\nthis is the 2nd line of the new notes.")
    print(f.tell())
    f.seek(0)
    print(f.read())

