import threading
import time

def task1():
    for i in range(3):
        print("Task 1 is processing...")
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2 is processing...")
        time.sleep(1)

# creating thread
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# starting thread
t1.start()
t2.start()

# wait for both to finish
t1.join()
t2.join()

print("Both task being finished.")