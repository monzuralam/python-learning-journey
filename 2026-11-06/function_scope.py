# local scope
def _local_func():
    print('local scope')
    x = 10
    print(x)
_local_func()

# local scope with inside function
def _local_func_inside_func():
    print('local scope with inside function')
    x = 20
    def _inside_func():
        print("Inside func x:", x)
    _inside_func()
  
_local_func_inside_func()

# global scope
y = 100
def _global_func():
    print('global scope')
    print(y)
_global_func()

# global scope naming variable
def _global_naming_func():
    y = 200
    print('global scope naming variable')
    print(y)
_global_naming_func()
print(y)

# global keyword
def _global_keyword_func():
    print('global keyword')
    global z
    z= 150
_global_keyword_func()
print(z)

# nonlocal keyword
def _non_local_func():
    a = 'Apple'
    def _my_func():
        nonlocal a
        a = 'Ant'
    _my_func()
    return a
print(_non_local_func())

# LEGB L = local, E = Enclosing, G = Global, B = Built in
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)