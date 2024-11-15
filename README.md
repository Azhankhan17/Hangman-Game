# Hangman Game

This is a simple text-based **Hangman** game implemented in Python. 
The program selects a random word, and the player guesses one letter at a time to uncover the word. 
The player has a limited number of incorrect guesses allowed before the game is lost.

## Author- Azhan Khan


## Features
- Random word selection from a predefined list.
- Display of the partially guessed word with placeholders for unguessed letters.
- Count of remaining incorrect guesses.
- Win/lose messages when the game ends.

## Rules
1. The player must guess one letter at a time.
2. If the letter is in the word, it will be revealed in its correct position(s).
3. If the letter is not in the word, it counts as an incorrect guess.
4. The game ends when the player guesses all letters correctly (win) or uses up all allowed incorrect guesses (lose).

## Setup
1. **Install Python**: Make sure Python is installed on your computer. [Download Python here](https://www.python.org/downloads/).
2. **Clone or Download this Repository**.
3. **Run the Game**:
   - Open a terminal and navigate to the directory containing the `hangman.py` file.
   - Run the game by entering:
     ```bash
     python hangman.py
     ```

## How to Play
1. The program will display a series of underscores representing each letter in the randomly selected word.
2. You will be prompted to enter a letter as a guess.
3. The game will tell you whether your guess is correct or incorrect.
4. Continue guessing letters until you either:
   - Uncover the entire word (you win), or
   - Reach the maximum number of incorrect guesses (you lose).

## Example Gameplay
