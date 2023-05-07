from helpers.clrscr import clrscr
from .systems_plot import (
    plot_freq_real_imag,
    plot_convolution,
    plot_output_conversions,
    plot_time,
    plot_frequency,
    plot_inverse,
)


def systems_init():
    clrscr()
    while True:
        print("1 - plot impulse over time")
        print("2 - plot impulse over frequency")
        print("3 - plot inverse")
        print("4 - plot output (input * impulse) over time")
        print("5 - plot output (input * impulse) over frequency")
        print("6 - exit")

        choice = int(input("choice: "))
        match choice:
            case 1:
                plot_time()
            case 2:
                plot_frequency()
                plot_freq_real_imag()
            case 3:
                plot_inverse()
            case 4:
                plot_convolution()
            case 5:
                plot_output_conversions()
            case 6:
                break
            case _:
                print("invalid choice!")


__all__ = [
    "plot_freq_real_imag",
    "plot_convolution",
    "plot_output_conversions",
    "plot_time",
    "plot_frequency",
    "plot_inverse",
]
