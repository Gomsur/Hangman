import random
from animals import word_list as animals_word
from country import word_list as country_word
from food import word_list as food_word


class text_colors:
    """
    adds different color to wining and end screen and intro.
    """
    BLUE = '\033[38;5;159m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'


class game_setting:
    """
    Choose game category
    """
    def __init__(self, lives, words):
        self.lives = lives
        self.hidden = ""
        if word == "animals":
            self.animals()
        elif word == "country":
            self.country()
        else:
            self.food()

    def animals(self):
        """
        Gets a random word from animals.py and returns it capitalized
        """
        self.word = random.choice(animals_word).upper()
        self.hidden = "_" * len(self.word)

    def food(self):
        """
        Gets a random word from food.py and returns it capitalized
        """
        self.word = random.choice(food_word).upper()
        self.hidden = "_" * len(self.word)

    def country(self):
        """
        Gets a random word from country.py and returns it capitalizede
        """
        self.word = random.choice(country_word).upper()
        self.hidden = "_" * len(self.word)


def intro_logo():
    """
    Intro logo shows up when you start the game
    """
    print(
        text_colors.BLUE
        + """ Welcome to
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/
"""
        + text_colors.WHITE
    )


def play(game_setting):
    """
    Display a word for each turn, this will continue to run until the user
    guesses the correct word or runs out of lives.
    """
    word_completion = game_setting.hidden
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8

    print(game_setting.word)

    print(display_hangman(tries))
    print(word_completion)
    print(" \n ")
    while not guessed and tries > 0:
        guess = input("Please guess a letter").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Sorry, you have already guessed that letter.", guess)
            elif guess not in game_setting.word:
                print(guess, "Incorrect, try again!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well done!", guess, "is correct")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(game_setting.word)
                    if letter == guess
                ]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(gma_setting.word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed this", guess)
            elif guess != game_settings.word:
                print(guess, "That is not correct.")
                tries -= 1
                guessed_words.append(guess)
        elif len(guess) != len(game_setting.word):
            print("That is not the correct amount of letters")
        else:
            guessed = True
            word_completion = game_setting.word

        print("Nope! Please enter a letter!")
        print(display_hangman(tries))
        print(word_completion)
        print(f"There is {len(game_setting.word)} letters in this word")
        print("\n")
    if guessed:
        win_game()
    else:
        print(
            "Sorry, no more tries! The correct word were "
            + game_setting.word
            + "\n You will get it next time!"
        )
        lose_game()


def display_hangman(tries):
    """
    Display Hangman figures depending on lives.
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                    --------
                    |      |
                    |      O
                    |     \|/
                    |      |
                    |     / \.
                    - """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
                # head, neck and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head and neck
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # rope added
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |
                   |
                   |
                   |
                   |
                   -
                """,
    ]
    return stages[tries]


def win_game():
    """
    Displays when the user completes the game
    """
    print(
        text.colors.BLUE
        + """ Congratulations, you completed the game!
   _____                            _         _       _   _                 _
  / ____|                          | |       | |     | | (_)               | |
 | |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___| |
 | |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
 | |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
  \_____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                     __/ |
 __     __          |___/                                        _
 \ \   / /          | |                                         | |
  \ \_/ /__  _   _  | |__   __ ___   _____  __      _____  _ __ | |
   \   / _ \| | | | | '_ \ / _` \ \ / / _ \ \ \ /\ / / _ \| '_ \| |
    | | (_) | |_| | | | | | (_| |\ V /  __/  \ V  V / (_) | | | |_|
    |_|\___/ \__,_| |_| |_|\__,_| \_/ \___|   \_/\_/ \___/|_| |_(_)
    """
        + text_colors.WHITE
    )


def lose_game():
    """
    Displays the the user loses the game
    """
    print(
        text_colors.WHITE
        + """
 __     __           _
 \ \   / /          | |
  \ \_/ /__  _   _  | | ___  ___  ___
   \   / _ \| | | | | |/ _ \/ __|/ _ \
    | | (_) | |_| | | | (_) \__ \  __/
    |_|\___/ \__,_| |_|\___/|___/\___|
    """
        + text_colors.WHITE
    )


def select_difficulty():
    """ Selects the word that you want to play """

    difficulty_selected = False
    while difficulty_selected is False:
        difficulty = input(
            """ Please select a word type """
        ).upper()
        if difficulty == "E":
            print("You have chosen animals. You have ", tries, "tries.")
            difficulty_selected = True
            player = game_setting("animals")
            return player
        elif difficulty == "M":
                print("You chose countries. You have", tries, "tries")
                difficulty_selected = True
                player = game_setting("country")
                return player
        elif difficulty == "H":
            print("You chose food. You have", tries, "tries")
            diffuclty_selected = True
            player = game_setting("food")
            return player
        else:
            print(difficulty, "is not a category")


def main():
    """ Whenever you win, lose or start the game.
    This setting resets and starts the game """

    intro_logo()
    game_instance = select_difficulty()

    print(game_instance.lives, game_instance.hidden)
    play(game_instance)
    while (
        input("Play again? 'Y' for YES \ any other letter for NO").upper()
        == "Y"
    ):
        game_instance = select_difficulty()
        play(game_instance)


if __name__ == "__main__":
    main()
