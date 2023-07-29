"""mido receiver."""

import mido

with mido.open_input() as inport:
    for msg in inport:
        print(msg)
        #  if succesful:
        #  "note_on channel=0 note=60 velocity=64 time=0"
