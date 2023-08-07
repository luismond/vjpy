"""vjpy wav device."""

import os
import numpy as np

from scipy.io.wavfile import write
from scipy.io import wavfile
from playsound import playsound
from dotenv import load_dotenv
load_dotenv()

LOCAL_DRUMKIT_PATH = os.environ.get("LOCAL_DRUMKIT_PATH")
WAV_ARRAY_C_NAME = os.environ.get("WAV_ARRAY_C_NAME")


class WavDevice:
    """vjpy wav device to write, read and play wavs."""

    def __init__(self, drumkit):
        self.sample_rate = 44100
        self.drumkit = drumkit

    def play_drum_wav_from_midi_msg(self, midi_msg):
        """Play a drum wav file associated with a midi message."""
        local_drumkit_paths = {}
        for drum in self.drumkit.drums.values():
            local_drumkit_paths[drum.note] = f"{LOCAL_DRUMKIT_PATH}/{drum.name}.wav"
        wav_name = local_drumkit_paths[midi_msg.note]
        playsound(wav_name)

    def write_concatenated_wavs(self, sound_names):
        """Take a wav file, concatenate it, write the result."""
        wav_array = []
        for _ in range(4):
            for sound_name in sound_names:
                wav_name = f"{LOCAL_DRUMKIT_PATH}/{sound_name}.wav"
                _, data = wavfile.read(wav_name)
                wav_array.append(data)

        wav_array_c = np.concatenate(wav_array)  # concatenate wavs
        write(WAV_ARRAY_C_NAME, self.sample_rate, wav_array_c)  # write concatenated wav
        playsound(WAV_ARRAY_C_NAME)  # play concatenated wav
