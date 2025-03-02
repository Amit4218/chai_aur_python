# Timing Function Execution

# write a decorator that mesures the time a function takes to execute

import time

def timer(func):
    def wrapper(*args, **Kwargs):
        start = time.time()
        resut = func(*args, **Kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start}")
        return resut
    return wrapper


@timer
def example(n):
    time.sleep(n)


example(2)