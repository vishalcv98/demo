def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    # version 2: with input validation
    if a is None or b is None:
        return 0
    return a * b