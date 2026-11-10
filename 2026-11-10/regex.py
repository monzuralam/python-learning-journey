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

product = "I'll buy realme 8 phone"
x = re.findall("\d", product)
print(x)

# find on the start
x = re.findall("I..l", product)
print(x)

# find on the start
x = re.findall('^I\'ll', product)
print(x)

# find on the end
x = re.findall('phone$', product)
print(x)