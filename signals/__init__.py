from .plot import plot_time

def signals_init():
    while True:
        print("1 - plot input over time")
        print("2 - exit")

        choice = int(input("choice: "))
        match choice:
            case 1:
                plot_time()
            case 2:
                break
            case _:
                print("invalid choice!")

__all__ = ["plot_time", "signals_init"]
