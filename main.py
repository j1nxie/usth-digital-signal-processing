import sys

from designing_filters import designing_filters_init
from filtering import filtering_init
from helpers.clrscr import clrscr
from numpy_tutorial import numpy_tutorial
from signals import signals_init
from systems import systems_init


def main():
    clrscr()
    while True:
        print("1 - numpy tutorial")
        print("2 - signals")
        print("3 - systems")
        print("4 - filtering")
        print("5 - designing filters")
        print("6 - exit")

        choice = int(input("choice: "))
        match choice:
            case 1:
                numpy_tutorial()
            case 2:
                signals_init()
            case 3:
                systems_init()
            case 4:
                filtering_init()
            case 5:
                designing_filters_init()
            case 6:
                break
            case _:
                print("invalid choice!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
