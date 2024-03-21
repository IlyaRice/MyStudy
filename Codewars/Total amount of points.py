"""
Total amount of points
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""


#Solution

def points(games):
    result = 0
    for scores in games:
        if scores[0] > scores[2]:
            result += 3
        #It is unneccessary to do anything in case of loosing score
        elif scores[0] == scores[2]:
            result += 1
    return result

#Clever solution

def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))

# This clever solution employs a compact and efficient approach by using list comprehension combined with tuple unpacking and conditional logic directly within the sum function.
# First, each match result string 's' in the list 'a' is split at ":", creating tuples of (x, y) representing our team's score and the opponent's score, respectively.
# Then, for each tuple, it calculates the points awarded using a succinct expression: (x >= y) + 2 * (x > y). This exploits the fact that boolean values can be treated as integers (True as 1 and False as 0) in Python.
# If our team wins (x > y), the expression evaluates to 3 (since True is 1, and 2*True is 2, summing up to 3).
# If it's a draw (x == y), only the first part of the expression contributes, resulting in 1 point (since x >= y is True but x > y is False).
# In case of a loss (x < y), both conditions are False, resulting in 0 points.
