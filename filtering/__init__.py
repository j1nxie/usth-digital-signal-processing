from helpers import clrscr

from .ecg import ecg_lowpass, plot_ecg_freq
from .highpass import highpass


def filtering_init():
    clrscr()
    while True:
        print("1 - print filtered impulse response")
        print("2 - print frequency representation of ECG")
        print("3 - print filtered ECG")
        print("4 - exit")

        choice = int(input("choice: "))

        match choice:
            case 1:
                highpass()
            case 2:
                plot_ecg_freq()
            case 3:
                ecg_lowpass()
            case 4:
                break
            case _:
                print("invalid choice!")


__all__ = ["lowpass"]
