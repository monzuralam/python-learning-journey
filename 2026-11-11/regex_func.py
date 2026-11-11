import re

txt = "Now AI Era of Development"

# findall
x = re.findall('AI', txt)
print(x)

# search
x = re.search('\s', txt)
print('search postion', x.start())

x = re.search('Era', txt)
print(x)

# Split
x = re.split('\s', txt)
print(x)

x = re.split('\s', txt, 1) # max split 1
print(x)

# sub
x = re.sub('\s', '=', txt)
print(x)