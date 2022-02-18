import random
from words import superheroes, words, cartoons

def welcome_screen():
    """
    This is the home screen and will take the players username
    and welcome them to the game.
    """
    #player_name = input("Please enter your username:\n ")
    #print(f"Hi {player_name}, welcome to Hangman.")
    print(
        """
        The rules of the game are simple. Guessing 1 letter at a time,
        you have 6 lives to guess The Hangman's secret word.
        Let's see if you can escape The Hangman's stage!
        """
        )
    while True:
        play_game = input("Would you like to play Hangman? Enter 'y' for yes and 'n' for no: \n ").lower()
        if play_game == "y":
            get_theme()
        elif play_game == "n":
            end_game()
        else:
            print("Please enter a valid selection")

def end_game():
    print("Thank you for playing Hangman")
    welcome_screen()

def continue_game():
    print("Would you like to continue playing?")
    print("y - Continue playing")
    print("n - Exit Game")
    replay = input(" \n").lower()
    if replay == "y":
        get_theme()
    elif replay == "n":
        end_game()
    else:
        print("Please enter a valid selection")

def get_theme():
    #player_name = input("Please enter your username:\n ")
    print(f"Hi, welcome to Hangman.")
    while True:
        print("Please choose a theme of secret words")
        print("1 - Superheroes")
        print("2 - Cartoons")
        print("3 - anything goes")
        theme = input(" \n")
        if theme == "1":
            word = random.choice(superheroes)
            run_game(word)
        elif theme == "2":
            word = random.choice(cartoons)
            run_game(word)
        elif theme == "3":
            word = random.choice(word)
            run_game(word)
        else:
            print("Please choose a valid theme")

def run_game(word):
    """
    Will start the game if the user enters 'y' on the welcome screen.
    """
    secret = "_" * len(word)
    print(f" guess the word: {secret}")
    print(word)
    already_guessed = []
    lives_left = 6
    while lives_left > 0:
        word_list = [letter if letter in already_guessed else '_' for letter in word]
        if "_" not in word_list:
            print("You have failed to escape The Hangman")
            print(f"The Hangman's secret word was '{word}'")
            continue_game()
        print(word_list)
        print('Current word: ', ' '.join(word_list))
        guessed_letter = input("Please guess a letter: ").lower()
        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            if guessed_letter in already_guessed:
                print("You have already guessed that letter")
                print(f"Used letters: {already_guessed}")
                already_guessed.append(guessed_letter)
            elif guessed_letter not in word:
                print(f"Sorry, {guessed_letter} is not in the secret word.")
                already_guessed.append(guessed_letter)
                lives_left -= 1
                print(f"You have {lives_left} lives left")
            else:
                already_guessed.append(guessed_letter)
                print(f"Congrats, {guessed_letter} is in the secret word")
        elif len(guessed_letter) != 1:
            print("Please enter 1 letter at a time")
        else:
            print("You entered an invalid character!")
    #if "_" not in word_list:
    #    print("You have failed to escape The Hangman")
    #    print(f"The Hangman's secret word was '{word}'")
    #else:
    #    print(f"Well done, you guessed {word} was The Hangman's secret word and managed to escape")
        
        

welcome_screen()
