"""
Returning Strings
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]
"""


#Solution

def greet(name):
    return f"Hello, {name} how are you doing today?"

#Alternative solution

def greet(name):
    return "Hello, {} how are you doing today?".format(name)

# While the .format() method is valid and provides a versatile approach to string formatting, 
# its use is becoming less common in favor of f-strings, introduced in Python 3.6. 
# F-strings offer a more readable and concise syntax for embedding expressions inside string literals. 
# The .format() method, however, remains a powerful tool for more complex cases where direct expression embedding is insufficient or for maintaining code compatible with Python versions older than 3.6.
