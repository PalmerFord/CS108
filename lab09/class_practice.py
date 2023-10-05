"""CS 108 - Lab 9.0

This module implements a simple food item class with nutritional information.

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""


class FoodItem:

    def __init__(self, name, fat, carbohydrates, protein):
        """Constructs a FoodItem instance with the given attributes"""
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def __str__(self):
        """Returns a printable representation of this food item"""
        return (
            self.name
            + "\n\tFat: {:.2f} g".format(self.fat)
            + "\n\tCarbohydrates: {:.2f} g".format(self.carbohydrates)
            + "\n\tProtein: {:.2f} g".format(self.protein)
        )

    def get_calories(self, num_servings):
        """Returns the number of calories for the given number of servings of
        this food item
        """
        return num_servings * (
            (self.fat * 9) + (self.carbohydrates * 4) + (self.protein * 4)
        )

# Creates a FoodItem object for M&Ms and prints its values and calories per serving
MandM = FoodItem('M&Ms', 10.00, 34.00, 2.00)
print(MandM)
print('Calories per serving:',MandM.get_calories(1.0))
print()

# Creates a FoodItem object for water and prints its values and calories per serving
water = FoodItem('Water', 0.00, 0.00, 0.00)
print(water)
print('Calories per 10 servings:',water.get_calories(10.0))





