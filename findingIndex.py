



def FindOccurance(text, Choice):
    newlist = []
    for ind, ch in enumerate(text):
        if ch == Choice:
            newlist.append(ind)

    return newlist


text1 = input("Enter Any Sentence ")

Choice1 = 'a'


print(FindOccurance(text1, Choice1))


    
        