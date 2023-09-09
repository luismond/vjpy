"""MIDI device class."""

import mido
import time
import random


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
        self.drumkit_sh_notes = drumkit_sh_notes

    def yield_midi_msg(self):
        """Yield MIDI messages from a MIDI in port."""
        for midi_msg in self.midi_in:
            yield midi_msg

    # def play_pattern(self, pattern):
    #     """Play a sequence of notes."""
    #     res = self.resolution
    #     note_value = self.note_values[res].relative_value / self.note_duration
    #     print(pattern+"\n")
    #     # print("\t"+pattern)
    #     for beat in pattern:
    #         # if beat != ' ':
    #         if beat == ' ':
    #             self.play_silence(duration=note_value)
    #         else:
    #             drum_note = self.drumkit_sh_notes[beat]
    #             self.play_note(note=drum_note, duration=note_value)

    def play_patterns(self, patterns):
        """
        Play a set of patterns with the following shape:

            'pattern_01':
                {
                    #      1   2   3   4   5   6   7   8   
                    "h": ["x","x","x","x","x","_","x","_", ], # hi-hat
                    "k": ["x","_","_","_","x","_","x","_", ], # kick
                    "s": ["_","_","x","_","_","x","_","x", ]  # snare
                    },
        """
        # drums = {"h": 44, "k": 36, "s": 38}
        for pattern in patterns.values():
            steps = {1: [], 2: [], 3: [], 4: [],
                     5: [], 6: [], 7: [], 8: []}
            # for each hit in pattern, append it to the steps
            for key in pattern:
                for step, hit in enumerate(pattern[key]):
                    if hit == "x":
                        note = self.drumkit_sh_notes[key]
                        steps[step+1].append(note)
            # use each note in each step to send a midi message
            for step in steps.values():
                for note in step:
                    if note == 0:
                        msg = mido.Message('note_off', note=note, velocity=120)
                    else:
                        msg = mido.Message('note_on', note=note, velocity=120)
                    self.midi_out.send(msg)
                time.sleep(.25)
        # self.midi_out.close()

    def play_note(self, note, velocity=50, duration=0):
        """Send a MIDI note."""
        msg = mido.Message('note_on', note=note, velocity=velocity)
        self.midi_out.send(msg)
        time.sleep(duration)
        # self.midi_out.close()

    # def play_bar(self, bar_):
    #     """Play a sequence of patterns."""
    #     self.play_pattern("".join(bar_.patterns))

    @staticmethod
    def play_silence(duration=0):
        """Play a silence of n duration."""
        time.sleep(duration)

    # def loop_bar(self, bar_, num_loops=1):
    #     """Iterate over a bar_."""
    #     for _ in range(num_loops):
    #         self.play_bar(bar_)

    # def loop_bars(self, bars, num_loops=1):
    #     """Iterate over a sequence of bars_."""
    #     for _ in range(num_loops):
    #         for bar_ in bars:
    #             self.loop_bar(bar_)

    def generate_random_pattern(self, patt_len):
        """Generate_random_pattern."""
        abbvs = ["👟", "🥾", "🥁", "👏", "🪘", "🔔", "🐍", "🧂", "🪵", "🐄"]
        random_pattern = []
        for _ in range(patt_len):
            random_pattern.append(random.choice(abbvs))
        return ''.join(random_pattern)
