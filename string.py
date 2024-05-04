

string = input("Enter a string: ")


def frontback(string):
    front = string[:1]
    back = string[len(string)-1:]
    
    
print(frontback(string))