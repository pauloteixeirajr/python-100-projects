# The Hangman Game
import random

# Step 3
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for _ in chosen_word:
    display.append('_')

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user
# has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if '_' not in display:
        end_of_game = True
        print("You win!")
