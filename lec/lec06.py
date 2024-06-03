def make_adder(n):
    """return a function that take K and return K + n 

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x*x

def triple(x):
    return 3*x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
