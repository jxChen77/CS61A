def fib(n):
    assert isinstance(n, int) and n >= 0, "Please enter a proper index, positive and full num"
    if n <= 1:
        return n
    else: return fib(n-2) + fib(n-1)

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count=0
    return counted


def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n]=f(n)
        return cache[n]
    return memoized

def exp(b,n):
    if n == 0:
        return 1
    else:
        return b * exp(b,n-1)
    
def exp_fast(b,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b,n-1)
    
def square(x):
    return x * x

# def factor_fast(n):
#     total = 0
#     sqrt_n = sqrt(n)
#     k = 1
#     while k <sqrt_n:
#         if divides(k,n):
#             total += 2
#         k+=1
#     if k*k == n :
#         total += 1
#     return total

# def count_frames(f):
#     def counted(n):
#         counted.open_count += 1
#         if counted.open_count > counted.max_count:
#             counted.max_count = counted.open_count
#         result = f(n)
#         counted.open_count -= 1

#     counted.open_count = 0
#     counted.max_count = 0
#     return counted