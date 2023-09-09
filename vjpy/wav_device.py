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
        self.wav_examples_dir = os.path.join("vjpy", "data", "wav", "wav_examples")
        self.drumkit_note_names = drumkit_note_names
        self.drumkit_sh_names = drumkit_sh_names

    def play_wav_from_midi_msg(self, midi_msg):
        """Play a drum wav file associated with a midi message."""
        wav_path = os.path.join("vjpy", "data", "wav",
                                "drumkits", "myfunkkit",
                                f"{self.drumkit_note_names[midi_msg.note]}.wav")
        playsound(wav_path)

    def concatenate_wavs(self, shs):
        """
        Concatenate wav files.

        1. Take note shorthands.
        2. Associate them with wav file paths.
        3. Concatenate resulting wav files.
        4. Write and play resulting concatenated wav.
        """
        # msgs = [mido.Message('note_on', note=note) for note in notes]
        wav_array = []
        for short_hand in shs:
            wav_name = f"{self.drumkit_sh_names[short_hand]}.wav"
            wav_path = os.path.join("vjpy", "data", "wav",
                                    "drumkits", "myfunkkit",
                                    f"{wav_name}")
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        return np.concatenate(wav_array)

    def write_wav(self, wav_filename, wav_object):
        """Write a wav file and save it to the wav examples directory."""
        wav_path = os.path.join(self.wav_examples_dir, wav_filename)
        write(wav_path, self.sample_rate, wav_object)

    def play_wav(self, filename):
        """Play a wav file from the wav examples directory."""
        filepath = os.path.join(self.wav_examples_dir, filename)
        playsound(filepath)
