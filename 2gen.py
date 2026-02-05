import string
import random
import os
import re
from itertools import product


v = list(string.ascii_letters + " " + ".")
v3 = [char for char in v if not char.isupper()]
v2 = {char: [] for char in v3}
v4 = {''.join(pair): [] for pair in product(v3, repeat=2)}

with open("Language.txt.txt", "r", encoding="utf-8") as f:
    text = ''.join(c.lower() for c in f.read() if c.isalpha() or c == " " or c == ".")

for i in range(len(text) - 2):
    pair = text[i:i + 2]
    if pair in v4:
        v4[pair].append(text[i + 2])


def auto_capitalize(text):
    sentences = re.split(r'(?<=[.])\s*', text.strip())
    capitalized = [s.capitalize() for s in sentences if s]
    return ' '.join(capitalized)


# print(v4)

letter_index = 0

start = input("Prompt letters: ")
while len(start) != 2 or not start in v4:
    print("No")
    start = input("Retry prompt letters: ")

while True:
    try:
        nm = int(input("NM: "))
        break
    except ValueError:
        print("No")

while True:
    made = list(start)
    for _ in range(nm - 2):
        key = made[-2] + made[-1]
        if key in v4 and v4[key]:
            next_char = random.choice(v4[key])
        else:
            next_char = random.choice(v3)
        made.append(next_char)
    generated = "".join(made)
    words = generated.split()
    joined_text = " ".join(words)
    final_text = auto_capitalize(joined_text)
    print("\n" + "".join(final_text) + "\n")
    again = input("Retry(y/n): ")
    if again.lower() == "n":
        break

