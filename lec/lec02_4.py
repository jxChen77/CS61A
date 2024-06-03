from operator import floordiv, mod
def divide_exact(n, d):
    """Return the quotirnt and reminder of dividing N ny D

    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n,d), mod(n,d)

def absolute_value(x):
    """Return the absolute value of x"""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
    