import re
# python sets
txt = "Today is a beautiful sunny day. Today I wake up at 4.00 am, but I can't work on the morning due to the electricity"

#[arn]
x = re.findall('[arn]', txt)
print(x)

#[a-n]
x = re.findall('[a-n]', txt)
print(x)

# [^an] - except an
x = re.findall('[^an]', txt)
print(x)

# [01234]
x = re.findall('[01234]', txt)
print(x)

# [0-9] return only 0 -9
x = re.findall('[0-9]', txt)
print(x)

# [0-5][0-9] - return like 00 and 59
x = re.findall('[0-5][0-9]', txt)
print(x)

# [a-zA-Z]
x = re.findall('[a-zA-Z]', txt)
print(x)

# [+]
x = re.findall('[+]', txt)
print(x)