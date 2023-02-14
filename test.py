def twice(f):
    return lambda x: f(f(x))

@twice
def f(x):
    return x + 1

def compose(f, g):
    return lambda *args, **kwargs: g(f(*args, **kwargs))

def turn_odd(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return turn_odd(n // 10) * 10 + n % 2
    else:
        return turn_odd(n // 10) * 10  + n % 2 + 1
    
print(turn_odd(100))