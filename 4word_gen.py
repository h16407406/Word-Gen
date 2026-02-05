import random
import re

with open("all.txt", "w") as f:
    f.write("")
def auto_capitalize(text):
    text = text.strip()
    if not text:
        return text
    def cap_sentence(match):
        return match.group(1) + match.group(2).upper()
    text = text[0].upper() + text[1:]
    text = re.sub(r'([\.!?]\s+)(\w)', cap_sentence, text)
    return text

def trim_to_last_sentence(text):
    matches = re.findall(r'.*?[.!?](?=\s|$)', text)
    return ' '.join(matches).strip() if matches else text


def r(filename, n=4):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    # Split into sentences (basic, using punctuation)
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Get first words of sentences (cleaned)
    first_words = [s.strip().split()[0] for s in sentences if s.strip()]

    # Pick n random ones
    return random.sample(first_words, min(n, len(first_words)))


#docu = input(":").strip().lower()
docu = "try"
if docu == "global warming":
    doc = "warming2.txt"
    start_words = ["global", "warming", "is", "the"]
elif docu == "try":
    doc = "try.txt"
    start_words = r("try.txt")
    print(start_words)
elif docu == "poems":
    doc = "Language.txt"
    start_words = ["i", "have", "seen", "the"]
else:
    print("Unknown option.")
    exit()

with open(doc, "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(r'\[.*?\]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

words = text.lower().split()
order = 4

markov_dict = {}
for i in range(len(words) - order):
    key = tuple(words[i:i+order])
    next_word = words[i + order]
    if key not in markov_dict:
        markov_dict[key] = []
    markov_dict[key].append(next_word)

if tuple(start_words) not in markov_dict:
    fallback = random.choice(list(markov_dict.keys()))
    print(f"Start sequence not found. Using: {' '.join(fallback)}")
    start_words = list(fallback)

length = 300
print(f"Number of words used to generate: {len(words)}")
while True:
    output = start_words.copy()
    for _ in range(length):
        key = tuple(output[-order:])
        next_words = markov_dict.get(key)
        if not next_words:
            key = random.choice(list(markov_dict.keys()))
            next_word = random.choice(markov_dict[key])
        else:
            next_word = random.choice(next_words)
        output.append(next_word)

    raw_text = " ".join(output)
    clean_text = trim_to_last_sentence(raw_text)
    final_text = auto_capitalize(clean_text)

    print("\n" + final_text + "\n")
    again = input("Retry(y/n): ").lower()
    if again == "n":
        break

