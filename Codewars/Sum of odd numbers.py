"""
Sum of odd numbers
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""


#Solution

def row_sum_odd_numbers(n):
    return sum(range(n*(n-1)+1, n*(n+1), 2))
# This solution calculates the first odd number in the nth row with 'n*(n-1)+1' and uses a range to generate all odd numbers in that row, and sum this range after that.


#Clever solution

def row_sum_odd_numbers(n):
   return n**3

# This solution uses the insight that the sum of numbers in the nth row of this triangle is always n^3