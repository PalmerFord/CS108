"""CS 108 - Lab 6.1

Searches a list of strings for a given word

@author: Palmer Ford (pjf5)
@author: Heyab Robel (hr29)
@date: fall, 2021
"""

def search(str_list, target):
    for i in range(len(str_list)):
        if str_list[i] == target:
            return i
    return -1
