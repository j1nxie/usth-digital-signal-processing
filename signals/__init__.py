import matplotlib.pyplot as plt
from .signals_plot import plot_time, plot_frequency, plot_inverse


def signals_init():
    while True:
        print("1 - plot input over time")
        print("2 - plot input over frequency")
        print("3 - plot inverse")
        print("4 - exit")

        choice = int(input("choice: "))
        match choice:
            case 1:
                plot_time()
                plt.show()
            case 2:
                plot_frequency()
                plt.show()
            case 3:
                plot_inverse()
                plt.show()
            case 4:
                break
            case _:
                print("invalid choice!")


__all__ = ["plot_time", "plot_frequency", "plot_inverse", "signals_init"]
