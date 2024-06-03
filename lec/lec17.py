def evens(start, end):
    even = start + (start%2)
    while even < end:
        yield even
        even +=2

def a_then_b(a, b):
    for x in a :
        yield x
    for x in b :
        yield x

# def a_then_b(a, b):
#     yield from a
#     yield from b

def countdown(k):
    if k> 0:
        yield k
        # for x in countdown(k-1):
        #     yield x
        yield from countdown(k-1)

