
def log_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
