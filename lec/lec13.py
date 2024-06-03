def mul_rational(x,y):
    return rational(numer(x)* numer(y), denom(x)* denom(y))

def add_rational(x,y):
    """add rational numbers x and y"""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * ny + ny * nx, dx *dy)

def rational_are_equal(x,y):
    """Multiply shether rational numbers x and y"""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))

# from fractions import gcd

def rational(n, d):
    """Construct a rational number x that represents n/d"""
    # g = gcd(n,d)
    # return [n//g, d//g]
    return [n, d]

def numer(x):
    """Return the numerator of rational number x"""
    return x[0]

def denom(x):
    """Return the denominator of rational number x"""
    return x[1]