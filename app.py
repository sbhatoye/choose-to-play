x = "Hello"
y = "World"
def check_scope():
  global y
  global z
  y = 42
  z = 100
  print(f"Inside function, x: {x}, y: {y}")

print(f"Before function, x: {x}, y: {y} ")

check_scope()
print(f"After function, x: {x}, y: {y}, z: {z} ")


