from abc import ABC

class Animal(ABC):
  def make_sound(self):
    pass
  def move(sef):
    pass
class Dog(Animal):
  def make_sound(self):
    return f" Dog Barks"
  def move(sef):
    return "Moves on floor"
class Cat(Animal):
  def make_sound(self):
    return f"Cat Does Meow"
  def move(sef):
    return "Moves on floor"
Doggy=Dog()
print(Doggy.make_sound())
print(Doggy.move())
Cattie=Cat()
print(Cattie.make_sound())
print(Cattie.move())