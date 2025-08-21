from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"🚀 Calling function: {func.__name__}")
        func(*args, **kwargs)
        print(f"Finished calling function: {func.__name__}")

    return wrapper


@logger
def call(number, saved="not_saved"):
    print(f"Getting call from: {number}, this person is {saved}")


call(123456789)
