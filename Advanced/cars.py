class cars:
  def __init__(self,name,engine):
    self.name=name
    self.engine=engine
  def car(self):
    return f"Name: {self.name} Engine: {self.engine}"
c1=cars("Supra MK4","V10")
print(c1.car())