# Simulate a task queue.

# Add 10 tasks (task1 … task10).

# Pop from the left to simulate processing tasks one by one.


from collections import deque

#create task quence
task_quence = deque()

#add 10 task to the quence
for task_num in range (1,11):
    task_quence.append(f"task{task_num}")


#simulate processing task
print("Task processing...")
while task_quence:
    current_task = task_quence.popleft()
    print(f"-",current_task)

