"""CS 108 - Lab 3.1

creates user id

@author: Palmer Ford (pjf5)
@author: Hayab Robel (hr29)
@date: fall, 2021
"""

first_name = input('First name: ')
last_name = input('Last name: ')
student_id = input('Student ID: ')
login = first_name[0] + last_name + student_id[0] + student_id[1]
login = login.lower()
print('User ID:', login)