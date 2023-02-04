def named(**kwargs):
  print(kwargs)

named(name = "Bob", age =25)

def named1(name, age):
  print(name, age)

details = {"name": "Bob", "age": 25}

named1(**details)

def print_nicely(**kwargs):
  named(**kwargs)
  for arg, value in kwargs.items():
    print(f"{arg}: {value}")

print_nicely(name = "Bob", age = 25)

def both(*args, **kwargs):
  print("ARGS", args)
  print("KWARGS", kwargs)

both(1, 2, 3, 4, 5, name = "Bob", age = 25)