# Cache Return Values

# Implement a decorator that chaces the return value of a function, so that when its called with the same arguments, the caced value is returned instead of re-executing the function

import time

def cache(func):

    cache_value = {}

    def wrapper(*args):

        if args in cache_value:
            return cache_value[args]
        
        result = func(*args)

        cache_value[args] = result

        return result
    return wrapper

@cache
def long_running_function(a , b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(5,5))