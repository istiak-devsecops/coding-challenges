import time

def timer(func):        # timer is the decorator function here. This function can be reused to call the function inside it later.
    def wrapper(*args, **kwargs): # wrapper is the function that is wrapped by timer. This function holds the logic.
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timer    # this is the syntax of calling a decorator function
def slow_function():  # this is the extra features that will be added on top of the wrapper function logic.
    time.sleep(2)

slow_function()
