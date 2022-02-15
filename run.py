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
    
    play_game = input("Would you like to play Hangman:\n ")
    if play_game == "y":
        run_game()
    elif play_game == "n":
        end_game()
    else:
        print("Please enter a valid selection")

def run_game():
    """
    Will start the game if the user enters 'y' on the welcome screen.
    """
    print("Game running")

welcome_screen()

