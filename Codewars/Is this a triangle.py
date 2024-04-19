"""
Is this a triangle?

Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

Examples:

Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false 
"""


#Solution

def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

#Clever solution

def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

# This clever solution first sorts the sides, ensuring `a` and `b` are the two smallest. It then checks if their sum exceeds `c`, 
# which is a simplified version of the triangle inequality theorem applicable when sorted smallest to largest.