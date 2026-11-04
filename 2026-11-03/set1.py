# set
set_items = {"apple", "banana", "chery", "coconut", "guava", "mango", "orange", "pineapple"}
new_items = {"apple", "banana", "mango", "peer"}

print(set_items)
print(len(set_items))
print(type(set_items))

# you can create set by set constructor also
another_items = set(("banana", "guava", "mango"))
print(another_items)

# access set itme
for x in another_items:
    print(x)

print('='*30)

# add items
set_items.add('next')
print(set_items)

set_items.update(new_items)
print(set_items)

# remove items by discard, remove
set_items.remove('banana')
print(set_items)

set_items.discard('next')
print(set_items)

# clear itemms
next_items = set(set_items)
next_items.clear()
print(next_items)

# delete set
del next_items

# frozen set
fro_set = frozenset({"next", "level", "python", "development"})
print(fro_set)
print(type(fro_set))

print('='*20)

# join sets
a = {"apple", "banana", "chery"}
b = {"banana", "guava"}

c = a.union(b) # union 
print(c)

d = a | b | set_items # shortcut of union
print(d)

e = a.intersection(b) # intersection
print(e)

f = a & b
print(f) # same as prev intersection

g = a.difference(b) # difference
print(g)

h = a - b # difference shortcut
print(h)

i = a.symmetric_difference(b) # symannantic difference
print(i)

j = a ^ b
print(j)