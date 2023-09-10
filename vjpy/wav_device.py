"""MIDI device class."""
import os
from playsound import playsound
from scipy.io import wavfile
from scipy.io.wavfile import write
import numpy as np


class WavDevice:
    """Audio device to manipulate wav files."""

    def __init__(self):
        self.sample_rate = 44100
        self.wav_dir = os.path.join("vjpy", "data", "wav")

    def play_wav(self, filepath):
        """Play a wav file."""
        print(f"\nPlaying {filepath} wav file.")
        playsound(filepath)

    def write_wav(self, filepath, wav_object):
        """Write a wav file."""
        write(filepath, self.sample_rate, wav_object)
        print(f"\nWav file written to {filepath}.")

    def concatenate_wavs(self, wav_list, drumkit):
        """Concatenate an array of wavs."""
        wav_array = []
        for wav_name in wav_list:
            wav_path = os.path.join(f"{self.wav_dir}",
                                    "drumkits",
                                    f"{drumkit}",
                                    f"{wav_name}")
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        print("\nWav file concatenation completed.")
        return np.concatenate(wav_array)

    def mix_wavs(self, wav_list, drumkit):
        """Mix an array of wavs."""
        wav_array = []
        for wav_name in wav_list:
            wav_path = os.path.join(f"{self.wav_dir}",
                                    "drumkits",
                                    f"{drumkit}",
                                    f"{wav_name}")
            _, data = wavfile.read(wav_path)
            wav_array.append(data)

        wav_mixed = wav_array[0]
        for wav in wav_array[1:]:
            wav_mixed += wav
        return wav_mixed
