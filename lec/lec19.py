class Account():
    """An account has a balance and a holder

    >>> a = Account('John')
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    """

    insterest = 0.02

    def __init__(self, account_holder, balance=0):
        self.holder = account_holder
        self.balance = balance
    
    # def holder(self):
    #     return self.holder
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance 
    
    def withdraw(self, amount):
        if self.balance < amount:
            return 'Insufficient funds'
        else:
            self.balance -= amount
            return self.balance
    
    def changeIns(self, amount):
        self.insterest = amount
        return self.insterest
    # def balance(self):
    #     return self.balance
