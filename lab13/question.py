""" Lab 13.1

This module implements a model of a variety of quiz question types.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@author: YOUR-NAME (yourid123)
@author: PARTNER-NAME (theirid123)
@date: semester, year
"""

class Question:
    def __init__(self, question):
        """Initializes a question object."""
        self.text = question    

class ShortAnswer:
    """This class implements a short-answer question with a string answer."""

    def __init__(self, question, answer):
        """Initializes a short-answer question object."""
        
        self.answer = answer

    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '?'

    def check_answer(self, answer):
        """Checks the correctness of the given answer (a string)"""
        return self.answer.lower() == answer.lower()

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return self.answer
