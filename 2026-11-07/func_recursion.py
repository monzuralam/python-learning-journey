"""
Recursion function: it's called it self
"""
def countdown(n):
    if n < 1:
        print("Done")
    else:
        print(n)
        countdown(n - 1)


countdown(10)

"""
Base Case and Recursive Case
Every recursive function must have two parts:

A base case - A condition that stops the recursion
A recursive case - The function calling itself with a modified argument
"""
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


print(factorial(5))
print('='*20)

# fibonacci series 
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

for i in range(7):
    print(fibonacci(i), end = ' ')