"""MIDI device class."""
import os
from playsound import playsound
from scipy.io import wavfile
from scipy.io.wavfile import write
import numpy as np


class WavDevice:
    """Audio device to manipulate wav files."""

    def __init__(self, drumkit_note_names, drumkit_sh_names):
        self.sample_rate = 44100
        self.wav_dir = os.path.join("vjpy", "data", "wav")
        self.drumkit_note_names = drumkit_note_names
        self.drumkit_sh_names = drumkit_sh_names

    def play_wav_from_midi_msg(self, midi_msg):
        """Play a wav file associated with a midi message."""
        wav_path = os.path.join(f"{self.wav_dir}",
                                "drumkits", "myfunkkit",
                                f"{self.drumkit_note_names[midi_msg.note]}.wav")
        playsound(wav_path)

    def concatenate_wavs(self, shs):
        """
        Concatenate wav files.

        1. Take instrument_note shorthands.
        2. Associate them with a wav file path.
        3. Concatenate resulting wav files.
        """
        wav_array = []
        for short_hand in shs:
            wav_path = os.path.join(f"{self.wav_dir}",
                                    "drumkits", "myfunkkit",
                                    f"{self.drumkit_sh_names[short_hand]}.wav")
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        print("\nWav file concatenation completed.")
        return np.concatenate(wav_array)

    def write_wav(self, wav_filename, wav_object):
        """Write a wav file to the wav dir."""
        wav_path = os.path.join(self.wav_dir, "examples", wav_filename)
        write(wav_path, self.sample_rate, wav_object)
        print(f"\nWav file written to {wav_path}.")

    def play_wav(self, filename):
        """Play a wav file from the wav dir."""
        filepath = os.path.join(self.wav_dir, "examples", filename)
        print(f"\nPlaying {filename} wav file.")
        playsound(filepath)
