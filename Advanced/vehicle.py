class vehicle:
  def __init__(self,speed,mileage):
    self.speed=speed
    self.mileage=mileage
  def motor(self):
    return f"Speed is:{self.speed} km/hr and Mileage is: {self.mileage}km/hr"
v1=vehicle(50,100)
print(v1.motor())