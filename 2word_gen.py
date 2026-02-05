import random
import re


with open("warming.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words = text.split()

markov_dict = {}

for i in range(len(words) - 2):
    key = (words[i], words[i+1])
    next_word = words[i+2]
    if key not in markov_dict:
        markov_dict[key] = []
    markov_dict[key].append(next_word)

start_words = input("Enter two starting words: ").lower().split()
while len(start_words) != 2 or tuple(start_words) not in markov_dict:
    print("Invalid input or start words not found.")
    start_words = input("Retry starting words (two words): ").lower().split()

try:
    length = int(input("Number of words to generate: "))
except ValueError:
    length = 20  # default length

def auto_capitalize(text):
    text = text.strip()
    if not text:
        return text
    def cap_sentence(match):
        return match.group(1) + match.group(2).upper()
    text = text[0].upper() + text[1:]
    text = re.sub(r'([\.]\s+)(\w)', cap_sentence, text)
    return text

while True:
    output = start_words.copy()
    for _ in range(length):
        key = (output[-2], output[-1])
        next_words = markov_dict.get(key, None)
        if not next_words:
            break
        next_word = random.choice(next_words)
        output.append(next_word)

    generated_text = " ".join(output)
    print("\n" + auto_capitalize(generated_text) + "\n")

    again = input("Retry(y/n): ")
    if again.lower() == "n":
        break
