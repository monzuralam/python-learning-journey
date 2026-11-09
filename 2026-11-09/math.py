# built in math functions ( min, max, abs, pow )
print("min", min(5, 10, 25), "max", max(5, 10, 25))

# abs number
print('abs', abs(-7.25))

# power
print('power', pow(4, 3))

# math module
import math

# sqrt
print("sqrt", math.sqrt(64))

# floor & ceil
print("floor", math.floor(3.2), "ceil", math.ceil(3.9))

# pi
print("PI", math.pi)

# e ( euler's number )
print("e", math.e)

# tau (pi*2)
print('tau', math.tau)

# inf (infinity)
print('inf', math.inf)

# nan (Not a Number)
print('nan', math.nan)

# ex: circle area, A = pi r^2
print('Circle area', math.pi * math.pow(5, 2))

# factorial
print(math.factorial(5))

# GCD (Greatest common divisor), LCM (least common module)
print(math.gcd(12, 18))
print(math.lcm(12, 18))

# Round
print('Round', round(4.5))

# Trunc
print('Trunc', math.trunc(-12.33))

# Sum
print('Sum', sum([12, 33, 55]))

# Product
print('Product', math.prod([11, 22, 33]))

# Modf
print('Modf', math.modf(12.75))

# isclose
print('lsclose', math.isclose(.3, 0.3))

# Sin
print('Sin', math.sin(math.radians(30)))

# cos
print('cos', math.cos(math.radians(60)))

# tan
print('tan', math.tan(math.radians(90)))

# on the python degree convert to the radians while calculation
# degree to radians
print('deg -> rad:', math.radians(90))
print('rad -> deg:', math.degrees(1.5707963267948966))

# log
print('log', math.log(10))

# log10
print('log10', math.log10(10))

# log2
print('log2', math.log2(100))

# log1p
print('log1p', math.log1p(3.33))

# number thery functions
# isfinite
print('is finite', math.isfinite(100))

# isinf
print('is inf', math.isinf(math.inf))

# isnan
print('is nan', math.isnan(math.nan))

# calc remainder
print('is remainder', math.remainder(10,3))

# hypot (ex: sqrt( pow(a, 2) + pow(b, 2)))
print('hypotenuse', math.hypot(3, 4))