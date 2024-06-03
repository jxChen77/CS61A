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

    interest = 0.02

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
        self.interest = amount
        return self.interest
    # def balance(self):
    #     return self.balance

class CheckingAccount(Account):


    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount+self.withdraw_fee)

class Bank:
    """A bank has accounts.

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """
    def __init__ (self):
        self.accounts = []
    
    def open_account(self, holder, amount = 0, kind=Account):
        account = kind(holder, amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            #assert type(a) == Account
            a.deposit(a.balance*a.interest)
    
    def too_big_to_fail(self):
        return len(self.accounts) > 1



class A:
    z = -1
    def f(self,x):
        return B(x-1)


class B(A):
    n = 4
    def __init__ (self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)
    
class C(B):
    def f(self,x):
        return x
    
class SavingAccount(Account):
    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingAccount):

    def __init__ (self, account_holder, amount = 0):
        self.holder = account_holder
        self.balance = 1 + amount


        
    