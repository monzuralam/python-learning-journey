# Tople is unchangeble, unordered data
new_list = ('apple', 'banana', 'pineapple')

# print tuple
print(new_list)

# access tuple
print(new_list[2]) # index
print(new_list[0:2]) # range
print(new_list[-3]) # negative index

if( 'banana' in new_list ):
    print("🍌 banana is stock")

# update tuple
update_list = list(new_list)
update_list[2] = 'mango'
new_list = tuple(update_list)
print(new_list)

old_list = ('chery', 'nut')
mix_list = new_list + old_list # tuple + tuple
print(mix_list)

update_list.append('lichu') # direct append doesn't work, you need to convert list then append
update_list.append('lemon')
new_list = tuple(update_list)
print(new_list)

update_list.remove('lemon') # direct remove doesn't work tuple, you need to convert list then remove
new_list = tuple(update_list)
print(new_list)

# delete tuple value
#del new_list
print(new_list)

#unpack tuple
apple, banana, *other = new_list
print(apple)
print(banana)
print(other)
print('-'*20)

# loop
for x in new_list:
    print(x)

print('-'*20)

for i in range(len(new_list)):
    print(new_list[i])

print('-'*20)

i = 0
while i < len(new_list):
    print(new_list[i])
    i += 1

print('-'*20)

# join tuple
v2 = ('rice', 'lentil')
join_list = new_list + v2
print(join_list)