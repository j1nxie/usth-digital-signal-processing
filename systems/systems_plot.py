import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft

from constants import IMPULSE_RESPONSE
from constants.signals import INPUT_1kHz_15kHz


def plot_time():
    plt.stem(IMPULSE_RESPONSE, markerfmt=" ")
    plt.show()


def plot_frequency():
    frequency = fft.fft(IMPULSE_RESPONSE)
    plt.xlabel("Impulse response over frequency", fontsize=10)
    plt.stem(frequency, markerfmt=" ")
    plt.show()


def plot_freq_real_imag():
    frequency = fft.fft(IMPULSE_RESPONSE)

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

    plt.show()


def plot_inverse():
    frequency = fft.fft(IMPULSE_RESPONSE)
    inverse = fft.ifft(frequency)
    plt.stem(inverse, markerfmt=" ")
    plt.show()


def plot_convolution():
    plt.subplot(2, 1, 1)
    output_convolve = np.convolve(INPUT_1kHz_15kHz, IMPULSE_RESPONSE)
    plt.stem(output_convolve, markerfmt=" ")
    plt.xlabel("Output calculated by convolution")

    plt.subplot(2, 1, 2)
    output_multiplication = fft.ifft(
        fft.fft(
            np.pad(INPUT_1kHz_15kHz, (0, len(output_convolve) - len(INPUT_1kHz_15kHz)))
        )
        * fft.fft(
            np.pad(IMPULSE_RESPONSE, (0, len(output_convolve) - len(IMPULSE_RESPONSE)))
        )
    )
    plt.stem(output_multiplication, markerfmt=" ")
    plt.xlabel("Output calculated by multiplication")
    plt.show()


def plot_output_conversions():
    output = np.convolve(INPUT_1kHz_15kHz, IMPULSE_RESPONSE)

    output_freq = fft.fft(output)
    plt.stem(output_freq, markerfmt=" ")
    plt.show()

    plt.subplot(2, 2, 1)
    output_real = np.real(output_freq)
    plt.stem(output_real, markerfmt=" ")
    plt.xlabel("Real part", fontsize=10)

    plt.subplot(2, 2, 2)
    output_imag = np.imag(output_freq)
    plt.stem(output_imag, markerfmt=" ")
    plt.xlabel("Imaginary part", fontsize=10)

    plt.subplot(2, 2, 3)
    output_magnitude = np.abs(output_freq)
    plt.stem(output_magnitude, markerfmt=" ")
    plt.xlabel("Magnitude", fontsize=10)

    plt.subplot(2, 2, 4)
    output_phase = np.angle(output_freq)
    plt.stem(output_phase, markerfmt=" ")
    plt.xlabel("Phase", fontsize=10)

    plt.show()
