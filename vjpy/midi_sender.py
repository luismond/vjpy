"""mido sender."""
import mido

PORT = mido.open_output()


class MidiSender:
    """Midi Sender."""

    def __init__(self):
        self.port = PORT

    def send(self):
        """Send."""
        for note in [36, 38, 43, 45]:
            msg = mido.Message('note_on', note=note)
            print(msg)
            self.port.send(msg)
