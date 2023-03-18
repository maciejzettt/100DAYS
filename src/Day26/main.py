

import pandas


nato_df = pandas.read_csv('./nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (item, row) in nato_df.iterrows()}

word = input("What is your word?")
nato_word = [nato_dict[letter.upper()] for letter in word]

print(f"NATO phonetic representation of '{word}' is {nato_word}.")
