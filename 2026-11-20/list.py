a = [10, 'Mango', 'Banana', 'Apple', True]
b = list(('Plam', 'Orange', 'Cherry'))

print(b)
print(len(a))

# add item
a.insert(1, 'Lichu')
a.append('Date')
a.extend(b)

# remove item
a.remove(True)
a.pop(0)

print(a)

# sort
a.sort()
# a.sort(key = str.lower)
# def myfunc(n):
#     return abs(n - 50)
# a.sort(key = myfunc)
print(a)

a.sort(reverse=True)
print(a)

a.reverse()
print(a)

# copy
c = b.copy()
print(c)

# copy using the list
d = list(a)
print(d)

# copy using the slice
e = a[:]
print(e)

# join list
f = d + b
print(f)