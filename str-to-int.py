from curses.ascii import isdigit


def isDig(num):
    for n in num:
        if n == ".":
            num = float(num)
        else:
            num = float(num)
    return isdigit(num) # type: ignore


print(isDig("90.8"))

