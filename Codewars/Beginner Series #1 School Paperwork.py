"""
Beginner Series #1 School Paperwork
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

Example:
n= 5, m=5: 25
n=-5, m=5:  0
Waiting for translations and Feedback! Thanks!
"""


#Solution

def paperwork(n, m):
    return n * m if n >= 0 and m >= 0 else 0

#Clever solution

def paperwork(n, m):
    return max(n, 0) * max(m, 0)

# The clever solution uses the max() function to ensure that both 'n' and 'm' are non-negative before multiplying them.
# By doing so, it eliminates the need for a conditional check to return 0 for negative values.
