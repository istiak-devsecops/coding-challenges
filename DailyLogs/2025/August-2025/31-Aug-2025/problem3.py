# filter dict by value. keep only students with marks >= 70

marks = {"Alice": 85, "Bob": 60, "Charlie": 95, "David": 45}

def filter_mark(status):
    result = {}
    for name, mark in status.items():
        if mark >= 70:
            result[name] = mark
    return result

print(filter_mark(marks))
    