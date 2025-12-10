# Polymorphism
## Allows objects of different classes to be treated as objects of a common superclass.

class Animal:
  def sound(self):
    pass
  
class Dog(Animal):
  def sound(self):
    print("Bark")

class Cat(Animal):
  def sound(self):
    print("Meow")

class Bird(Animal):
  def sound(self):
    print("Chirp")

dog = Dog()
cat = Cat()
bird = Bird()

dog.sound()
cat.sound()
bird.sound()