import sys
import random


def create_line(words_per_line, word_bank):
    if word_bank is None:
        word_bank = ["none"] * 100
    final_str = ""
    for i in range(0, words_per_line):
        final_str += " " + str(word_bank[i])
    return final_str


input_file = open(str(sys.argv[1]), "r").read()
word_bank = input_file.split(" ")
words_per_line = int(input("How many words per line?\n"))
lines_total = int(input("how many lines will this poem be?\n"))
print("\n")
for i in range(0, lines_total):
    random.shuffle(word_bank)
    print(create_line(words_per_line, word_bank))

print("\n\n")
