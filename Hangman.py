import random

# List of words for the game
word_list = ["azhan", "python", "programming", "challenge", "developer", "algorithm", "function", "variable"]

# Function to select a random word from the list
def get_random_word(word_list):
    return random.choice(word_list)

# Main function to play the game
def play_hangman():
    word = get_random_word(word_list)
    word_length = len(word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("_ " * word_length)

    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("\nGuess a letter: ").lower()

        # Check if input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add guessed letter to the set
        guessed_letters.add(guess)

        # Check if guessed letter is in the word
        if guess in word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        # Display the current progress
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display_word))

        # Check if player has won
        if "_" not in display_word:
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print("Sorry, you've run out of guesses. The word was:", word)

# Run the game
play_hangman()
