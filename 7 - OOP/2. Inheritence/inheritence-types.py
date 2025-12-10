# Types of Inheritance
# 1. Single Inheritance
## Child Class Inherits from Parent Class
## Parent Class > Child Class

class Parent:
  def parent_method(self):
    print("This is Parent Class Method")
  
class Child(Parent): # Child Class Inherits Parent Class
  def child_method(self):
    super().parent_method() # Accessing Parent Class's Method
    return "This is Child Class Method"
  
data1 = Child()
print(data1.child_method()) # Accessing Child Class's Method

# 2. Multiple Inheritance
## Same Child Class Inherits from Multiple Parent Classes
## Parent Class1 + Parent Class2 > Child Class

# 3. Multilevel Inheritance
## Child Inherits from Parent, which Inherits from Grandparent Class
## Child has all the Attributes & Methods of both Parent & Grandparent Class
## Grandparent Class > Parent Class > Child Class

# 4. Hierarchical Inheritance
## Multiple Child Inherits from Same Parent Class
## Parent Class > Child Class1 + Child Class2

# 5. Hybrid Inheritance
## Combination of Two or More Types of Inheritance
## Example: Combination of Multiple & Multilevel Inheritance

