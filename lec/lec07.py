# from ucb import trace


def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def trace1(fn):
    """return a version of fn that first print before
    it is called
    
    fn - a function of 1 argument
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return  traced
        
#@trace1
def square(x):
    return x*x
#square = trace1(square)

@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k<=n :
        total, k = total + square(k), k+1
    return total

def search (f):
    x = 0
    while True:
        if f(x):
            return x
        x +=1

def is_three(x):
    return x == 3

def positive(x):
    return max(0, square(x)-100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x"""
    return lambda y: search(lambda x: f(x) ==y)

