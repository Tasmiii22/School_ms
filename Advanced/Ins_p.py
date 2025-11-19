class person:
  behv="Human"
  def __init__(self,name):
    self.name=name
  def greet(self):
    return f"Name of a persson is {self.name} and behaviour is {person.behv}"
man=person("Tasmiii")
print(man.greet())

    