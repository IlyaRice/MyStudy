"""
Grasshopper - Check for factor
This function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not.

About factors
Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: 2 * 3 = 6

You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
You can use the mod operator (%) in most languages to check for a remainder
For example 2 is not a factor of 7 because: 7 % 2 = 1

Note: base is a non-negative number, factor is a positive number.
"""


#Solution

def check_for_factor(base, factor):
    return base % factor == 0

# Alternative solution

def check_for_factor_alt(base, factor):
    return int(base / factor) == base / factor

# This alternative approach divides 'base' by 'factor' and checks if the result is an integer by comparing it to its integer cast.
# The idea is that if 'base' divided by 'factor' gives a whole number, then 'factor' is indeed a factor of 'base'.
# However, this method is less efficient and less intuitive than using the modulus operator (%) to check for no remainder.
# The use of division and comparison introduces unnecessary complexity and potential for floating-point arithmetic errors.
