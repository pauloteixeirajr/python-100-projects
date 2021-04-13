print("Welcome to the tip calculator.")
total = float(input("What was the total bill?: $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?: "))
party_size = int(input("How many people to split the bill?: "))
total_by_person = round((total * (tip / 100) + total) / party_size, 2)

message = f"Each person shoudl pay: ${total_by_person}"
print(message)
