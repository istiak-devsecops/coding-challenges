# Implement an undo/redo system:
# Typing → append to right
# Undo → pop from right, store in another deque
# Redo → bring it back

from collections import deque
actions = ["Type A", "Type B", "Delete A", "Paste Text"]

dq = deque()
dq2 = deque()

for action in actions:
    dq.append(action)
    print(f"action performed: {action}")

print("\n_ _ _ undoing last two action _ _ _ ")
for _ in range(2):
    if dq:
        undone = dq.pop()
        dq2.append(undone)
        print(f"Undone: {undone}")

print("\n_ _ _ going to redo last 2 performance_ _ _")
if dq2:
    redone = dq2.pop()
    dq.append(redone)
    print(f"Redo done: {redone}")

print(f"\nFinal history: {list(dq)}")
print(f"Final history after redo: {list(dq2)}")