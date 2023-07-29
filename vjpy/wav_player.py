"""vjpy wav player."""

from vjpy import my808kit
from playsound import playsound

my808kit_drum_paths = {}
my808kit_path = "wavs/my808kit"
for drum_ in my808kit.drums.values():
    my808kit_drum_paths[drum_.note] = f"{my808kit_path}/{drum_.name}.wav"


def play_wav(midi_msg):
    """Wav player."""
    wav_name = my808kit_drum_paths[midi_msg.note]
    print(midi_msg)
    print(wav_name)
    print("\n\n")
    playsound(wav_name)
