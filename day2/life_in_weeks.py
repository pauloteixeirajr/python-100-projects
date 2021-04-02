# Create a program using maths and f-strings that tells us
# how many days, weeks and months we have left if we live
# until 90 years old.
age = input('What is your current age? ')

age_int = int(age)
y_left = 90 - age_int
m_left = y_left * 12
w_left = y_left * 52
d_left = y_left * 365

print(f'You have {d_left} days, {w_left} weeks and {m_left} months left')
