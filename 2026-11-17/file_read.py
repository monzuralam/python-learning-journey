# file open & read
f = open('sample.txt')
print(f.read())
f.close()
print('-'*30)

# with method file open and read
with open('sample.txt') as file:
    print(file.read())
    print('-'*30)

# readline
with open('demo.txt', 'r', encoding='utf-8') as f1:
    print(f1.readline())
    print('-'*30)
    print(f1.readline())
    print('-'*30)
    print(f1.readline())
    print('-'*30)

# readline by for loop
with open('demo.txt', 'r', encoding='utf-8') as f2:
    for x in f2:
        print(x)
        print('+'*30)