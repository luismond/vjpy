"""mido sender."""
import mido

PORT = mido.open_output()


class MidiSender:
    """Midi Sender."""

    def __init__(self):
        self.port = PORT

    def send_note(self, note):
        """Send a note."""
        msg = mido.Message('note_on', note=note)
        print(msg)
        self.port.send(msg)
