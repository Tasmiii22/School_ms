#keywords i classes
#Special methods
# 1=__init__
# 2=__str__
# 3=__repr__
# 4= __call__

# class Student:
#   def __init__(self,roll_no,name,marks):
#     self.roll_no=roll_no
#     self.name=name
#     self.marks=marks

# stu_info=Student(10,"Sana",80)
# print(stu_info.roll_no,stu_info.name,stu_info.marks)
  

# class Student:
#   def __init__(self,roll_no,name,marks):
#     self.roll_no=roll_no
#     self.name=name
#     self.marks=marks

#   def __str__(self):
#     return f"Student roll no is {self.roll_no},Name is {self.name} and marks is {self.marks}"
  
# s=Student(1,"abc",80)
# print(s)


# __repr__
# class Student:
#   def __init__(self,roll_no,name,marks):
#     self.roll_no=roll_no
#     self.name=name
#     self.marks=marks

#   def __repr__(self):
#     return f"Student roll no is {self.roll_no!r},Name is {self.name!r} and marks is {self.marks!r}"
  
# s=Student(1,"abc",80)
# print(repr(s))


# __call__
# class Calc:
#   def __init__(self,a):
#     self.a=a
#   def __call__(self,b):
#     return self.a+b
# res=Calc(4)
# print(res(3))

# class Power:
#   def __init__(self,exponent):
#      self.exponent=exponent
#   def __call__(self,base):
#     return self.exponent**base
# res=Power(2)
# print(res(4))

# class Counter:
#   def __init__(self):
#     self.count=0
#   def __call__(self):
#     self.count+=1
#     return self.count
# c=Counter()
# print(c())
# print(c())
# print(c())

class Discount:
  def __init__(self,name,percentage):
    self.name=name
    self.percentage=percentage
  def __str__(self):
    return f"Discount {self.name} {self.percentage}% Off"    
  def __repr__(self):
    return f"Discount {self.name!r} {self.percentage!r}% Off"  
    
  def __call__(self,price):
    dis_price=(price*self.percentage/100)
    return dis_price
  
sat=Discount("26 jan",10)
diwali=Discount("diwalii",15)
print([sat,diwali])    
  
print(sat(2000))