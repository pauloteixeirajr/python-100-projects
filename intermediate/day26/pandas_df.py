import pandas
# Iterating over Pandas DataFrame

student_dict = {
    "student": ["Angie", "James", "Lily"],
    "score": [56, 76, 98]
}

df = pandas.DataFrame(student_dict)

# Loop through rows of dataframe
for (index, row) in df.iterrows():
    print(index)
    print(row.student)
    print(row.score)
