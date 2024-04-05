"""
Binary Addition
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""


#Solution

def add_binary(a,b):
    return format(a+b, 'b')

#Alternative solution

def add_binary(a,b):
    return bin(a+b)[2:]

# The alternative solution uses the bin() function to convert the sum of 'a' and 'b' to its binary representation.
# The [2:] slicing removes the '0b' prefix that bin() adds to the start of its return value, leaving only the binary digits.