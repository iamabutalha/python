#Higher Order function




def create_adder(x):
    def adder(y):
        return x + y
    return adder



add_15 = create_adder(2)


print(add_15(20))
