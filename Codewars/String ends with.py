"""
String ends with?
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


#Solution

def solution(text, ending):
    return text.endswith(ending)

#Clever solution

def solution(string, ending):
    return ending in string[-len(ending):]

# This solution manually slices the string from the end by the length of the ending string and checks if it matches the ending.
# It effectively replicates the behavior of .endswith() method, providing a direct, albeit less intuitive, approach to string comparison.
