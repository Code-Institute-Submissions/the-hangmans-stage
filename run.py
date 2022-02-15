import random
from words import words

def welcome_screen():
    """
    This is the home screen and will take the players username
    and welcome them to the game.
    """
    player_name = input("Please enter your username:\n ")
    print(f"Hi {player_name}, welcome to Hangman.")
    print(
        """
        The rules of the game are simple. Guessing 1 letter at a time, you have 6 lives to guess The Hangman's secret word.
        Let's see if you can escape The Hangman's stage!
        """
        )
    
    play_game = input("Would you like to play Hangman:\n ").lower()
    if play_game == "y":
        run_game()
    elif play_game == "n":
        end_game()
    else:
        print("Please enter a valid selection")

def get_word(words):
    """
    Will randomly select a word from words.py for the player to guess.
    """
    word = random.choice(words)
    return word


def run_game():
    """
    Will start the game if the user enters 'y' on the welcome screen.
    """
    word = get_word(words)
    secret = "_" * len(word)
    print(secret)
    already_guessed = []
    lives_left = 6
    guessed_letters = input("Please guess a letter: ").lower()
    if len(guessed_letters) != 1:
        print("Please enter 1 letter at a time")



welcome_screen()
