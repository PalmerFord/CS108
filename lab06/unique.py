"""CS 108 - Lab 6.2

Unique

@author: Palmer Ford (pjf5)
@author: Heyab Robel (hr29)
@date: fall, 2021
"""
def search(str_list, target):
    """
    Searches a list of strings for a target string and returns the index value of the first matching string
    If so matches are found, the function returns -1
    """
    for i in range(len(str_list)):
        if str_list[i] == target:
            return i
    return -1

def get_unique_words(str_list):
    """
    Returns a list of all unique strings in a given list of strings
    """
    unique_words = []
    for i in str_list:
        if search(unique_words, i) == -1:
            unique_words.append(i)
    return unique_words