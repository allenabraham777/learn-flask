l = ["Bob", "Mary", "Jane"]
t = ("Bob", "Mary", "Jane") # Immutable
s = {"Bob", "Mary", "Jane"} # No duplicate values and no order is maintained

print(l[0])
print(t[2])
# no subsript to sets


l[0] = "Rob"
# t[0] = "Peter" // Not allowed
# cannot do on sets

l.append("Smith")
print(l)
# cannot append to tuples
s.add("Smith")
s.add("Smith") # Ingnored as values are unique
print(s)

l.remove("Rob")
print(l)
# Cannot remove in tuple
s.remove("Bob")
print(s)
