# Count word frequencies in a paragraph.

from collections import defaultdict
text = "Python is great and Python is fun. Python powers the web."
counts = defaultdict(int)

for word in text.split():
    counts[word] += 1

print(counts)