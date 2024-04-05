"""
Convert a string to an array
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""


#Solution

def string_to_array(s):
    return s.split(' ')

#Clever solution

def string_to_array(s):
    return s.split()

# Uses the default behavior of the split() method without specifying a delimiter, which splits the string by any whitespace.