# using zip in two var

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

name_score_collection = zip(names,scores)
print(list(name_score_collection))

# using reverse zip

pairs = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

student_name, student_score = zip(*pairs)
print(f"{student_name}\n{student_score}")