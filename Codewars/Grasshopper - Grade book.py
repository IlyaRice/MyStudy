"""
Grasshopper - Grade book
Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""


#Solution

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'

#Clever solution

def get_grade(*s):
    return 'FFFFFFDCBAA'[sum(s)//30]

#Clever solution

def get_grade(*s):
    return 'FFFFFFDCBAA'[sum(s)//30]

# This solution uses string indexing to map summed scores to grades. By dividing the sum of scores by 30, it achieves two things simultaneously:
# it calculates the average of the scores (as if dividing by 3) and scales this average to a 0-10 range (equivalent to dividing the average by 10) for direct mapping to grades.
# The string 'FFFFFFDCBAA' is cleverly designed so that each index corresponds to a specific grade, with index 0 for 'F' up to index 10 for 'A', matching the average score ranges after division.
# This method provides a succinct and efficient way to determine grades, leveraging the linear relationship between scores and grade thresholds.
