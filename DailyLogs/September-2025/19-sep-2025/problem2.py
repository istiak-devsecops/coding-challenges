# Simulate a task queue.

# Add 10 tasks (task1 … task10).

# Pop from the left to simulate processing tasks one by one.


from collections import deque

Last_5_task = deque(maxlen=5)

# taking user input till user exit
while True:
    user_input = input("Write a task name: (exit for stop): ")
    if user_input.lower() == "exit":
        break
    Last_5_task.append(user_input)

print("Last 5 tasks are: ")
for task in Last_5_task:
    print("-", task)


