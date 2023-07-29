"""mido sender."""
import mido

PORT = mido.open_output()

# Send messages
for note in [36, 38, 43, 45]:
    msg = mido.Message('note_on', note=note)
    print(msg)
    PORT.send(msg)
