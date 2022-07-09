show = True
from functools import wraps


def decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before func")
        if show:
            result = func(*args, **kwargs)
        else:
            print("Funkcja nie jest wykonana")
        print("po funkcji")
        return result

    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    # wrapper.__annotations__ = func.__annotations__
    return wrapper


@decor
def foo(x: str):
    """Dokumentacja funkcji foo"""
    print("foo")
    return 10


@decor
def bar():
    print("bar")


# foo = decor(foo)


print(foo.__name__)
print(foo.__doc__)
print(foo.__annotations__)

x = foo("ddd")
bar()
print(x)
