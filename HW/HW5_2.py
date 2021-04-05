


#TODO: Add a try-except block to the following function that protects the
# "result = x + y" line from throwing errors. If ANY exception is caught on that line
# This function should return x
def add_except(x, y):

  result = x + y
  
  return result

# TODO: Add two assert statements before the "result = x + y" line in the following
# function. These assert statments should check that the x and y inputs are ints
# The built-in python function isinstance(x, int) will return True is x is an int
def add_assert(x,y):

  result = x + y
  return result

# TODO: Add a try-except block to the following function that ONLY excepts AssertionError
# If an AssertionError is accepted, set result to None and return it. Otherwise, return
# the result of the call to the "add_assert" function
def add_assert_except(x,y):

  result = add_assert(x,y)

  return result

# TODO: What is the difference between the three above functions? Please answer the following
# Questions for each function:

# How does each function react to two integer arguments? (For example, x=1, y=2)
# Possible responses include: returns the sum, throws an error, returns None, etc.

# How does each function react to two float arguments? (For example, x=1.5, y=2.5)

# How does each function react to two string arguments? (For example, x="Hello", y="World")

# How does each function react to two boolean arguments? (For example, x=True, y=False)