class Student:
  def study(self):
    return"Tasmiya"
  
class Subject:
  def study(self):
    return"Maths"
  
class aspirant:
  def study(self):
    return"MPSC"
  
  

def result(tasmii):
   print(tasmii.study())



a=Student()
b=Subject()
c=aspirant()

result(a)
result(b)
result(c)
