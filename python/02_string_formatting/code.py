#F string
name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

#Template string

name = "Rob"
greet = "Hey, {}"
with_name = greet.format(name)

print(with_name)