import camelcase

text = "hello world pip"

c = camelcase.CamelCase()

print(c.hump(text))


# install any package via: pip install camelcase
# uninstall any package via: pip uninstall camelcase
# see all package: pip list