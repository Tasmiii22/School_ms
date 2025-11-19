class Vehicle():
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def display(self):
    return f"Vehicle brand is {self.brand} and model is"

class Car(Vehicle):
    def __init__(self,brand,model,price):
      super().__init__(brand,model)
      self.price=price
    def horn(self):
      return f"Brand is {self.brand} Model is {self.model} Price is {self.price} and Sound: STUTUTUTUTU...."
class bike(Vehicle):
    def __init__(self,brand,model,version):
      super().__init__(brand,model)
      self.version=version
    def start(self):
      return f"Bike ka Brand is {self.brand} Model is {self.model} and version is {self.version}"
MyCar=Car("Toyota","Supraa",8000000)
print(MyCar.horn())
MyBike=bike("TVS","IQUBE",2.0)
print(MyBike.start())
      

