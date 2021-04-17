import pandas

# Create a dictionary:
df = pandas.read_csv("./intermediate/day26/nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (_, row) in df.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
spelling = [nato_alphabet[letter] for letter in word if letter != " "]
print(spelling)
