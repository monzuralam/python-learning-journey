i = 1
while( i <= 9 ):
    print(i)

    if( i == 6 ):
        break
    
    i += 1

while( i > 6 ):
    print(i)
    i += 1
else:
    print('oops')

# count 10 number value
i = 0
sum = 0
while( i <= 10 ):
    sum += i
    i += 1

print(f"total sum value is: {sum}")
