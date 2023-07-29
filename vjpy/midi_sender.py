"""mido sender."""
import time
import mido

# First, open receiver.

PORT = mido.open_output()
MSG = mido.Message('note_on', note=60)

# message sending test
for n in range(8):
    PORT.send(mido.Message('note_on', note=36))
    PORT.send(mido.Message('note_on', note=38))
    PORT.send(mido.Message('note_on', note=43))
    PORT.send(mido.Message('note_on', note=45))
    time.sleep(.05)
