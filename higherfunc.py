


def Shout(text):
    return text.upper()

def Wispher(text):
    return text.lower()


def greet(func):
    greeting = func("Hi I am created By a function")
    print(greeting)

greet(Shout)
greet(Wispher)