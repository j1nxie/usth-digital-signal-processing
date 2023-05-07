import matplotlib.pyplot as plt
import scipy.fftpack as fft
import numpy as np

from constants import INPUT_1kHz_15kHz


def plot_time():
    plt.stem(INPUT_1kHz_15kHz, markerfmt=" ")


def plot_frequency():
    frequency = fft.fft(INPUT_1kHz_15kHz)
    plt.stem(frequency, markerfmt=" ")
    plt.title("Signal in frequency domain", fontsize=10)
    plt.show()

    plt.subplot(2, 2, 1)
    real = np.real(frequency)
    plt.xlabel("Real part", fontsize=10)
    plt.stem(real, markerfmt=" ")

    plt.subplot(2, 2, 2)
    imag = np.imag(frequency)
    plt.xlabel("Imaginary part", fontsize=10)
    plt.stem(imag, markerfmt=" ")

    plt.subplot(2, 2, 3)
    magnitude = np.abs(frequency)
    plt.xlabel("Magnitude", fontsize=10)
    plt.stem(magnitude, markerfmt=" ")

    plt.subplot(2, 2, 4)
    phase = np.angle(frequency)
    plt.xlabel("Phase", fontsize=10)
    plt.stem(phase, markerfmt=" ")


def plot_inverse():
    frequency = fft.fft(INPUT_1kHz_15kHz)
    inverse = fft.ifft(frequency)
    plt.stem(inverse, markerfmt=" ")
