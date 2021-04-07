# Write a program that calculates the average student height from a list of heights
student_heights = input("Input a list of student heights:\n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# From this point, you are not allowed to use len() and sum()
sum = 0
count = 0

for height in student_heights:
    sum += height
    count += 1

avg_height = round(sum / count)
print(f"The average height is: {avg_height}")
