import os
def clear(): return os.system('clear')


clear()
print('''
             ___________
             \         /
              )_______(
              |"""""""|_.-._,.---------.,_.-._
              |       | | |               | | ''-.
              |       |_| |_             _| |_..-'
              |_______| '-' `'---------'` '-'
              )"""""""(
             /_________\\
           .-------------.
          /_______________\\
''')
print("Welcome to the secret auction program.")

auction = {}
should_continue = True

while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    auction[name] = bid

    result = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if result == 'no':
        should_continue = False

    clear()


highest_bid = 0
winner = ""
for name in auction:
    if auction[name] > highest_bid:
        highest_bid = auction[name]
        winner = name

print(f"The winner is {winner} with a bid of ${highest_bid}.")
