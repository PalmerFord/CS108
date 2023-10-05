"""CS 108 - Lab/3.2

creates a dictionary of student scores

@author: Palmer Ford (pjf5)
@author: Heyab Robel (hr29)
@date: fall,2021
"""

score_dict = {'Joe': 10, 'Tom': 23, 'Barb': 13, 'Sue': 19, 'Sally': 12}
print(score_dict['Barb'])
score_dict['Sally'] = 13
del score_dict['Tom']
print(score_dict)