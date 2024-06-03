class Ratio:

    def __init__(self, n, d):
        self.numer = n
        self.denom = d
        
    def __repr__(self) -> str:
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return f'{self.numer}/{self.denom}'
    
    def __add__(self, other):
        if isinstance(other,int):
            n = self.numer + other*self.denom
            return Ratio(n, self.denom)
        
        elif isinstance(other,Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
            g = gcd(n,d)
            return Ratio(n//g,d//g)
        elif isinstance(other, float) :
            return float(self) + other
    
    def __float__(self):
            return self.numer / self.denom
    __radd__ = __add__
def gcd(n,d):
    while n!=d:
        n,d = min(n,d), abs(n-d)
    return n