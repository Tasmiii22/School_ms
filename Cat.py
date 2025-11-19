#OOPS CONCEPT
class cat:

  def __init__(self,name,age):
     self.name=name
     self.age=age
  def meow(self):
    return f"{self.name} says meow"
cat1=cat("Leo",4)
print(cat1.meow())