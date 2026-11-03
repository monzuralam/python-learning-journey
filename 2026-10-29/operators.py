"""
Operators
operators are perform operations on the variable and values
 
operators type
- Arithmetic operator
- Assignment operator
- Comparison operator
- Logical operator
- Identity operator
- Membership operator
- Bitwise operator
"""

"""
Arithmetic operator used to the perform basic math operations.
+
-
*
/
%
** ( exponent )
// ( flor divition, ex: 9/2 = 4)
"""
print("Arithmetic operator")
print('=' * 20)

a = 10
b = 5
c = a + b
print("a:{} b:{} a+b: {}".format(a, b, c)) # Operators is old school way
print(f"a:{a} b:{b} a+b: {c}") # modern approch
print('=' * 20)

c = a - b
print("a:{} b:{} a-b:{}".format(a, b, c)) # Operators is old school way
print(f"a:{a} b:{b} c:{c}") # modern approch
print('=' * 20)

c = a * b
print("a:{} b:{} a*b:{}".format(a, b, c)) # Operators is old school way
print(f"a:{a} b:{b} c:{c}") # modern approch
print('=' * 20)

c = a / b
print("a:{} b:{} a/b:{}".format(a, b, c)) # Operators is old school way
print(f"a:{a} b:{b} c:{c}") # modern approch
print('=' * 20)

c = a ** b
print("a:{} b:{} a**b:{}".format(a, b, c)) # Operators is old school way
print(f"a:{a} b:{b} c:{c}") # modern approch
print('=' * 20)

c = a // b
print("a:{} b:{} a//b:{}".format(a, b, c)) # Operators is old school way
print(f"a:{a} b:{b} c:{c}") # modern approch
print('=' * 20)

"""
Assignment Operator
assignment operator is used to assign value on the variable.

=
+=
-=
*=
/=
%=
**=
//=
&=
|=
^=
>>=
<<=
"""
print('=' * 20)
a += 10
print(a)
a -= 5
print(a)
a *= 8
print(a)
a /= 2
print(a)
print()

"""
Comparison operator is to compare two value

== ( Equal )
!= ( Not Equal )
> ( Greater than )
< ( Less than )
>= ( Greater than equal )
<= ( Less than equal )

"""
print('Comparison Operator')
print('=' * 20)

if(a == b):
    print(f"a is equal to the b")
else:
    print("a is not equal to the b")

if(a != b):
    print(f"a is not equal to the b")
else:
    print("a is equal to the b")

if(a > b):
    print(f"a is greater than b")
else:
    print("a less than b")

if(a < b):
    print(f"a is less than b")
else:
    print("a is not less than b")

if(a >= b):
    print(f"a is greater than equal b")
else:
    print("a not greater than equal b")

if(a <= b):
    print(f"a is less than equal b")
else:
    print("a is not less than equal b")

"""
Logical operator

and
or 
not
"""
print('=' * 20)
print('Logical operator')
print('=' * 20)
if(a > 8 and b < 6):
    print("a greater than 8 and 5 less than 6")

if( a> 10 or b == 5):
    print("a greater than 10 or b equal 5")

if( not( a > 10 and b < 5) ):
    print("DDD")

print('=' * 20)
"""
Membership operator

check on the string, tuples & list
- in
- not in
"""
print('Membership operator')
print('=' * 20)

list = [1, 5, 7, 9, 10, 12, 15, 60]

if( a in list):
    print(f"{a} found on the list")

if( c not in list ):
    print(f"{c} not found on the list")

print('=' * 20)
"""
Bitwise operator

bitwise operator perform bit by bit operation and compare binary numbers
- & ( AND )
- | ( OR )
- ^ ( XOR )
- ~ ( NOT )
- << ( zero left shift )
- >> ( zero right shift )
"""
print('Bitwise operator')
print('=' * 20)
a = int(a)
print(f"a: {a}, a: {bin(a)}, b: {b}, b: {bin(b)}")

d = a & b
print(f"Result of a AND b {bin(d)}")

e = a | b
print(f"Result of a OR b {bin(e)}")

f = a ^ b
print(f"Result of a XOR b {bin(f)}")

g = ~a
print(f"Result of a NOT {bin(g)}")

h = a << 2
print(f"a left shift 2 is {bin(h)}")

i = a >> 2
print(f"a right shift 2 is {bin(i)}")

print('=' * 20)
"""
Identity operator

Identity operator compare the memory locations of two objects

- is 
- is not
"""
print('Identity operator')
print('=' * 20)

j = [1, 2, 3, 4, 5]
k = [1, 2, 3, 4, 5]
l = j

print( j is l )
print( j is not k)

