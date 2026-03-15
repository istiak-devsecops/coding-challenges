# Track votes for candidates in a dictionary without checking if the key exists first.

from collections import defaultdict
votes = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice"]

counts = defaultdict(int)

for vote in votes:
    counts[vote] += 1

print(dict(counts))