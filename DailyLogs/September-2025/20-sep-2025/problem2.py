# count freq

from collections import defaultdict
text = "python python devops cloud cloud cloud"

counts = defaultdict(int)

for char in text.split():
    counts[char] += 1

print(dict(counts))