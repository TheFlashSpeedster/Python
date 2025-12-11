"""
Q10. Polymorphism using Common Interface (High) 
Classes Cat and Dog each having speak() method. Write function that calls speak() for any animal object.
"""

class Cat:
  def speak(self):
    print("Meow!")

class Dog:
  def speak(self):
    print("Woof!")

# function to call speak function
def animal_sound(animal):
  animal.speak()

# object for cat sound
cat = Cat()
animal_sound(cat)

# object for dog sound
dog = Dog()
animal_sound(dog)