# Writing multiple notes, Reading and printing them cleanly


def writing_notes(filename, message):
    with open(filename, 'a') as file:
        file.write(message + '\n')

def reading_notes(filename):
    with open(filename, 'r') as file:
        return file.readlines()
    
writing_notes('notes.txt','This is the first note of note taker app!')
notes = reading_notes('notes.txt')
for line in notes:
    print(line.strip())


