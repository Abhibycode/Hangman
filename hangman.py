#Hangman or Batman?
import random

# List of words to guess
words = ["joker", "riddler", "freeze", "hush", "pyg", "poisonivy", "penguin", "twoface", "scarecrow", "bane"]

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  # Create a list of underscores


print("Welcome to hangman game\nIt's no ordinary game\nIt's life or death situation\nA crime is attempted, you have guess which batman villan could have done this?")

def Game():
    attempts = 8  # Number of allowed attempts
    while attempts > 0 and '_' in word_display:
        print("\n" + ' '.join(word_display))
        guess = input("Guess a letter: ").lower()

        # Check if the guessed letter is in the chosen word
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[index] = guess  # Reveal the letter
        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1


    # Game conclusion
    if '_' not in word_display:
        print("You guessed the word!")
        print(' '.join(word_display))
        print("You survived!")
    else:
        print("You ran out of attempts. The word was: " + chosen_word)
        print("You lost!")

Q = str(input("Are you ready for the trial?(y/n): "))
if Q == 'y':
    Game()
else:
    print("See you next time")