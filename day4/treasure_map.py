# Write a program which will mark a spot with an X
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]
print(f"\n{row1}\n\n{row2}\n\n{row3}\n")
position = input("Where do you want to put the treasure? ")
col = int(position[0]) - 1
row = int(position[1]) - 1

map[row][col] = "❌"
print(f"{row1}\n\n{row2}\n\n{row3}")
