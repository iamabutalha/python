import sys

sentence = input("Enter a sentence : ")


for char in sentence.lower():
    if sentence.startswith('w') or sentence.startswith('h') and sentence.endswith('?'):
        print('Interogative Sentence ')
        sys.exit(0)
    elif 'not' not in sentence:
        print('Sentence is Positive')
        sys.exit(0)
    elif 'not' in sentence:
        print('Negative sentence')
        sys.exit(0)