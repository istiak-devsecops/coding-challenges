#write a string in reverse order

userInp = input("Write down a word. " )

reversed_text = userInp[::-1]   #slicing methods

print(reversed_text)

userInp2 = input("Write down a word. " )

oldSchool_reserve_txt = ""

for chr in userInp2:
    oldSchool_reserve_txt += oldSchool_reserve_txt

print(oldSchool_reserve_txt)
