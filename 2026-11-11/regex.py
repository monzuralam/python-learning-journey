import re

txt = 'A quick brown fox jumps over the lazy dog'
x = re.search('^A.*dog$', txt) # check start with A and end with dog

if x:
    print('Yes! we have a match')
    print(x)
else:
    print('No! 404')

"""
regex function
- findall
- search
- split
- sub

match charecters
. ^ $ * + ? {} [] \ | ()

[abc] => match any of charecters a, b or c
[a-c] => range to the charecters a-c
[a-z] => only lowercase letter
[0-9] => match only digits
. = any charecter
^ => start with
$ => ends with
* => zero or more occurance
+ => one or more occurance
? => zero or more occurance
{} => exactly the specified number of occurence
\ = signal a special sequance
| = either or
() = capture or group
"""

x = re.findall("[a-m]", txt)
print(x)

product = "I'll buy realme 8 phone. this phone is very amazing."

# find the first letter match
x = re.findall('\AI\'ll', product)
print(x)

# find the begining of the word
x = re.findall('\bbuy', product)
print(x)

# find the not begining of the word
x = re.findall('\Bis', product)
print(x)

# return digit
x = re.findall("\d", product)
print(x)

# return not digit
x = re.findall("\D", product)
print(x)

# return whitle space charecter
x = re.findall("\s", product)
print(x)

# return whitle space charecter
x = re.findall("\S", product)
print(x)

# return every charecter ( 0-9, a-z & _)
x = re.findall('\w', product)
print(x)

# return non word charecter
x = re.findall('\W', product)
print(x)

# check end with string
x = re.findall('amazing.\Z', product)
print(x)

# find on the start
x = re.findall("I..l", product)
print(x)

# find on the start
x = re.findall('^I\'ll', product)
print(x)

# find on the end
x = re.findall('amazing.$', product)
print(x)

# find zero or more occures
x = re.findall('ph.*e', product)
print(x)

# find one or more occures
x = re.findall('ph.+e', product)
print(x)

# find zero or more occures
x = re.findall('ph.?e', product)
print(x)

# either or 
x = re.findall('phone|pc', product)
print(x)

#group