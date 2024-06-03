class Link:

    empty = ()

    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self) :
        if self.rest is Link.empty:
            return f'Link({self.first})'
        else:
            return  f'Link({self.first}, {repr(self.rest)})'    

    def __str__(self):
        if self.rest is Link.empty:
            return f'{self.first}'
        return f'{self.first} -> {self.rest}'

def square(x):
    return x * x

def odd(x):
    return x % 2 == 1

def range_link(start, end):
    """Return a Link containing consecutive integers from start to end
    
    >>> range_link(3,6)
    Link(3, Link(4, Link(5)))
    """

    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))


def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s.
    >>> map_link(square, range_link(3,6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    elif isinstance(s, Link):
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link that contains only elements x of Link s for which f(x) 
    is a true value.

    >>> filter_link(odd, range_link(3,6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    elif isinstance(s, Link):
        filtered_rest = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered_rest)
        else:
            return filtered_rest

def empty(s):
    return s==Link.empty

def add(s, v):
    """Add v to an ordered list s with no repeats, returning modified s."""
    # assert isinstance(s,Link)
    # temp_link = s
    # while temp_link.rest is not Link.empty and temp_link.first < v:
    #     temp_link = temp_link.rest
    
    # if temp_link.rest is Link.empty and temp_link.first < v:
    #     temp = Link(v, temp_link.rest)
    #     temp_link.rest = temp 

    # elif temp_link.first != v:
    #     temp = Link(temp_link.first, temp_link.rest)
    #     temp_link.rest = temp
    #     temp_link.first = v         
    # return s

    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest) 
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest,v)
    return s

class Tree:
    def __init__(self, label, branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self) -> str:
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return "Tree({0}{1})".format(repr(self.label), branch_str)
    
    def __str__(self):
        return '\n'.join(self.indented())
    
    def indented(self):
        lines = []
        for b in self.branches: 
            for line in b.indented():
                lines.append