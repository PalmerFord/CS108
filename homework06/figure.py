"""CS 108 Homework 6

This module implements a model of a square.

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

class Model:
    """ Particle models a single square that may be rendered to a canvas. """

    def __init__(self, x=50, y=50, radius=40, color="red"):
        """Instantiate a particle object."""
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, drawing):
        drawing.rectangle(self.x - self.radius,
             self.y - self.radius,
             self.x + self.radius,
             self.y + self.radius,
             outline=True,
             color=self.color
             )
