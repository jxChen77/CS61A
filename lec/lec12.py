def index (keys, values, match):
    """Return a dictionary from keys k to a list of values x for which 
    match(k, v) is a true value
    
    >>> index([7, 9, 11], range(30, 50), lambda k, v: v%k == 0)
    
    """

    return {k : [v for v in values if match(k,v)] for k in keys}