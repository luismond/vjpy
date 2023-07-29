"""vjpy wav player."""

from playsound import playsound
from vjpy.drumkits import my808kit_drum_paths


class WavPlayer:
    """Wav player."""

    def __init__(self):
        pass

    @staticmethod
    def play_wav_from_midi_msg(midi_msg):
        """Play a wav file associated with a midi message."""
        wav_name = my808kit_drum_paths[midi_msg.note]
        print(f"Playing: {midi_msg}\n{wav_name}\n\n")
        playsound(wav_name)

    def rewind(self):
        """Rewind."""
        obj = 1
        return obj

    def forward(self):
        """Forward."""
        obj = 1
        return obj

    def record(self):
        """Record."""
        obj = 1
        return obj
