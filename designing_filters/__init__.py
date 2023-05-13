from helpers.clrscr import clrscr

from .fir import fir
from .iir import iir


def designing_filters_init():
    clrscr()
    while True:
        print("1 - FIR")
        print("2 - IIR")
        print("3 - exit")

        choice = int(input("choice: "))

        match choice:
            case 1:
                bartlett()
            case 2:
                chebyshev()
            case 3:
                break
            case _:
                print("invalid choice!")


__all__ = ["bartlett", "chebyshev"]
