# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
#
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 ✖️ 4) ÷ 5 = 1.6
import math


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You will need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
