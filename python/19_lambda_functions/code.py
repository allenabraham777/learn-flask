def add(x, y):
  return x + y

def double(x):
  return x * 2;

_add = lambda x, y: x + y

print(add(5, 3))
print(_add(10, 3))
print((lambda x, y: x + y)(12, 13))

seq = [1, 3, 5, 7, 9]
doubled = [double(x) for x in seq]
print(doubled)
doubled = list(map(double, seq))
print(doubled)
doubled = list(map(lambda x: x * 2, seq))
print(doubled)