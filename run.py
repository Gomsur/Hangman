# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from animals import word_list as animals_word
from country import word_list as country_word
from food import word_list as food_word

class gamesetting:
    """
    Choose game category
    """
    def __init__(self, lives, words):
        self.lives = lives
        self.hidden = ""
        if word == "animals":
            self.animals()
        else if == "country":
        self.country()
        else:
        self.food()

    def animals(self):
        """
        Gets a random word from animals.py and returns it in capitalized letters
        """
        self.word = random.choice(animals_word).upper()
        self.hidden = "_" * len(self.word)

    def food(self):
        """
        Gets a random word from food.py and returns it in capitalized letters
        """
        self.word = random.choice(food_word).upper()
        self.hidden = "_" * len(self.word)

    def country(self):
        """
        Gets a random word from country.py and returns it in capitalizede letters
        """
        self.word = random.choice(country_word).upper()
        self.hidden = "_" * len(self.word)    