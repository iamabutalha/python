#Function with dynamic params


from traceback import print_tb


def Average(*args):
    p =  sum(args)/len(args)
    return p



print(Average(90,89,765,524,24,334))
