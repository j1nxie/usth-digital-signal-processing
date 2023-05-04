import sys
from helpers.clrscr import clrscr
from numpy_tutorial import numpy_tutorial
from signals import signals_init


def main():
    clrscr()
    while True:
        print("1 - numpy tutorial")
        print("2 - signals")
        print("3 - exit")

        choice = int(input("choice: "))
        match choice:
            case 1:
                numpy_tutorial()
            case 2:
                signals_init()
            case 3:
                break
            case _:
                print("invalid choice!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
