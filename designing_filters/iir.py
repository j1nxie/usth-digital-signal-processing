import matplotlib.pyplot as plt
import scipy.fftpack as fft
import scipy.signal as sgl
import numpy as np

from constants import INPUT_1kHz_15kHz

def chebyshev():
    b, a = sgl.cheby1(10, 1, 15, "hp", fs=len(INPUT_1kHz_15kHz))
    w, h = sgl.freqs(b, a)

    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.xlabel("Frequency representation of Chebyshev filter")
    plt.show()

    output = sgl.filtfilt(b, a, INPUT_1kHz_15kHz)
    # output = np.convolve(INPUT_1kHz_15kHz, w)

    plt.subplot(2, 2, 1)
    plt.stem(INPUT_1kHz_15kHz, markerfmt=" ")
    plt.xlabel("Input in time domain")

    plt.subplot(2, 2, 2)
    plt.stem(fft.fft(INPUT_1kHz_15kHz), markerfmt=" ")
    plt.xlabel("Input in frequency domain")

    plt.subplot(2, 2, 3)
    plt.stem(output, markerfmt=" ")
    plt.xlabel("Output in time domain")

    plt.subplot(2, 2, 4)
    plt.stem(fft.fft(output), markerfmt=" ")
    plt.xlabel("Output in frequency domain")

    plt.show()
