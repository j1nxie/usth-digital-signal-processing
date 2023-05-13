import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fft
import scipy.signal as sgl
from scipy.io import wavfile


def audio_processing():
    freq_sample, sig_audio = wavfile.read("constants/audio.wav")

    print("- Shape of signal: ", sig_audio.shape)
    print("- Signal datatype: ", sig_audio.dtype)
    print(
        "- Signal duration: ",
        round(sig_audio.shape[0] / float(freq_sample), 2),
        "seconds",
    )

    pow_audio_signal = sig_audio / np.power(2, 15)
    pow_audio_signal = pow_audio_signal[:100]
    time_axis = 1000 * np.arange(0, len(pow_audio_signal), 1) / float(freq_sample)

    plt.subplot(2, 1, 1)
    plt.plot(time_axis, np.abs(fft.fft(pow_audio_signal)))
    plt.xlabel("Original audio signal")

    plt.subplot(2, 1, 2)
    noise = np.random.normal(0, 1 * np.sqrt(1000 / 2), 100) / np.power(2, 15)
    audio_with_noise = pow_audio_signal + noise
    plt.plot(time_axis, np.abs(fft.fft(audio_with_noise)))
    plt.xlabel("Audio signal with noise")
    plt.show()

    plt.subplot(2, 1, 1)
    plt.plot(time_axis, np.abs(fft.fft(audio_with_noise)))
    plt.xlabel("Audio signal with noise")

    plt.subplot(2, 1, 2)
    denoised = sgl.wiener(audio_with_noise)
    plt.plot(time_axis, np.abs(fft.fft(denoised)))
    plt.xlabel("Audio signal after noise removal")
    plt.show()
