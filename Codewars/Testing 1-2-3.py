"""
Testing 1-2-3
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
"""


#Solution

def number(lines):
    return[f"{i}: {line}" for i, line in enumerate(lines, start=1)]

#Clever solution

def number(lines):
    return['%d: %s' % v for v in enumerate(lines, 1)]

#Uses the `%` string formatting operator to prepend line numbers, utilizing `enumerate` with a start index of 1 to generate line numbers alongside the original lines.