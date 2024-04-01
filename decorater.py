def announce(name):
    def wrapper():
        print("Function is about to run ")
        name()
        print("Done running code ")
    return wrapper    


@announce
def hello():
    print("Hello World ")


hello()   