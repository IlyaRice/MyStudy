"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]


"""


#Solution

def digitize(n):
    num_array = []
    for x in str(n):
        num_array,insert(0, int(x))
    return num_array

#Clever solution

def digitize(n):
    return [int(digit) for digit in str(n)][::-1]

# Converts the number to a string for iteration over each digit.
# The list comprehension iterates over each digit, converting them to integers.
# The slicing [::-1] reverses the list, achieving the required reverse order of digits.
