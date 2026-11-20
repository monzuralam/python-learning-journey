a = {"Apple", "Banana", "Cucumber"}
b = set(("Chicken", "Mutton", "Beef"))

# length
print(len(a))

# type
print(type(b))

print(a)

# Add item
b.add("Rice")
print(b)

# add items
a.update(b)
print(a)

# remove item
a.remove("Mutton")
a.discard("Banana")
print(a)

# join
c = a.union(b)
print(c)

a.update({"Lentil"})
print(a)

d = a.intersection(c)
print(d)

e = a.difference(d)
print(e)

f = a.symmetric_difference(d)
print(f)

# frozen set
g = frozenset({"white", "black", "red"})
print(g)
print(len(g))
print(type(g))
