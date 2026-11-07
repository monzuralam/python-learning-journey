"""
Python Decorators
"""
def hello_decorators(func):
    def inner_func():
        print("Hi, Decorator")
        func()
        print("Thanks")
    return inner_func

@hello_decorators # auto execute the decorator function

def hello_world():
    print("Hello World")

hello_world()

@hello_decorators
def hello_line():
    print("=======================")

hello_line()