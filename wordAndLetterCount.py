
sentence = input('Enter a sentence : ')

num = [char for char in sentence]
sentenceWords = sentence.split()

count = 0
LetterCount = 0

for word in sentenceWords:
    count += 1

for num in sentence:
    LetterCount += 1

print(num)
print(count)
print(LetterCount)
print(sentenceWords)

