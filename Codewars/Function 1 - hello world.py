"""
Function 1 - hello world
Make a simple function called greet that returns the most-famous "hello world!".

Style Points
Sure, this is about as easy as it gets. But how clever can you be to create the most creative "hello world" you can think of? What is a "hello world" solution you would want to show your friends?
"""


#Solution

def greet():
    return "hello world!"

#Clever solution

def greet():
    return(''.join(chr(int('68656c6c6f20776f726c6421'[i:i+2], 16)) for i in range(0, 24, 2)))

# This solution decodes the "hello world!" message from hexadecimal, where '68656c6c6f20776f726c6421' is the ASCII in hex.
# By slicing every two characters, converting them to integers with base 16, and then to their ASCII counterparts using 'chr',
# it cleverly assembles the greeting. This showcases an inventive use of string manipulation, hexadecimal, and character encoding.
