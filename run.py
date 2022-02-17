import random
from words import words, superheroes, cartoons

def welcome_screen():
    """
    This is the home screen and will take the players username
    and welcome them to the game.
    """
    #player_name = input("Please enter your username:\n ")
    #print(f"Hi {player_name}, welcome to Hangman.")
    print(
        """
        
  _______ _            _    _                                         
 |__   __| |          | |  | |                                        
    | |  | |__   ___  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | |  | '_ \ / _ \ |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | | |  __/ | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_| |_|\___| |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                           __/ |                      
                                          |___/                       

        """        
    )
    print(
        """
        The rules of the game are simple. Guessing 1 letter at a time,
        you have 6 lives to guess The Hangman's secret word.
        Let's see if you can escape The Hangman's stage!
        """
        )
    while True:
        play_game = input(
            "Would you like to play Hangman? Enter 'y' for yes and 'n' for no: \n "
        ).lower()
        if play_game == "y":
            run_game()
        elif play_game == "n":
            end_game()
        else:
            print("Please enter a valid selection")

def get_word(choice):
    """
    Will randomly select a word from words.py for the player to guess.
    """
    word = random.choice(words)
    return word

def end_game():
    print("hello")


def run_game():
    """
    Will start the game if the user enters 'y' on the welcome screen.
    """
    word = get_word(words)
    secret = "_" * len(word)
    print(f" guess the word: {secret}")
    print(word)
    already_guessed = []
    lives_left = 6
    while lives_left > 0:
        word_list = [letter if letter in already_guessed else '_' for letter in word]
        if "_" not in word_list:
            end_game()
            print("Congratulations, you guessed the word")
            print(f"The Hangman's secret word was '{word}'")
            break
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

welcome_screen()

#def end_game():
#    print("hello")
#    #break

