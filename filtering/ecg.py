import matplotlib.pyplot as plt
import scipy.fftpack as fft
import scipy.signal as sgl

from constants import ECG


def plot_ecg_freq():
    plt.stem(fft.fft(ECG), markerfmt=" ")
    plt.show()


def ecg_lowpass():
    sos = sgl.butter(5, 10, "low", fs=len(ECG), output="sos", analog=False)
    filtered_ecg = sgl.sosfilt(sos, ECG)
    plt.stem(filtered_ecg, markerfmt=" ")
    plt.show()
