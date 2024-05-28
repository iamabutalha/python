from traceback import print_tb


def terminal(cmd):
    n = ""
    if cmd.lower() == 'ls':
        n = "All files list"
    elif cmd.lower() == 'mkdir':
        n = "Create new folder"
    elif cmd.lower() == 'cd':
        n = 'Enter to the directory'
    elif cmd.lower() == 'code':
        n = 'code that file '
    else:
        n = "The term is not recognized as the name of a cmdlet, \
            function, script file, or operable "

    return n


cmd = input("Enter a command")

print(terminal(cmd))