my_tuple = ('Apple', 'Banana', 'Mango')
my_iter = iter(my_tuple)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print('='*20)

# we can dot the same thing as for loop
for i in my_tuple:
    print(i)
print('='*20)

# numbers handle with stopIteration
numbers = [10, 20, 30]
iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        break
print('='*20)

# Create a iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

my_numbers = MyNumbers()
my_iter = iter(my_numbers)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print('='*20)

# Create a iterator with StopIteration
class AnotherClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        if x <= 5:
            self.a += 1
            return x
        else:
            raise StopIteration

another_class = AnotherClass()
another_iter = iter(another_class)

for item in another_iter:
    print(item)