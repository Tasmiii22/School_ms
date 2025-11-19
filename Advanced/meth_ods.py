class Maths:
  factor=10
  def __init__(self,base):
    self.base=base
  def multiply(self,n):
    return (self.base*n)*Maths.factor
  
  @classmethod
  def change_fac(cl,new_fac):
    cl.factor=new_fac
  @staticmethod
  def is_even(n):
    return n%2==0
  
num=Maths(2)
print(num.multiply(3))

Maths.change_fac(6)
print(num.multiply(5))


print(Maths.is_even(3))
print(num.is_even(2))

