fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for fruit in fruits:
    if 'a' in fruit:
        new_list.append(fruit)

print(new_list)

# shortcut in one line
update_list = [x for x in fruits if "e" in x]
print(update_list)

# we can use also iterable range
num_list = [x for x in range(10) if x % 2 == 0]
print(num_list)