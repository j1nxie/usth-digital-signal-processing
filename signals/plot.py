import matplotlib.pyplot as plt
import sys

from constants import INPUT_1kHz_15kHz

def plot_time():
    plt.plot(INPUT_1kHz_15kHz)
    plt.show()

if __name__ == "__main__":
    try:
        plot_time()
    except KeyboardInterrupt:
        sys.exit(0)
