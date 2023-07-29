"""mido receiver."""

import mido
from playsound import playsound
from vjpy import my808kit

my808kit_drum_paths = {}
my808kit_path = "wavs/my808kit"
for drum_ in my808kit.drums.values():
    my808kit_drum_paths[drum_.note] = f"{my808kit_path}/{drum_.name}.wav"


def play_wav(midi_msg):
    """Wav player."""
    wav_name = my808kit_drum_paths[midi_msg.note]
    print(wav_name)
    playsound(wav_name)


def init_midi_receiver():
    """
    MIDI receiver.

    mido opens an inport where messages are received.
    messages are passed to a wav playing function.

    Instructions:
        1. Run the receiver in a kernel.
        2. Run the sender in a separate kernel.

    Returns
    -------
    None.

    """
    print("MIDI receiver on")
    with mido.open_input() as inport:
        for msg in inport:
            print(msg)
            play_wav(msg)


init_midi_receiver()
