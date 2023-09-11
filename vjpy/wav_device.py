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

    def concatenate_wavs(self, wav_list):
        """Concatenate an array of wavs."""
        wav_array = []
        for wav_path in wav_list:
            # wav_path = os.path.join(f"{self.wav_dir}",
            #                         "drumkits",
            #                         f"{drumkit}",
            #                         f"{wav_name}")
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        print("\nWav file concatenation completed.")
        return np.concatenate(wav_array)

    def mix_wavs(self, wav_list):
        """Mix an array of wavs."""
        wav_array = []
        for wav_path in wav_list:
            # wav_path = os.path.join(f"{self.wav_dir}",
            #                         "drumkits",
            #                         f"{drumkit}",
            #                         f"{wav_name}")
            _, data = wavfile.read(wav_path)
            wav_array.append(data)

        wav_mixed = wav_array[0]
        for wav in wav_array[1:]:
            wav_mixed += wav
        return wav_mixed

    def mix_wav_patterns(self, patterns):
        """Concatenate and mix a drum pattern."""
        d = {"h": "hat1.wav",
             "k": "kick1.wav",
             "c": "clap1.wav",
             "_": "silence.wav"}
        drumkit = "myfunkkit"
        for pattern in patterns.values():
            steps = {1: [], 2: [], 3: [], 4: [],
                     5: [], 6: [], 7: [], 8: []}
            # for each hit in pattern, append it to the steps
            for key in pattern:
                for step, hit in enumerate(pattern[key]):
                    if hit == "x":
                        note = d[key]
                        steps[step+1].append(note)

            # for each step, mix the corresponding wavs
            wavs_mixed = []
            for step_n, step in steps.items():
                wav_list = [os.path.join(
                    self.wav_dir, "drumkits", drumkit, wn) for wn in step]
                wav_mixed = self.mix_wavs(wav_list)
                wavs_mixed.append(wav_mixed)

            # concatenate the steps
            wav_concat = np.concatenate(wavs_mixed)
            return wav_concat
