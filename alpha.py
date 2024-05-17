

"""A Simple program to count all 
the words in a sentence by using dictionary"""


sentence = input("Enter a sentence: ")


cout = {}


# Firts we will take every charter in sentence
for char in sentence:
# We will check if the character exit in the empty dict if yes
# then we will increase it value by 1
    if char in cout:
        cout[char] += 1

# If not exits the we will count it only once
    else:
        cout[char] = 1

print(cout)
    