"""
Data types
- String type ( str )
- Number type ( int, float, complex )
- Sequence type ( list, tupple, range )
- Mapping type ( dict )
- Set type ( set, frozenset )
- Boolean type ( bool )
- Binary type ( bytes, bytearray, memoryview )
- None type ( NoneType )
"""

# get type
a = str("Python") #string
print(type(a))

b = int(10.2)
print(type(b)) #int

c = float(12.99)
print(type(c)) # float

d = complex(2+2j)
print(type(d)) # complex

e = ['Apple', 'Banana', 'Cumin']
print(type(e)) # list

f = ('Radis', 'Cabage', 'Koly flower', 'Bean')
print(type(f)) # tuple

g = range(1, 10)
print(type(g)) #range

h = {"name":"Monzur", "age":"26"}
print(type(h)) #dict

i = {"Apple", "Cucumber", "Lemon"}
print(type(i)) #set

j = frozenset({"Apple", "Cucumber", "Lemon"})
print(type(j))

k = True
print(type(k)) #bool

l = b"Hello"
print(type(l)) #bytes

m = bytearray(10)
print(type(m)) #bytearray

n = memoryview(bytearray(5))
print(type(n))

o = None
print(type(o)) #NoneType
