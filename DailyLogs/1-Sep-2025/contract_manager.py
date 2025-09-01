# Contract Manager
contract_book = {}

while True:
    print("\n--- Contact Manager ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Show all contacts")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        # Add user
        name = input("Enter name: ")
        number = int(input("Enter number: "))
        contract_book[name] = number
        print(f"Added {name}: {number}")

    elif choice == "2":
        # search user
        user_inquery = input("Search for a name: ")
        if user_inquery in contract_book:
            print(f"{user_inquery}: {contract_book[user_inquery]}")
        else:
            print("Contract not found.")

    elif choice == "3":
        # update user
        user_inquery = input("Search for a name: ")
        if user_inquery in contract_book:
            update_num = input("Enter the number.")
            contract_book[user_inquery] = update_num
            print(f"updated {user_inquery}: {update_num}")
        else:
            print("Contact not found")

    elif choice == "4":
        # Delete user
        user_inquery = input("Search for a name: ")
        if user_inquery in contract_book:
            del contract_book[user_inquery]
            print(f"Deleted {user_inquery}")
        else:
            print("Contact not found")
    
    elif choice == "5":
        # show all
        if contract_book:
            for user, number in contract_book.items():
                print(f"{user}: {number}")
        else:
            print("Contract not found.")
    
    elif choice == "6":
        # exit
        print("Exiting...")
        break

    else:
        print("Invalid option. try again.")


