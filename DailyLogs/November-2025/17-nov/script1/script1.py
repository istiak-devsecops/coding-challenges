# command line arguments parser
 
import os
import sys

# check if there are not 3 arguments then put an expected input type
if len(sys.argv) != 3:
    print(f"Usage: python3 script.py <file name> <--count-lines | --count-words>")
    sys.exit(1)


file_path = sys.argv[1]     # 2nd arguments
flags = sys.argv[2]         # 3rd arguments

# total line count function
def count_lines(filepath):  
    total_lines = 0
    with open(filepath, 'r')as file:
        for _ in file:
            total_lines += 1
    return total_lines  

# total word count function
def count_words(filepath):
    total_words = 0
    with open(filepath, 'r')as file:
        for line in file:
            words = line.split()
            total_words += len(words)
        return total_words

# check if the file exist
if not os.path.isfile(file_path):
    print(f"{file_path} does not exist.")
    sys.exit(1)

# verify the flag and run the correct function
if flags == "--count-lines":
    print(f"Total lines: {count_lines(file_path)}")
elif flags == "--count-words":
    print(f"Total words: {count_words(file_path)}")
else:
    print(f"ERROR: unknown flag. Only use '--count-lines' or '--count-words'")
    sys.exit(1)
