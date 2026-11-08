# module is a code library you can use it on your application

import greating

# module alias
# import greating as gt

print(greating.hello("Monzur"))

# access module variable
print(greating.foods)
print(greating.foods["breakfast"])

# built in module
import platform

# os
print(platform.system())

# dir
x = dir(platform)
print(x)
print('='*20)

# import specific item
from person import info

print(info())