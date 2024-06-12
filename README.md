# Repository
This repository contains an app made by:
- Camila Maire
- Daylin Ortega
- Ignacio Romero

The app contains three functions:

## Rock Paper Scissors Lizard Spock

### Description
This Python function implements the extended version of the classic Rock, Paper, Scissors game, including two additional choices: Lizard and Spock. The game rules were popularized by the TV show *The Big Bang Theory*. This function was designed by Ignacio Romero on nacho-branch.

### Game Rules
- **Scissors** cuts **Paper**
- **Paper** covers **Rock**
- **Rock** crushes **Lizard**
- **Lizard** poisons **Spock**
- **Spock** smashes **Scissors**
- **Scissors** decapitates **Lizard**
- **Lizard** eats **Paper**
- **Paper** disproves **Spock**
- **Spock** vaporizes **Rock**
- **Rock** crushes **Scissors**

### Function
The function `rock_paper_scissors_lizard_spock` takes the player's choice as input and randomly generates a choice for the computer. It then determines the winner based on the above rules.

## Wordle

### Description
This python function implements a Wordle game programme. This function was designed by Daylin Ortega on day-branch.

### Game Rules

It is a game that consists of guessing the 5-letter word, having a limited
number of attempts to do so, in this case, there will be six opportunities.

In each round, the game colors each letter indicating if that letter is
in the word and if it is in the correct position.

1. GREEN means the letter is in the word and in the CORRECT position.
2. YELLOW means the letter is in the word but in the INCORRECT position.
3. GRAY means the letter is NOT present in the word.

## Main Menu

### Description
The menu displays the on screen for the user.
This function allows the user to choose playing between the games already described before or exiting the menu with a goodbye message and was designed by Camila Maire on cami-branch.

### Function
This function allows a user to select one of the mentioned games or close down the application properly.

Behavior:
The function contains an endless loop that displays menu options until the user decides to leave.
User is requested to enter a number (1, 2, or 3) which prompts their for selecting an option.
  Option 1: For instance, this can be “rock, paper, scissors, lizard, spock”. Next call is made to rock_paper_scissors_lizard_spock function using user’s selection and its output gets printed. In case this function does not exist error message is produced.
    
  Option 2: If wordle exists in the functions it uses the name otherwise it prints out an error message.
    
  Option 3: At this point good bye is displayed and then we exit from the menu breaking out of the loop.
    
  Any other input results in an "undefined option" message.

