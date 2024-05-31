# import curses
# from curses import wrapper

def main(stdcsr):
    stdcsr.clear()
    stdcsr.addstr(10,10, "Hello World")
    stdcsr.refresh()
    stdcsr.getch()


wrapper(main)