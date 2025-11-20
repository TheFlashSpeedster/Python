# Nested Functions

def outer_fn():
  x = 1

  def inner_fn():
    y = 2
    sum = x + y
    return sum # 3 (output of inner function)
  
  return inner_fn() # 3 (output of outer function)

print(outer_fn())