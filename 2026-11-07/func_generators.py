# Python Generator
def simple_generator():
    yield 1
    yield 2
    yield 3


for value in simple_generator():
    print(value)

print("=" * 20)
# using the next()
sample = simple_generator()
print(next(sample))
print(next(sample))
print(next(sample))
print("=" * 20)

# Generator Expressions
# List comprehension - creates a list
list_com = [x * x for x in range(7)]
print(list_com)
print("=" * 20)

# Generator expression - creates a generator
gen_exp = ( x * x for x in range(7))
print(gen_exp)
print("=" * 20)

# Generator Method( send )
def echo_gen():
    while True:
        received = yield
        print('Received', received)

gen = echo_gen()
next(gen)
gen.send('Hello')
gen.send('World')
print("=" * 20)

# Generator Method ( close)
def next_generator():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")
next_gen = next_generator()
next(next_gen)
next_gen.close()
next(next_gen)