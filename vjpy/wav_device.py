"""MIDI device class."""
from playsound import playsound
from scipy.io import wavfile
from scipy.io.wavfile import write
import numpy as np


class WavDevice:
    """Audio device to manipulate wav files."""

    def __init__(self, drumkit_note_names, drumkit_sh_names):
        self.sample_rate = 44100
        self.drumkit_note_names = drumkit_note_names
        self.drumkit_sh_names = drumkit_sh_names

    def play_drum_wav_from_midi_msg(self, midi_msg):
        """Play a drum wav file associated with a midi message."""
        wav_name = self.drumkit_note_names[midi_msg.note]
        playsound(f"vjpy/data/wav/drumkits/myfunkkit/{wav_name}.wav")

    def write_concatenated_wavs(self, shs):  # notes):
        """
        1. Take integers or shorthands, pass them as MIDI notes to mido.

        2. Associate them with wav file paths.
        3. Concatenate resulting wav files.
        4. Write and play resulting concatenated wav.
        """
        # msgs = [mido.Message('note_on', note=note) for note in notes]
        wav_array = []
        for short_hand in shs:  # for msg in msgs:
            wav_name = f"{self.drumkit_sh_names[short_hand]}.wav"
            # wav_name = f"{self.drumkit_note_names[msg.note]}.wav"
            wav_path = f"vjpy/data/wav/drumkits/myfunkkit/{wav_name}"
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        wav_array_c = np.concatenate(wav_array)
        wav_array_c_name = "vjpy/data/wav/wav_examples/concat.wav"
        write(wav_array_c_name, self.sample_rate, wav_array_c)
        playsound(wav_array_c_name)
