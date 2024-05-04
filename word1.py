from word import words
import sys

for word in words:
    if word == "achiever":
        print(f"Found word {word}")
        sys.exit(0)
    else:
        print("Not found")
        sys.exit(1)

