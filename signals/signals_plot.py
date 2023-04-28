import matplotlib.pyplot as plt
import scipy.fftpack as fft
import numpy as np

from constants import INPUT_1kHz_15kHz


def plot_time():
    plt.plot(INPUT_1kHz_15kHz)


def plot_frequency():
    plt.subplot(5, 1, 1)
    frequency = fft.fft(INPUT_1kHz_15kHz)
    plt.plot(frequency)

    plt.subplot(5, 1, 2)
    real = np.real(frequency)
    plt.plot(real)

    plt.subplot(5, 1, 3)
    imag = np.imag(frequency)
    plt.plot(imag)

    plt.subplot(5, 1, 4)
    magnitude = np.abs(frequency)
    plt.plot(magnitude)

    plt.subplot(5, 1, 5)
    phase = np.angle(frequency)
    plt.plot(phase)


def plot_inverse():
    frequency = fft.fft(INPUT_1kHz_15kHz)
    inverse = fft.ifft(frequency)
    plt.plot(inverse)
