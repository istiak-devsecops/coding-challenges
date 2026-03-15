#split the list
num = [1,2,3,4,5,6]

def split_list(number):
    mid = len(number)//2
    return number[:mid], number[mid:]

print(split_list(num))

