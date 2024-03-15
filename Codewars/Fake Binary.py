"""
Fake binary
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
Example: '27491' -> '01010'
"""


#Solution

def fake_bin(x):
    result = ''
    for digit in x:
        if int(digit) < 5:
            result += '0'
        else:
            result += '1'
    return result


#Clever solution

def fake_bin(x):
    return ''.join('0' if digit < '5' else '1' for digit in x)

# Comparing characters works because digits follow each other in order in the ASCII table.
# This uses a generator inside join(), efficiently turning each character into '0' or '1'.
# Based on this comparison, we create a string of '0's and '1's, directly from the input string.
