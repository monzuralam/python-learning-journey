try:
    print(a)
except:
    print("Error")

print('='*20)

try:
    print("hello world")
except:
    print("Except")
else:
    print("Else")

print('='*20)

try:
    print(a)
except:
    print("Except 2x")
finally:
    print("try except is finished")

print('='*20)

try:
    file = open('demo.txt')
    try:
        file.write("3rd wold war will be loading")
    except:
        print("Error to write file")
    finally:
        print("Execution done")
except:
    print('Error to open file')

# Exception

x = -1
if x < 0:
    raise Exception("Negative number not allowed")