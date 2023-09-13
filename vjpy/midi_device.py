"""MIDI device class."""


import os
import time
import random
from collections import defaultdict
import mido


class MidiDevice:
    """MIDI device."""

    def __init__(self,
                 bpm,
                 resolution,
                 note_values,
                 drumkit_sh_notes,
                 ):
        self.bpm = bpm
        self.midi_in = mido.open_input()
        self.midi_out = mido.open_output()
        self.resolution = resolution
        self.note_values = note_values
        self.note_duration = self.bpm/60
        self.note_value = self.note_values[resolution].relative_value / self.note_duration
        self.drumkit_sh_notes = drumkit_sh_notes
        self.midi_data_dir = os.path.join("vjpy", "data", "midi")

    def yield_midi_msg(self):
        """Yield MIDI messages from a MIDI in port."""
        for midi_msg in self.midi_in:
            yield midi_msg

    def play_pattern(self, pattern):
        """Play a sequence of notes."""
        res = self.resolution
        note_value = self.note_values[res].relative_value / self.note_duration
        for beat in pattern:
            if beat == ' ':
                time.sleep(note_value)
            else:
                drum_note = self.drumkit_sh_notes[beat]
                self.play_note(note=drum_note, duration=note_value)

    def play_patterns(self, patterns):
        """
        Play a list of patterns with the following shape.

            'pattern_01':
                {
                    #      1   2   3   4   5   6   7   8
                    "h": ["x","x","x","x","x","_","x","_", ], # hi-hat
                    "k": ["x","_","_","_","x","_","x","_", ], # kick
                    "s": ["_","_","x","_","_","x","_","x", ]  # snare
                    },
        """
        for pattern in patterns.values():
            steps = {1: [], 2: [], 3: [], 4: [],
                     5: [], 6: [], 7: [], 8: []}
            for key in pattern:
                for step, hit in enumerate(pattern[key]):
                    if hit == "x":
                        note = self.drumkit_sh_notes[key]
                        steps[step+1].append(note)
            self.play_steps(steps)

    def play_note(self, note, velocity=50, duration=0):
        """Send a MIDI note."""
        msg = mido.Message("note_on", note=note, velocity=velocity)
        self.midi_out.send(msg)
        time.sleep(duration)

    def generate_random_pattern(self, patt_len):
        """Generate_random_pattern."""
        short_hands = ["k", "q", "s", "c", "t", "h", "o", "r", "v", "w"]
        # emoji = ["👟", "🥾", "🥁", "👏", "🪘", "🔔", "🐍", "🧂", "🪵", "🐄"]
        random_pattern = []
        for _ in range(patt_len):
            random_pattern.append(random.choice(short_hands))
        return ''.join(random_pattern)

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
                     144: [42],         # step 4
                     192: [42, 36],     # ...
                     240: [42],
                     288: [42, 38],
                     336: [46]})
        """
        for step in steps.values():
            for note in step:
                if note == 0:
                    msg = mido.Message("note_off", note=note, velocity=120)
                else:
                    msg = mido.Message("note_on", note=note, velocity=120)
                self.midi_out.send(msg)
            time.sleep(self.note_value)
