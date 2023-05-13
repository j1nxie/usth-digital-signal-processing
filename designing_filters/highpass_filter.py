import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft
import scipy.signal as sgl

from constants import INPUT_1kHz_15kHz


def highpass_filter():
    b, a = sgl.butter(10, 15, "highpass", fs=len(INPUT_1kHz_15kHz))
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
