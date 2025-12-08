#Day 26 - NATO Speller
# Made to help you spell out stuff.
import pandas
student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


di = student_data_frame.to_dict()
abd = {}
key = 0
for value in di['letter']:
    abd[di["letter"][value]] = di['code'][key]
    key += 1

newWordL = []
newWordS = ""

word = input("What is the word that you want to spell? ")
for letter in word:
    if letter.upper() in abd:
        newWordL.append(abd[letter.upper()])
    else:
        newWordL.append(letter)

for value in newWordL:
    newWordS += value + " "
print(newWordS)
