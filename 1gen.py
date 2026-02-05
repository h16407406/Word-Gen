import string
import random
import os
import re
from itertools import product


v = list(string.ascii_letters + " "+".")
v3 = [char for char in v if not char.isupper()]
v2 = {char: [] for char in v3}#


with open("warming2.txt", "r", encoding="utf-8") as f:
	text = ''.join(c.lower() for c in f.read() if c.isalpha() or c == " " or c == ".")

for i in range(len(text)-1):
	letter = text[i]
	if letter in v2:
		v2[letter].append(text[i+1])

def auto_capitalize(text):
	sentences = re.split(r'(?<=[.])\s*', text.strip())
	capitalized = [s.capitalize() for s in sentences if s]
	return ' '.join(capitalized)

#print(v2)

letter_index=0

start = input("Prompt letter: ")
while len(start) != 1 or not start in v2:
	print("No")
	start = input("Retry prompt letter: ")

while True:
	try:
		nm = int(input("NM: "))
		break
	except ValueError:
		print("No")

while True:
	made = list(start)
	for _ in range(nm - 1):
		key = made[-1]
		if key in v2 and v2[key]:
			next_char = random.choice(v2[key])
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
