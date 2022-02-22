# **The Hangman's Stage!**
## **Aim of the site**

The aim of the site is to allow users to play a single player python command line version of the Hangman game. There are 3 categories of words for players to choose from on each run through of the game. The player then has 6 guesses to correctly guess the secret word or fail the game.

## **Game Features**
### **Title Screen**

![Title Screen](assets/docs/screenshots/title_screen.jpg)

The title screen welcomes players to the site, explains the rules and asks the player to input "y" to play the game and "n" to exit the game.

### **Theme Choices**

![Themes](assets/docs/screenshots/theme_choices.jpg)

Once the user has input "y" to play the game, they're presented with a list of theme's to choose for the secret word.

### **Game Play**

**The Secret Word**

The secret word is presented to user with a series of underscores which match the length of the secret word. Underscores are replaced with correct letter guesses.

As the player guesses letters, the letter is appended to a list of used characters which is then printed so the player is aware of letters they have already guessed. 
**Invalid Selections**

If the player inputs an invalid selection, such as too many letters, numbers or a letter than have already entered, they're presented with an error message.

**Hanging Stages**

The player is given 6 lives at the start of the game. Each incorrect answer is visally represented with a hangman graphic. Each of the 6 lives is associated with a body part: head, torso, left arm, right arm, left leg and right leg.

**Correctly Or Incorrectly Guessing The Word**

If the player manages to correctly guess the word within their 6 lives, they're presented with a congratulatory message and asked if they would like to continue playing. On the other hand, if the player fails to guess the word, they're presented with a fail message and again asked if they would like to continue playing.

## **Possible Future Features**

* A timer feature, so the player is not only playing against the 6 lives but also timing out will result in a failure.
* Difficulty levels, with increased or decreased number of lives. This was a feature I did look at implementing, and had working in part but ran out of time to finish.

## **Testing**

The game has been deployed using Heroku and runs in a command line Python Terminal. I've tested the site using Chrome, Firefox and Edge browsers on PC and also on mobile using Chrome. I tried to cause the code to crash at various points using incorrect inputs to try and make the code break it's loop. Thankfully any incorrect inputs result in an error message and ask for a valid input.

## **Technologies Used**

This project has been created using Python. Any other technologies present such as javascript are part of the Code Institute template used to create this project.
I have run the python code through the [PEP8 Validator](http://pep8online.com/) which resulted in no errors.

## **Bugs**

1.  **Intended Outcome** - ASCII Art to be used for graphics
    * ***Issue Found***
        * The backslashes present in the ASCII Art used for my title, win and fail graphics would cause these graphics to be printed out incorrectly. These would appear blue in the code
    * ***Solution***
        * To resolve this, I had to use double backslashes wherever a blue backslash was present.

2. **Intended Outcome** - Incorrect Input to not break out of code loop when choosing theme
    * ***Issue Found***
        * If the player input and invalid option at the chose theme stage, the game would fall out of the loop.
    * ***Solution***
        * Added a while True statement to this stage.