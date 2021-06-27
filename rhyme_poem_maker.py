import sys
import random



def get_rhyming_pairs(word_bank, min_matching_last_letters = 2, ing_words = False):
    new_word_bank = []
    word_bank = list(set(word_bank))
    rhyme_pairs = set()
    # strip all words less than 3 characters
    for i in range(0, len(word_bank)):
        curr_word = (str(word_bank[i]).replace(",", "").replace(".", ""))
        if not ing_words and (curr_word.endswith("ing")):
            continue
        if ((len(curr_word)) > 2) and (curr_word not in new_word_bank):
            new_word_bank.append(curr_word)
    # iterate over all words n2 style looking for rhyming pairs
    for i in range(0, len(new_word_bank)):
        for j in range(0, len(new_word_bank)):
            # make sure they're not identical words (we don't want that kind of rhyme)
            curr1, curr2 = new_word_bank[i], new_word_bank[j]
            len1, len2 = len(curr1), len(curr2)
            if curr1 != curr2:
                # check if the last 2, 3, 4, or 5 letters match
                for letter_counts in list(list(range(min_matching_last_letters, 6))[::-1]):
                    if (len1 > letter_counts) and (len2 > letter_counts):
                        if curr1[::-1][:letter_counts] == curr2[::-1][:letter_counts]:
                            templist = [curr1, curr2]
                            templist.sort()
                            rhyme_pairs.add((templist[0], templist[1]))
                            continue
    return rhyme_pairs

def create_poem_rhyming_aa(words_per_line, lines_total, word_bank, rhyme_letter_match):
    pairs = get_rhyming_pairs(word_bank, rhyme_letter_match)
    if len(pairs) < 1:
        print("No rhyming pairs found in dataset, cannot create rhyming poem")
        exit(1)
    poem_lines = []
    print("\n")
    # create pair lines and replace their final words with our rhyming ones
    for i in range(0, lines_total, 2):
        random.shuffle(word_bank)
        linebuffer1 = create_line(words_per_line, word_bank).split(" ")
        random.shuffle(word_bank)
        linebuffer2 = create_line(words_per_line, word_bank).split(" ")
        # random.choice gets a random item with replacement
        # random.sample gets a random item without replacement
        random_pair = random.choice(list(pairs))
        linebuffer1 = linebuffer1[:len(linebuffer1)-1]
        linebuffer1.append(random_pair[0])
        linebuffer2 = linebuffer2[:len(linebuffer2)-1]
        linebuffer2.append(random_pair[1])
        # add them to the total poem
        poem_lines.append(str(' '.join(linebuffer1)).strip())
        poem_lines.append(str(' '.join(linebuffer2)).strip())
    for i in range(0, lines_total):
        print(poem_lines[i])
    print("\n")

def create_line(words_per_line, word_bank):
    if word_bank is None:
        word_bank = ["none"] * 100
    final_str = ""
    for i in range(0, words_per_line):
        final_str += " " + str(word_bank[i])
    return final_str

def create_poem(words_per_line, lines_total, word_bank):
    print("\n")
    for i in range(0, lines_total):
        random.shuffle(word_bank)
        print(create_line(words_per_line, word_bank))
    print("\n")

def read_file():
    if(len(sys.argv) < 2):
        print("Usage: python3 rhyme_poem_maker.py wordbank.txt")
        print('''\t>the wordbank can be any text file and each word will be anything delimited by spaces''')
    return open(str(sys.argv[1]), "r").read()

def get_input(user_input = True):
    input_file = read_file()
    word_bank = input_file.replace("\n", "").strip().split(" ")
    words_per_line = 5
    lines_total = 5
    if(user_input == True):
        try:
            words_per_line = input("How many words per line?\n")
            words_per_line = int(words_per_line)
            if(words_per_line > len(word_bank)):
                print("\t>Invalid, line length selected it larger than wordbank.")
                print("\t>Defaulting to 5 words per line.")
            elif(words_per_line <= 0):
                print("\t>Invalid, line length selected less than or equal to zero.")
                print("\t>Defaulting to 5 words per line.")
        except TypeError:
            print("Input: '" + str(words_per_line) + "' not recognized as valid integer value")
        try:
            lines_total = input("How many lines will this poem be?\n")
            lines_total = int(lines_total)
        except TypeError:
            print("Input: '" + str(lines_total) + "' not recognized as valid integer value")
        print("")
    return (words_per_line, lines_total, word_bank)

if __name__ == '__main__':
    words_per_line, lines_total, word_bank = get_input()
    print("Standard Poem:")
    create_poem(words_per_line, lines_total, word_bank)
    print("Rhyming Poem:")
    # the last argument is for the number of matching letters to consitute a rhyme
    create_poem_rhyming_aa(words_per_line, lines_total, word_bank, 3)
