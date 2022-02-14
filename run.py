import random
from words import words

def welcome_screen():
    """
    This is the home screen and will take the players username
    and welcome them to the game.
    """
    player_name = input("Please enter your username:\n ")
    print(f"Hi {player_name}, welcome to The Hangman's stage. Please try to guess what The Hangman's word is and see if you can escape him")

welcome_screen()