"""CS 108 - Homework 5.0

Module containing the BarGraph class.

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

class BarGraph:
    """Represents a BarGraph object."""
    
    def __init__(self, data, color='blue'):
        """Instantiate a new BarGraph object, color defaulting to blue."""
        self.data = data
        self.color = color
        
    def __str__(self):
        """Create a BarGraph string with a simple format."""
        return 'Bar Graph - Color: ' + self.color + ' Data: ' + str(self.data)

    def draw(self, drawing):
        """draws a bar graph given a GuiZero canvas."""
        hight = drawing.master.height / len(self.data)
        for i in range(len(self.data)):
            drawing.rectangle(0, i * hight, (self.data[i] / max(self.data)) * drawing.master.width, (i * hight) + hight, color=self.color, outline=True, outline_color="black")
            
            