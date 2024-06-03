def prime_factors(n):
    """print the prime factors of n in non-decreasing order
    
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_prime_factor(n)
        n = n // k
        print(k)

def smallest_prime_factor(n):
    """return the smallest prime factor k > 1 """
    k = 2
    while n % k!=0:
        k = k+1
    return k

def fib(n):
    """Compute the nth Fibonacci number, for N >=1"""
    # pred, curr = 0, 1   # 0th and 1st Fibonacci numbers
    # k = 1               # curr is the kth Fibonacci number
    pred, curr = 1, 0   
    k = 0               # curr is the kth Fibonacci number
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

def if_(c, t, f):
    if c:
        return t
    else:
        return f

from math import sqrt

def real_sqrt(x):
    """Return the real part of the square root of x."""
    # return if_(x>=0, sqrt(x), 0)    # every parts will be evaluated in this expression 
    if x >= 0:
        return sqrt(x)
    else:
        return 0

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10

def resonable(n):
    return n == 0 or 1/n != 0

from math import pi

def area(r, shape_constant):
    assert r > 0, 'A length must be greater than zero'
    return r * r * shape_constant
    

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 *sqrt(3)/2)

def identity (k) :
    return k

def cube(k):
    return pow(k,3) 

def summation(n, term):
    """Sum the first N terms of a sequence.
    
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total+term(k), k+1
    return total

def sum_naturals(n):
    """
    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k+1
    return total

def sum_cubes(n):
    """sum the first n cubes of natural numbers
    
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k+1
    return total

from operator import mul
def pi_term(k):
    return 8/ mul(4*k-1, 4*k-3)
