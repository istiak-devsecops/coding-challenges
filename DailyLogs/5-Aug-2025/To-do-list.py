# To-Do List

def main():
    to_do_list = []

    while True:
        task = input("Write a task(type 'exit' to stop).")

        if task.lower() == "exit": 
            print("\n Here are your to-do list: ")
            for t in to_do_list:
                print("-",t)
            break
        
        to_do_list.append(task) #add new task in the to_do_list
        print(f"Added: {task}")

if __name__ == "__main__":
    main()
