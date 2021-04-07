import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Rock wins against scissors
# Paper wins against rock.
# Scissors win against paper

game_choices = [rock, paper, scissors]
user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_choices[user_choice])

    print("Computer chose: ")
    cpu_choice = random.randint(0, 2)
    print(game_choices[cpu_choice])

    if user_choice == cpu_choice:
        print("It's a draw")
    elif user_choice == 0 and cpu_choice == 2:
        print("You win!")
    elif user_choice == 1 and cpu_choice == 0:
        print("You win!")
    elif user_choice == 2 and cpu_choice == 1:
        print("You win!")
    else:
        print("You lost :(")
