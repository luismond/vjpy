"""MIDI device class."""

import os
import time
from collections import defaultdict
import mido


class MidiDevice:
    """MIDI device."""

    def __init__(self, vj):
        self.midi_out = mido.open_output()
        self.midi_data_dir = os.path.join("vjpy", "data", "midi")
        self.note_value = vj.note_value

    def play_midi_file(self, filename):
        """Parse and play a MIDI file."""
        steps = self.parse_midi_file(filename)
        for step in steps.values():
            for note in step:
                if note == 0:
                    msg = mido.Message("note_off", note=note, velocity=120)
                else:
                    msg = mido.Message("note_on", note=note, velocity=120)
                self.midi_out.send(msg)
            time.sleep(self.note_value)

    def parse_midi_file(self, filename):
        """Read a Hydrogen MIDI file and get the notes of each step."""
        mid = mido.MidiFile(filename, clip=True)
        track = mid.tracks[0]
        messages = track[4:-1]
        steps = defaultdict(list)
        step = 0
        for msg in messages:
            if msg.type == "note_on":
                step += msg.time
                steps[step].append(msg.note)
        return steps
