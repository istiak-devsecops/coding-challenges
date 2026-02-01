#Implement a queue where people join at the back and leave from the front.

from collections import deque
people = ["Alice", "Bob", "Charlie", "Diana"]
dq = deque()

for person in people:
    dq.append(person)
    print(f"{person} joined the {list(dq)}")

while dq:
    leaving = dq.popleft()
    print(f"{leaving} left the {list(dq)}")