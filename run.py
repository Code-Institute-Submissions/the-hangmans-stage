import random


def welcome_screen():
    """
    This is the games home screen, it displays the title graphic,
    welcomes players to the game and explain the rules.
    Players are asked to input Y or N to play or exit the game."
    """
    title_graphic()
    print("Hi, welcome to The Hangman's Stage!")
    print(
        """
        The rules of the game are simple. Guessing 1 letter at a time,
        you have to guess The Hangman's secret word and survive.
        You can play with 6 lives or risk playing with 3!
        Let's see if you can escape The Hangman's stage!
        """
        )
    while True:
        print("Would you like to play Hangman?")
        play_game = input("Enter 'Y' for yes or 'N' for no:\n").upper()
        print("")
        if play_game == "Y":
            select_theme()
        elif play_game == "N":
            end_game()
        else:
            print("Invalid input. Please enter 'Y' to play or 'N' to exit")


def end_game():
    """
    This function thanks the user for playing and then exits the game.
    """
    print("Thank you for playing The Hangman's Stage")
    exit()


def continue_game():
    """
    This function is displayed after the player has successfuly
    or unsuccessfuly guessed the secret word. It allows the player
    to continue playing or exit the game.
    """
    print("Would you like to continue playing?\n")
    print("y - Continue playing")
    print("n - Exit Game")
    replay = input("\n").upper()
    if replay == "Y":
        select_theme()
    elif replay == "N":
        end_game()
    else:
        print("Invalid input. Please enter 'Y' to continue or 'N' to exit")


def select_theme():
    """
    This function allows the user to select a theme for their secret word.
    It will then choose a random word from the choosen theme list text file.
    I have used 'while' to filter only for single word answers in my theme
    files.
    """
    while True:
        print("Please choose a theme for your secret word\n")
        print("1 - Animals")
        print("2 - Country Names")
        print("3 - Marvel Comic Characters")
        print("4 - Pokemon")
        print("5 - Random Words")
        theme = input("\n")
        if theme == "1":
            with open('animals.txt', 'r') as animals:
                words = animals.readlines()
            word = random.choice(words)[:-1].upper()
            while "-" in word or " " in word or "." in word or "'" in word:
                word = random.choice(words)[:-1].upper()
            run_game(word)
        elif theme == "2":
            with open('countries.txt', 'r') as countries:
                words = countries.readlines()
            word = random.choice(words)[:-1].upper()
            while "-" in word or " " in word or "." in word or "'" in word:
                word = random.choice(words)[:-1].upper()
            run_game(word)
        elif theme == "3":
            with open('marvel.txt', 'r') as marvel:
                words = marvel.readlines()
            word = random.choice(words)[:-1].upper()
            while "-" in word or " " in word or "." in word or "'" in word:
                word = random.choice(words)[:-1].upper()
            run_game(word)
        elif theme == "4":
            with open('pokemon.txt', 'r') as pokemon:
                words = pokemon.readlines()
            word = random.choice(words)[:-1].upper()
            while "-" in word or " " in word or "." in word or "'" in word:
                word = random.choice(words)[:-1].upper()
            run_game(word)
        elif theme == "5":
            with open('random_words.txt', 'r') as random_words:
                words = random_words.readlines()
            word = random.choice(words)[:-1].upper()
            while "-" in word or " " in word or "." in word or "'" in word:
                word = random.choice(words)[:-1].upper()
            run_game(word)
        else:
            print("Enter a number between 1 and 5 to choose a theme")


def select_lives():
    """
    This function allows the user to select how many lives they wish to
    play with.
    """
    lives_left = 0
    print(
        """
        Are you up for a challenge? You can chose to play 6 lives as normal,
        or take a risk and play with 3!
        """)
    print("")
    print("Enter 6 for 6 lives")
    print("Enter 3 for 3 lives")
    while lives_left == 0:
        lives = input("\n")
        if lives == "6":
            return 6
        elif lives == "3":
            return 3
        else:
            print("Please enter '6' for 6 lives or '3' for 3 lives")
    print("")


def run_game(word):
    """
    Will start the game if the user enters 'Y' on the welcome screen
    and has choosen a theme for their secret word. It takes the arguement
    'word' to use a word for the player to guess. It displays underscores
    for the length of the secret word and replaces these with correctly
    guessed letters. Incorrect guesses display the hanging stages.
    """
    secret = "_" * len(word)
    guesses = []
    lives_left = select_lives()
    print("")
    while lives_left > 0:
        word_list = [letter if letter in guesses else '_' for letter in word]
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
        print('Current word: ', ' '.join(word_list))
        guessed_letter = input("Please guess a letter:\n").upper()
        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            if guessed_letter in guesses:
                print("You have already guessed that letter")
                guesses.append(guessed_letter)
            elif guessed_letter not in word:
                print(f"Sorry, {guessed_letter} is not in the secret word.")
                guesses.append(guessed_letter)
                lives_left -= 1
                print(f"You have {lives_left} lives left")
            else:
                guesses.append(guessed_letter)
                print(f"Congrats, {guessed_letter} is in the secret word")
        elif len(guessed_letter) != 1:
            print("Please enter 1 letter at a time")
        else:
            print("You entered an invalid character! Pick a letter from A - Z")
        print("Used letters: " + ", ".join(guesses) + "\n")
        print(hangman_lives(lives_left))
    if lives_left == 0:
        lose_graphic()
        print(
            f"""
            You failed to guess The hangman's secret word
            The Hangman's secret word was '{word}.'\n
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
    """
    This is the graphic displayed when the player successfuly guesses
    the secret word.
    """
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
    """
    This is the graphic displayed when the player has used all their lives
    and failed to guessthe secret word.
    """
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
    """
    These graphics represent the players lives and are looped through
    dependent on the amount of lives the player has left. It takes the
    argument lives_left to run through the index and display the right
    graphic."
    """
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


def main():
    """
    Runs the program.
    """
    welcome_screen()

main()
