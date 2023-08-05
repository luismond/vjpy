"""vjpy wav device."""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.io import wavfile
from playsound import playsound
from dotenv import load_dotenv
load_dotenv()

user = os.environ.get("USER")
my808kit_path = os.environ.get("MY_808_KIT_PATH")
sine_wave_example_filepath = os.environ.get("SINE_WAVE_EXAMPLE_FILEPATH")
snare_wav_filepath = os.environ.get("SNARE_WAV_FILEPATH")
funk_kit_path = os.environ.get("FUNK_KIT_PATH")
wav_array_c_name = os.environ.get("WAV_ARRAY_C_NAME")


def get_my808kit_paths(drumkit):
    """Get my drumkit drum paths."""
    my808kit_drum_paths = {}
    for drum_ in drumkit.drums.values():
        my808kit_drum_paths[drum_.note] = f"{my808kit_path}/{drum_.name}.wav"
    return my808kit_drum_paths


class WavDevice:
    """vjpy wav device to write, read and play wavs."""

    def __init__(self, drumkit):
        self.sound_paths = get_my808kit_paths(drumkit)

    def play_wav_from_midi_msg(self, midi_msg):
        """Play a wav file associated with a midi message."""
        wav_name = self.sound_paths[midi_msg.note]
        playsound(wav_name)

    @staticmethod
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
        write(sine_wave_example_filepath, sample_rate, data)

        # play wav
        input("This will play a loud sinewave! Continue?")
        playsound(sine_wave_example_filepath)

        # plot wav
        length = data.shape[0] / sample_rate
        time = np.linspace(0., length, data.shape[0])
        plt.plot(time, data)
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

    @staticmethod
    def test_wav_reading():
        """Read a wav, rewrite it, plot it."""
        sample_rate, data = wavfile.read(snare_wav_filepath)
        print(f"number of channels = {data.shape[1]}")
        length = data.shape[0] / sample_rate
        print(f"length = {length}s")

        # re-write read wav
        write(f"{snare_wav_filepath}_test.wav", sample_rate, data)

        #  plot read wav
        time = np.linspace(0., length, data.shape[0])
        plt.plot(time, data[:, 0], label="Left channel")
        plt.plot(time, data[:, 1], label="Right channel")
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

    @staticmethod
    def plot_sine():
        """Plot a sine with matplotlib and numpy."""
        equis_var = np.linspace(-np.pi, np.pi, 201)
        plt.plot(equis_var, np.sin(equis_var))
        plt.xlabel('Angle [rad]')
        plt.ylabel('sin(equis_var)')
        plt.axis('tight')
        plt.show()

    @staticmethod
    def write_concatenated_wavs():
        """Take a wav file, concatenate it n times, write the result."""
        sample_rate = 44100

        # read wav files, store them in an array
        wav_array = []
        for _ in range(4):
            _, data = wavfile.read(f"{funk_kit_path}/kick.wav")
            wav_array.append(data)
            _, data = wavfile.read(f"{funk_kit_path}/hat.wav")
            wav_array.append(data)
            _, data = wavfile.read(f"{funk_kit_path}/clap.wav")
            wav_array.append(data)
            _, data = wavfile.read(f"{funk_kit_path}/hat.wav")
            wav_array.append(data)

        # concatenate wavs
        wav_array_c = np.concatenate(wav_array)

        # write concatenated wav
        write(wav_array_c_name, sample_rate, wav_array_c)

        # play concatenated wav
        playsound(wav_array_c_name)
