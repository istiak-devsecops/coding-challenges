# Group by length

from collections import defaultdict

animals = ["cat", "dog", "bear", "lion", "tiger"]
grouped = defaultdict(list)

for (
    animal
) in animals:  # loop through the list to get each animal length and define it as a key
    key = len(animal)
    grouped[key].append(animal)

grouped = dict(grouped)
print(grouped)
