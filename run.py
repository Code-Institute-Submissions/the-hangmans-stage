import random
from words import superheroes, words, cartoons


def welcome_screen():
    """
    This is the home screen and will take the players username
    and welcome them to the game.
    """
    title_graphic()
    print("Hi, welcome to The Hangman's Stage!")
    print(
        """
        The rules of the game are simple. Guessing 1 letter at a time,
        you have 6 lives to guess The Hangman's secret word and survive.
        Let's see if you can escape The Hangman's stage!
        """
        )
    while True:
        print("Would you like to play Hangman?")
        play_game = input("Enter 'y' for yes and 'n' for no:\n").lower()
        print("")
        if play_game == "y":
            get_theme()
        elif play_game == "n":
            end_game()
        else:
            print("Please enter a valid selection")


def end_game():
    """
    This function thanks the user for playing and then exits the game.
    """
    print("Thank you for playing Hangman")
    exit()


def continue_game():
    print("Would you like to continue playing?\n")
    print("y - Continue playing")
    print("n - Exit Game")
    replay = input("\n").lower()
    if replay == "y":
        select_theme()
    elif replay == "n":
        end_game()
    else:
        print("Please enter a valid selection")


def select_theme():
    while True:
        print("Please choose a theme for your secret word\n")
        print("1 - Superheroes")
        print("2 - Cartoons")
        print("3 - anything goes")
        theme = input("\n")
        if theme == "1":
            word = random.choice(superheroes)
            run_game(word)
        elif theme == "2":
            word = random.choice(cartoons)
            run_game(word)
        elif theme == "3":
            word = random.choice(words)
            while "-" in word or " " in word:
                word = random.choice(words)
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
        word_list = [letter if letter in already_guessed else '_' for
                     letter in word]
        if "_" not in word_list:
            win_graphic()
            print(
                f"""
                Congratulations, you guessed The hangman's secret word.
                The Hangman's secret word was '{word}'.
                You have escaped The Hangmans's stage for now!
                Will you risk another go?\n
                """)
            continue_game()
        print(word_list)
        print('Current word: ', ' '.join(word_list))
        guessed_letter = input("Please guess a letter:\n").lower()
        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            if guessed_letter in already_guessed:
                print("You have already guessed that letter")
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
        print("Used letters: " + ", ".join(already_guessed) + "\n")
        print(hangman_lives(lives_left))
    if lives_left == 0:
        lose_graphic()
        print(
            f"""
            You failed to guess The hangman's secret word
            The Hangman's secret word was '{word}'\n
            """)
        continue_game()


def title_graphic():
    """
    This is the welcome screen title graphic.
    It is displayed only on the initial startup of the game.
    """
    print(
        """
 __ __   ____  ____    ____  ___ ___   ____  ____
|  |  | /    ||    \  /    ||   |   | /    ||    \\
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|
""")


def win_graphic():
    print(
        """

               /$$
              |__/
 /$$  /$$  /$$ /$$ /$$$$$$$
| $$ | $$ | $$| $$| $$__  $$
| $$ | $$ | $$| $$| $$  \ $$
| $$ | $$ | $$| $$| $$  | $$
|  $$$$$/$$$$/| $$| $$  | $$
 \_____/\___/ |__/|__/  |__/
    """
    )


def lose_graphic():
    print(
        """
   _____   _____     __   __
 /\_____\ /\___/\   /\_\ /\_\\
( (  ___// / _ \ \  \/_/( ( (
 \ \ \_  \ \(_)/ /   /\_\\ \_\\
 / / /_\ / / _ \ \  / / // / /__
/ /____/( (_( )_) )( (_(( (_____(
\/_/     \/_/ \_\/  \/_/ \/_____/
"""
    )


def hangman_lives(lives_left):
    hanging_stages = [
        """
            ======
           |/    |
           |     O
           |    /|\\
           |     |
           |    / \\
           |
         __|\_______
        |           |
        |___________|
        """,
        """
            ======
           |/    |
           |     O
           |    /|\\
           |     |
           |    /
           |
         __|\_______
        |           |
        |___________|
        """,
        """
            ======
           |/    |
           |     O
           |    /|\\
           |     |
           |
           |
         __|\_______
        |           |
        |___________|
        """,
        """
            ======
           |/    |
           |     O
           |    /|
           |     |
           |
           |
         __|\_______
        |           |
        |___________|
        """,
        """
            ======
           |/    |
           |     O
           |     |
           |     |
           |
           |
         __|\_______
        |           |
        |___________|
        """,
        """
            ======
           |/    |
           |     O
           |
           |
           |
           |
         __|\_______
        |           |
        |___________|
        """,
        """
            ======
           |/    |
           |
           |
           |
           |
           |
         __|\_______
        |           |
        |___________|
        """
    ]
    return hanging_stages[lives_left]


welcome_screen()
