"""CS 108 - Lab 9.1

Fraction Class              

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

import math


class Fraction:
    
    def __init__(self, numerator, denominator):
        """Constructs a Fraction instance with the given attributes"""
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
        
    def __str__(self):
        """Returns a printable representation of this Fraction item"""
        return (
            '{}'.format(self.numerator)
            + '/'
            + '{}'.format(self.denominator)
            )
    
    def is_valid(self):
        """Returns a true or false depending on if the Fraction item is valid"""
        if self.denominator == 0:
            return False
        return True
    
    def get_decimal_value(self):
        """Returns the floating point value of the Fraction item"""
        decimal = self.numerator / self.denominator
        return decimal
    
    def simplify(self):
        """simplifies the Fraction item"""
        gcd = math.gcd(self.numerator, self.denominator)
        if gcd != 0:
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd
        if self.denominator < 0:
            self.numerator = self.numerator * -1
            self.denominator = self.denominator * -1

    def __mul__(self, other):
        """Multiplies the Fraction item with a different Fraction item and returns a third Fraction item"""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    
f1 = Fraction(3, 6)
f2 = Fraction(2, 7)

print(f1)