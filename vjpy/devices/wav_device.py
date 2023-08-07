"""vjpy wav device."""

import os
import numpy as np
import mido
from scipy.io.wavfile import write
from scipy.io import wavfile
from playsound import playsound
from dotenv import load_dotenv
load_dotenv()

DRUMKIT_PATH = os.environ.get("LOCAL_DRUMKIT_PATH")
WAV_ARRAY_C_NAME = os.environ.get("WAV_ARRAY_C_NAME")


class WavDevice:
    """vjpy wav device to write, read and play wavs."""

    def __init__(self, drumkit):
        self.sample_rate = 44100
        self.drumkit = drumkit

    def play_drum_wav_from_midi_msg(self, drum_midi_notes_to_names, midi_msg):
        """Play a drum wav file associated with a midi message."""
        wav_name = drum_midi_notes_to_names[midi_msg.note]
        playsound(DRUMKIT_PATH+"/"+wav_name+".wav")

    def write_concatenated_wavs(self, drum_midi_notes_to_names, notes):
        """Take a wav file, concatenate it, write the result."""
        wav_array = []
        msgs = [mido.Message('note_on', note=note) for note in notes]
        for msg in msgs:
            wav_path = DRUMKIT_PATH + "/" + drum_midi_notes_to_names[msg.note] + ".wav"
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        wav_array_c = np.concatenate(wav_array)
        write(WAV_ARRAY_C_NAME, self.sample_rate, wav_array_c)
        playsound(WAV_ARRAY_C_NAME)
