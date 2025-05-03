"""
create Account class with 2 attributes- balance and account no.
create methods for debit, credit and printing the balance
"""

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.accountno=acc

    def debit(self,amount):
        self.balance -=amount
        print("$",amount," was debited")
        print("total balance =",self.get_balance())


    def credit(self,amount):
        self.balance += amount
        print("$", amount, " was credited")
        print("total balance =", self.get_balance())


    def get_balance(self):
        return self.balance

acc1=Account(10000,101)
print("The balance in account is ",acc1.balance)
# print(acc1.accountno)

acc1.credit(300)
acc1.debit(100)