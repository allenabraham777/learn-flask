def add(x, y):
  return x + y

def divide(dividend, divisor):
  if divisor != 0:
    return dividend / divisor
  else:
    return "Infinity!"

result = add(5, 8)
print(result)
print(add(10, 20))
print(divide(10, 20))
print(divide(10, 0))