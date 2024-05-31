
# with open("Demo.txt", "w")as f:
#     data = f.write("This is cs50 Harvard University Intro \n Computer Science Courses is this")
#     print(data)

with open("Demo.txt", "r") as f:
    data = f.read()
    print(data)

    n = []
    for ind, c  in enumerate(data):
        if c == 's':
            n.append(ind)

    print(n)

            