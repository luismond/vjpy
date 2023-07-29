"""mido receiver."""
import mido


class MidiReceiver:
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

    def __init__(self):
        self.inport = mido.open_input()
        print("MIDI receiver on\n")

    def receive_midi_msg(self):
        """
        Receive midi message.

        Yields
        ------
        midi_msg : mido.msg
            MIDI message from mido.

        """
        with self.inport as inport:
            for midi_msg in inport:
                yield midi_msg
