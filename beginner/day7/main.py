# The Hangman Game
import random
from hangman_words import word_list
from hangman_art import logo, stages

end_of_game = False
chosen_word = random.choice(word_list)

lives = 6

display = []
for _ in chosen_word:
    display.append('_')

print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(
            f"You've already guessed {guess}. Try again with a different letter.")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives < 1:
            end_of_game = True
            print("You lose!")

    print(" ".join(display))

    if '_' not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
