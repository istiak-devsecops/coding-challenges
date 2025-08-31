# Invert a Dictionary (Swap Keys and Values)

from collections import defaultdict

status = {"git": "installed", "docker": "missing", "ansible": "installed"}

inverted = defaultdict(list)
for key, value in status.items():
    inverted[value].append(key)

print(dict(inverted))

