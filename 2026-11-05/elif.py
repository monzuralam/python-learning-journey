a = 28
b = 28
if( a > b ):
    print(f"{a} is greater than {b}")
elif( a == b ):
    print(f"{a} is equal to the {b}")

marks = 75
if( marks >= 80 ):
    print("A+")
elif( marks >= 70 and marks <= 79):
    print("A")
elif( marks >= 60 and marks <= 69):
    print("A-")
else:
    print("F")