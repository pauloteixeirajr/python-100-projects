import random


def check_answer(guess, answer, attempts):
    """ Checks the answer and returns the remaining attempts """
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return 0
    elif guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    return attempts - 1


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    attempts = set_difficulty()
    guess = None

    while answer != guess:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)

        if attempts > 1:
            print("Guess again.\n")
        elif attempts == 0:
            print("You've run out of guesses, you lose.")
            return


game()
