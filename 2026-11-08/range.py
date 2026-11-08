# range 
days = range(5)
print(days)
for day in days:
    print(day)
print('='*20)

# Week
weeks = range(0, 7) # start & end days
print(weeks)
for day in weeks:
    print(day)
print('='*20)

x = range(1, 10, 3) # start, end & increment
print(x)
for item in x:
    print(item)
print('='*20)

# list on the range
roll = list(range(1, 10))
print(roll)

# membership testing
print( 9 in roll) # True

# length
print(len(roll))