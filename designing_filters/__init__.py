from helpers.clrscr import clrscr

from .fir import fir
from .highpass_filter import highpass_filter
from .iir import iir


def designing_filters_init():
    clrscr()
    while True:
        print("1 - FIR")
        print("2 - IIR")
        print("3 - applying a highpass filter to input")
        print("4 - exit")

        choice = int(input("choice: "))

        match choice:
            case 1:
                fir()
            case 2:
                iir()
            case 3:
                highpass_filter()
            case 4:
                break
            case _:
                print("invalid choice!")
