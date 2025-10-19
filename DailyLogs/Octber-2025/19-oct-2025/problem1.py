# Create a @timer decorator that prints how long a function took to run.


import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Function '{func.__name__}' took {duration:.4f} seconds.")
        return result
    return wrapper
