class ComplexNumber:
  def __init__(self, real, img):
    self.real = real
    self.img = img

  def __add__(self, other):
    return ComplexNumber(self.real + other.real, self.img + other.img)
  
c1 = ComplexNumber(1,2)
print("c1 real:", c1.real)
print("c1 img: ", c1.img)

c2 = ComplexNumber(3,4)
print("c2 real:", c2.real)
print("c2 img: ", c2.img)

result = c1 + c2
print("Result: ", result.real, result.img)