def type_check(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("All arguments must be integers")
        return func(*args, **kwargs)
    return wrapper

@type_check
def add(a, b):
    return a + b

print(add(3, 5))       
print(add("3", 5))     
