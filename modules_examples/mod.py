s: str  = "Yes we can"
a: list = [100, 200, 300]

def foo(arg):
    print(f"arg: {arg}")

class Foo(): pass

def print(*args, **kwargs):
    __builtins__.get('print')("You are hacked")

# print("x")

#
# print(dir(__builtins__))
# print(__builtins__.get('print'))