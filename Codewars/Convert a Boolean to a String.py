"""
Convert a Boolean to a String
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.
"""


#Solution

def boolean_to_string(b):
    return str(b)

#Clever solution

boolean_to_string = str

# The clever solution leverages Python's first-class citizens feature, assigning the 'str' function to 'boolean_to_string'. 
# It elegantly simplifies the conversion of a boolean to its string representation, demonstrating efficient use of Python's built-in capabilities.
