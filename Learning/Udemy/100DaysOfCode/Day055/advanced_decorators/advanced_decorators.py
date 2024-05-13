# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper_function(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It return: {function(*args)}")

    return wrapper_function


# Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a + b + c


a_function(1, 2, 3)
