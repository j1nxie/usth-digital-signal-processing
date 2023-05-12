import matplotlib.pyplot as plt
import scipy.fftpack as fft
import scipy.signal as sgl
import numpy as np

from constants import INPUT_1kHz_15kHz


def chebyshev():
    b, a = sgl.cheby1(10, 1, 15, "low", fs=len(INPUT_1kHz_15kHz))
    w, h = sgl.freqs(b, a)

    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.xlabel("Frequency representation of Chebyshev filter")
    plt.show()

    output = sgl.filtfilt(b, a, INPUT_1kHz_15kHz)

    plt.subplot(2, 2, 1)
    plt.plot(INPUT_1kHz_15kHz, "r.", ms=2)
    plt.xlabel("Input in time domain")

    plt.subplot(2, 2, 2)
    plt.plot(np.abs(fft.fft(INPUT_1kHz_15kHz)))
    plt.xlabel("Input in frequency domain")

    plt.subplot(2, 2, 3)
    plt.plot(output, "r.", ms=2)
    plt.xlabel("Output in time domain")

    plt.subplot(2, 2, 4)
    plt.plot(np.abs(fft.fft(output)))
    plt.xlabel("Output in frequency domain")

    plt.show()
