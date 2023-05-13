import matplotlib.pyplot as plt
import scipy.fftpack as fft
import scipy.signal as sgl

from constants import IMPULSE_RESPONSE


def highpass():
    plt.subplot(2, 1, 1)
    plt.stem(fft.fft(IMPULSE_RESPONSE), markerfmt=" ")

    plt.subplot(2, 1, 2)
    b, a = sgl.butter(5, 0.1, "highpass")
    impulse_filtered = sgl.filtfilt(b, a, IMPULSE_RESPONSE, axis=0)
    plt.stem(fft.fft(impulse_filtered), markerfmt=" ")
    plt.show()
