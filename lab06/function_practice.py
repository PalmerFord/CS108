"""CS 108 - Lab 6.0

Function Practice

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

def compute_cost(miles, miles_per_gallon, dollars_per_gallon):
    """
    Calculates the cost of a trip given miles, miles_per_gallon, and dollars_per_gallon
    """
    cost = (miles / miles_per_gallon) * dollars_per_gallon
    return cost

def count_spaces(s):
    """
    Counts the number of spaces in a given string
    """
    count = 0
    for c in s:
        if c == ' ':
            count += 1
    return count
