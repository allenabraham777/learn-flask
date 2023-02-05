a = [1, 2, 3]
b = a

a.append(4)

print("a: ", id(a))
print("b: ", id(b))

print("a: ", a)
print("b: ", b)

c = []
d = []

c.append(4)

print("c: ", id(c))
print("d: ", id(d))

print("c: ", c)
print("d: ", d)
