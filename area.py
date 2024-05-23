

try:
    length = float(input("Enter Length "))
    width = float(input("Enter Width "))

except ValueError:
    print("Enter Digits")







def Area(l,w):
    return l * w


def main():
    print(Area(length,width))


main()