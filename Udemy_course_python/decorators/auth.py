from functools import wraps


def auth(func):
    @wraps(func)
    def wrapper(role):
        if role != "admin":
            print(f"Permissn Denied !")
            return None
        else:
            print(f"Permission granted: Calling {func.__name__}")
            return func(role)

    return wrapper


@auth
def get_info(role):
    pass


get_info("admin")
get_info("user")
