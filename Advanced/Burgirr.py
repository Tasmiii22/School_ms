class Burger:
  def __init__(self,radius,toppings):
    self.radius=radius
    self.toppings=toppings
  @classmethod
  def MacEgg(cls,radius):
    return cls(radius,["Bun","tikki","Mayonise"])
  
  @classmethod
  def Burgir(cls,radius):
    return cls(radius,["Bun","chicken_tikki","Mayonise"])

b1=Burger.MacEgg(4)
print(b1.radius,b1.toppings)

b2=Burger.Burgir(5)
print(b2.radius,b2.toppings)


  

                            