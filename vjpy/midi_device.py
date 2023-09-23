"""MIDI device class."""

import os
import time
from collections import defaultdict
import mido


class MidiDevice:
    """MIDI device."""

    def __init__(self, vj):
        self.midi_in = mido.open_input()
        self.midi_out = mido.open_output()
        self.bpm = vj.bpm
        self.note_value = vj.note_value
        self.drumkit_sh_notes = vj.drumkit_sh_notes
        self.midi_data_dir = os.path.join("vjpy", "data", "midi")

    def yield_midi_msg(self):
        """Yield MIDI messages from a MIDI in port."""
        for midi_msg in self.midi_in:
            yield midi_msg

    def play_note(self, note, velocity=50, duration=0):
        """Send a MIDI note."""
        msg = mido.Message("note_on", note=note, velocity=velocity)
        self.midi_out.send(msg)
        time.sleep(duration)

    def play_midi_file(self, filename):
        """Parse and play a MIDI file."""
        steps = self.parse_midi_file(filename)
        self.play_steps(steps)

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

    def play_steps(self, steps):
        """
        Play MIDI notes from a "steps" dictionary.

        defaultdict(<class 'list'>,
                    {0: [42, 36],       # step 1
                     48: [42],          # step 2
                     96: [42, 38],      # step 3
                     144: [42]}         # step 4
        """
        for step in steps.values():
            for note in step:
                if note == 0:
                    msg = mido.Message("note_off", note=note, velocity=120)
                else:
                    msg = mido.Message("note_on", note=note, velocity=120)
                self.midi_out.send(msg)
            time.sleep(self.note_value)
