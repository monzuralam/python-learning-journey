txt = f"Hello String Formating"

print(txt)

price = 49.99
txt = f"Current, price is {price}"
print(txt)

# price formating
txt = f"current price is: {price:.2f}"
print(txt)

txt = f"current doller rate: {122:.2f}"
print(txt)

# operation on the f string
txt = f"The multipy of 10 and 5 equal {10 * 5}"
print(txt)

# perform if else operation
txt = f"the product price is {'expensive' if price > 100 else 'cheap'}"
print(txt)

# execute the functions
product = "mobile"
txt = f"Product name is {product.upper()}"
print(txt)

# string format
txt = "total amout is {}"
print(txt.format(100))

# string format using the index number
txt = "buy price: {0} & selling price: {1}"
print(txt.format(100, 120))

# string format using the name index
txt = "my favorite phone is {name} & color {color}"
print(txt.format(name = 'realme', color = 'black'))