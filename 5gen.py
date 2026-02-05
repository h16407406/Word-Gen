import string
import random
import os
import re


v = list(string.ascii_letters + " " + ".")
v3 = [char for char in v if not char.isupper()]
v2 = {char: [] for char in v3}
v4 = {}

with open("Language.txt", "r", encoding="utf-8") as f:
    text = ''.join(c.lower() for c in f.read() if c.isalpha() or c == " " or c == ".")

for i in range(len(text) - 5):
    quint = text[i:i+5]
    next_char = text[i+5]
    if quint not in v4:
        v4[quint] = []
    v4[quint].append(next_char)

def auto_capitalize(text):
    sentences = re.split(r'(?<=[.])\s*', text.strip())
    capitalized = [s.capitalize() for s in sentences if s]
    return ' '.join(capitalized)

start = input("Prompt letters (5 chars): ").lower()
while len(start) != 5:
    print("No")
    start = input("Retry prompt letters: ").lower()

while True:
    try:
        nm = int(input("NM: "))
        break
    except ValueError:
        print("No")

while True:
    made = list(start)
    for _ in range(nm - 5):
        key = ''.join(made[-5:])
        if key in v4 and v4[key]:
            next_char = random.choice(v4[key])
        else:
            next_char = random.choice(v3)
        made.append(next_char)

    generated = "".join(made)
    words = generated.split()
    joined_text = " ".join(words)
    final_text = auto_capitalize(joined_text)
    print("\n" + final_text + "\n")

    again = input("Retry(y/n): ")
    if again.lower() == "n":
        break

