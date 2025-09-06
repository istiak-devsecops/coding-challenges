# Write a list to the file

with open("coins.txt","a", buffering=1) as file:
    while True:
        user_input = input("write a crypto coin name: ")
        if user_input == "exit":
            break
        file.write(user_input + "\n")
        print(f"Saved: {user_input}")
