import random
from word import words
import string
from hangman_visual import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)
    while '-' in words or '' in words:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word) #letters in word
    alphabet  = set(string.ascii_uppercase)
    used_letter = set() #what the user had guess
    lives = 6

    while len(word_letter) > 0 and lives > 0:
        #letter used
        # ' '.join (['a', 'b','cd'] -> [a b cd])
        print('You have',lives,' lives left. You have Used these letter: ',' '.join(used_letter))

        # What Current Word of the list (i.e W-RD)
        word_list = [letter if letter in used_letter else '-' for letter in word ]
        print(lives_visual_dict[lives])
        print('Current word : ',''.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the Word ")
        elif user_letter in used_letter:
            print("You have already Used this letter ")
        else:
            print("Invalid Character")
    
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died")
    else:
        print(f"Yaay You gussed the word {word} !! ")

hangman()


