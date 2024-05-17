

active = True

while active:
    sentence = input("Enter a sentence")
    if sentence.startswith('w') or sentence.startswith('h'):
        print("Question")
    elif sentence.endswith("") or sentence.endswith("."):
        print("Positive")

    n = input("Enter Q to terminate")
    if n == 'q':
        active = False
    else:
        pass