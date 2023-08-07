"""Wav utils to learn more about the wav format."""

import os
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()

SINE_WAVE_EXAMPLE_FILEPATH = os.environ.get("SINE_WAVE_EXAMPLE_FILEPATH")
SNARE_WAV_FILEPATH = os.environ.get("SNARE_WAV_FILEPATH")


def create_sine_wave():
    """
    Write and plot a wave.

    100Hz sine wave, sampled at 44100Hz.
    Write to 16-bit PCM, Mono.
    Plot with matplotlib

    linspace returns num evenly spaced samples,
    calculated over the interval [start, stop].
    Todo: find out how to change the duration.
    """
    # write wav
    sample_rate = 44100
    fs_var = 300  # Hz
    amplitude = np.iinfo(np.int16).max
    time = np.linspace(start=0., stop=1., num=sample_rate)
    data = amplitude * np.sin(2 * np.pi * fs_var * time)
    write(SINE_WAVE_EXAMPLE_FILEPATH, sample_rate, data)

    # play wav
    # input("This will play a loud sinewave! Continue?")
    # playsound(SINE_WAVE_EXAMPLE_FILEPATH)

    # plot wav
    length = data.shape[0] / sample_rate
    time = np.linspace(0., length, data.shape[0])
    plt.plot(time, data)
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()


def test_wav_reading():
    """Read a wav, rewrite it, plot it."""
    sample_rate, data = wavfile.read(SNARE_WAV_FILEPATH)
    print(f"number of channels = {data.shape[1]}")
    length = data.shape[0] / sample_rate
    print(f"length = {length}s")

    # re-write read wav
    write(f"{SNARE_WAV_FILEPATH}_test.wav", sample_rate, data)

    #  plot read wav
    time = np.linspace(0., length, data.shape[0])
    plt.plot(time, data[:, 0], label="Left channel")
    plt.plot(time, data[:, 1], label="Right channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()


def plot_sine():
    """Plot a sine with matplotlib and numpy."""
    equis_var = np.linspace(-np.pi, np.pi, 201)
    plt.plot(equis_var, np.sin(equis_var))
    plt.xlabel('Angle [rad]')
    plt.ylabel('sin(equis_var)')
    plt.axis('tight')
    plt.show()


create_sine_wave()
test_wav_reading()
plot_sine()
