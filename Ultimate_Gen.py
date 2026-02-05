import random
import re

# ===================== Load Diverse Text Corpus =====================
files = [
    "science.txt", "history.txt", "tech.txt",
    "philosophy.txt", "literature.txt"
]
text = ""
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        text += f.read() + " "

# Clean text
text = re.sub(r'\[.*?\]', '', text)  # Remove bracketed content
text = re.sub(r'\s+', ' ', text).strip()
words = text.split()
order = 4  # Markov chain order

# ===================== Build Markov Chain =====================
markov_dict = {}
for i in range(len(words) - order):
    key = tuple(words[i:i+order])
    next_word = words[i + order]
    markov_dict.setdefault(key, []).append(next_word)

# ===================== Generate Text Function =====================
def generate_markov_text(length=500):
    start_key = random.choice(list(markov_dict.keys()))
    output = list(start_key)
    for _ in range(length):
        key = tuple(output[-order:])
        next_words = markov_dict.get(key)
        if not next_words:
            key = random.choice(list(markov_dict.keys()))
            next_word = random.choice(markov_dict[key])
        else:
            next_word = random.choice(next_words)
        output.append(next_word)
    return " ".join(output)

# ===================== Generate Massive Text =====================
output_file = "massive_text_output.txt"
total_words = 500000  # Adjust as needed
chunk_size = 500  # Words per generation chunk

with open(output_file, "w", encoding="utf-8") as f:
    generated_words = 0
    while generated_words < total_words:
        text_chunk = generate_markov_text(chunk_size)
        f.write(text_chunk + "\n\n")
        generated_words += chunk_size
        print(f"Generated {generated_words}/{total_words} words...")

print(f"Finished generating {total_words} words. Saved to {output_file}")
