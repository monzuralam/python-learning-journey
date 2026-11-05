a = 10
b = 8
c = 5

if( a > b and a > c ):
    print("A Winner")

if( a < b or b > c):
    print("B Winner")

if( not c > a ):
    print("C Winner")

age = 20
is_student = True
is_discount = False

if( ( age >= 18 and age <= 65) and is_student and not is_discount ):
    print("Elligible for discount")