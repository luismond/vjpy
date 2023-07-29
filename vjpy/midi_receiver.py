"""mido receiver."""

import mido
from playsound import playsound


midi_wav_dict = {
    60: "wavs/my808kit/snare2.wav"
    }


def play_wav(midi_msg):
    """Wav player."""
    wav_name = midi_wav_dict[midi_msg.note]
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
