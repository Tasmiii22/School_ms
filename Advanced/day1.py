#Encapsulation
class SBI:
  def __init__(self,owner,balance):
    self.owner=owner
    self.__balance=balance
  def deposit(self,amount):
    if amount>0:
      self.__balance+=amount
      return f"deposited{amount} and your current balance is {self.__balance}"
    return "Insufficient Balance"
  def withdraw(self,amount1):
     if amount1>0 and amount1<self.__balance:
       self.__balance-=amount1
       return f"₹{amount1} withdrawed your current balance is ₹{self.__balance}"
     return "Insufficient Balance"
  def check_bal(self):
     return self.__balance
sa=SBI("Tasmiya",50000)
print(sa.deposit(10000))
print(sa.withdraw(10000))



