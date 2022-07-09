from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()  # 1000
        result = func(*args, **kwargs)
        stop = time.time()  # 1002
        print(f"{func.__name__} takes {stop - start} seconds")
        return result

    return wrapper


@timeit
def sleeeping(n: int = 1):
    "Sleeps"
    time.sleep(n)
    return 10


def test_decorated_func():
    assert sleeeping.__name__ == "sleeeping"
    assert sleeeping.__doc__ == "Sleeps"
    assert sleeeping.__annotations__ == {"n": int}
    assert sleeeping(1) == 10
