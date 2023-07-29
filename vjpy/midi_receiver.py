"""mido receiver."""

import mido

with mido.open_input() as inport:
    for msg in inport:
        print(msg)
