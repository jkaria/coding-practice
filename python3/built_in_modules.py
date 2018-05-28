#!/usr/local/bin/python3
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("{}({}, {}) -> {}".format(func.__name__, args, kwargs, res))
        return res
    return wrapper


@trace
def fibonacci(num):
    """Calculates fibonacci number for arg: num"""
    if num in (0, 1):
        return num
    return fibonacci(num-2) + fibonacci(num-1)

if __name__ == '__main__':
    print("Chap 6: Built-in modules concepts")
    result = fibonacci(3)
    print("fibonacci(3) is {}".format(result))
    help(fibonacci)
