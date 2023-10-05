"""CS 108 - Lab 5.1

Convert to binary

@author: Palmer Ford (pjf5)
@author: Heyab Robel (hr29)
@date: fall, 2021
"""

x = int(input('integer: '))

while x > 0:
    print(x % 2, end ='')
    x = x // 2
print()