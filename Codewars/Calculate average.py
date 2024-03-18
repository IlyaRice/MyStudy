"""
Calculate average
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""


#Solution

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

#Alternative solution

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# This alternative solution uses a more concise, conditional expression to handle the case of an empty list.
# The expression `sum(numbers) / len(numbers)` calculates the average as before, but it's only evaluated if `numbers` is truthy (i.e., the list is not empty).
# If `numbers` is falsy (an empty list), `0` is returned immediately.
# This approach streamlines the code by eliminating the explicit length check and directly embedding the logic into a single, readable line.
