"""vjpy MIDI receiver."""
import mido


class MidiReceiver:
    """
    MIDI receiver.

    1. mido opens an inport where MIDI messages are received.
    2. MidiReceiver yields each MIDI message.

    Instructions:
        1. Run the receiver in a kernel.
        2. Run the sender in a separate kernel.

    Returns
    -------
    None.

    """

    def __init__(self):
        self.inport = mido.open_input()
        print("MIDI receiver is listening.\n")

    def yield_midi_msg(self):
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
