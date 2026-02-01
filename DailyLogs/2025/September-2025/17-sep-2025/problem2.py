#Group names by their first letter.
from collections import defaultdict
names = ["alice", "adam", "bob", "billy", "carol", "chris"]
grouped = defaultdict(list)

for name in names:
    first_letter = name[0].lower()
    grouped[first_letter].append(name)

print(dict(grouped))