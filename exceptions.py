import sys

try:
    x = int(input("Enter X "))
    y = int(input("Enter Y "))
except ValueError:
    print("Enter Numbers")
    sys.exit(1)


try:
    result = x/y

    print(f"{x}/{y} = {result}")

except ZeroDivisionError:
    print("Infinity not divide by :)")
    sys.exit(1)