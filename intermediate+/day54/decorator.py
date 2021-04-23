from time import sleep


# Python Decorator Functions
def delay_decorator(function):
    def wrapper_function():
        sleep(2)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


@delay_decorator
def say_greeting():
    print("How are you?")


say_bye()
say_greeting()
say_hello()
