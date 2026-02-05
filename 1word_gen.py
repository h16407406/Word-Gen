import string
import random
import os
import difflib
import nltk

nltk.download('words', quiet=True)
from nltk.corpus import words

word_list = set(w.lower() for w in words.words())


def get_similar_word(word, cutoff=0.6):
    matches = difflib.get_close_matches(word, word_list, n=20, cutoff=cutoff)
    if matches:
        return random.choice(matches)
    return word



v = list(string.ascii_letters + " " + ".")
v3 = [char for char in v if not char.isupper()]
v2 = {char: [] for char in v3}

with open("Language.txt", "r", encoding="utf-8") as f:
    text = ''.join(c.lower() for c in f.read() if c.isalpha() or c == " " or c == ".")

for i in range(len(text) - 1):
    letter = text[i]
    if letter in v2:
        v2[letter].append(text[i + 1])

# print(v2)

letter_index = 0

start = input("Prompt letter: ")
while len(start) != 1 or not start in v2:
    print("No")
    start = input("Retry prompt letter: ")

made = [start]
while True:
    try:
        nm = int(input("NM: "))
        break
    except ValueError:
        print("No")

for _ in range(nm - 1):
    last = made[-1]
    if (v2[last]):
        next_char = random.choice(v2[last])
    else:
        next_char = random.choice(v3)
    made.append(next_char)
generated = ("".join(made))
l = generated.split()

final_words = []

for word in l:
    has_period = word.endswith(".")
    cleaned = ''.join(c for c in word if c.isalpha())
    if cleaned in word_list:
        final = cleaned
    elif cleaned:
        final = get_similar_word(cleaned)
    else:
        continue

    if has_period:
        final += "."

    final_words.append(final)
end = " ".join(final_words)

finish = []
capitalize_next = True

for char in end:
    if capitalize_next and char.isalpha():
        finish.append(char.upper())
        capitalize_next = False
    else:
        finish.append(char)

    if char == '.':
        capitalize_next = True
    elif char not in string.whitespace and char != '.':
        capitalize_next = False

print("".join(finish))
