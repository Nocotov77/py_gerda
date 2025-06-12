import json
import random

with open("words.json", "r", encoding="utf-8") as f:
    words = json.load(f)
length = int(input().strip())
word = random.choice(words[str(length)])
pattern = ["*"] * length
penalty = 0
while True:
    print("Your word " + "".join(pattern) + ". Enter the letter.")
    letter = input().strip().lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Bad input. Try once more, please.")
        continue
    if letter in word:
        for i, ch in enumerate(word):
            if ch == letter:
                pattern[i] = letter
    else:
        penalty += 1
        print("There is no such letter in the word. Check is " + str(penalty) + ".")
    if "*" not in pattern:
        print("You win! Your word is " + word.upper() + ".")
        break
    if penalty >= length:
        print("You loss! Word was " + word.upper() + ".")
        break