txt = 'A Quick brown fox jumps over the lazy DOG'

# startswith
print(txt.startswith('A'))

# swapcase
print(txt.swapcase())

# title 
print('today is my 3 day'.title())

# translate
text = "Py@th#on $is fun!"
dic = text.maketrans('','','@#$')
print(text.translate(dic))

# upper
print(text.upper())

# zfill
price = "10"
print(price.zfill(5))