"""mido sender."""
import mido
import time

# First, open receiver.

# sender kernel
PORT = mido.open_output()
MSG = mido.Message('note_on', note=60)

# message sending test
for n in range(10):
    PORT.send(MSG)
    time.sleep(.1)
