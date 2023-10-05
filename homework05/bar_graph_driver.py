"""CS 108 - Homework 5.0

Draws a bar graph given a text file.

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

import random
from guizero import App, Drawing
from bar_graph import BarGraph

app = App('Drawing Canvas', bg="white")

drawing = Drawing(app, width='fill', height='fill')


def get_data(filename):
    """Collects data from a text file"""
    file = open(filename)
    data = []
    for i in file.readlines():
        data.append(int(i))
    file.close()
    return data
    
def get_random_color():
    """Returns a random color."""
    color = random.choice(['#ffffd9','#edf8b1','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8','#253494','#081d58'])
    return color

bg = BarGraph(get_data(input("Filename: ")), 'blue')
bg.draw(drawing)  


app.display()