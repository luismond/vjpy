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
        res = self.resolution
        note_value = self.note_values[res].relative_value / self.note_duration
        for pattern in patterns.values():
            steps = {1: [], 2: [], 3: [], 4: [],
                     5: [], 6: [], 7: [], 8: []}
            # for each hit in pattern, append it to the steps
            for key in pattern:
                for step, hit in enumerate(pattern[key]):
                    if hit == "x":
                        note = self.drumkit_sh_notes[key]
                        steps[step+1].append(note)
                        # todo: implement metronome here
            # use each note in each step to send a midi message
            for step in steps.values():
                for note in step:
                    if note == 0:
                        msg = mido.Message("note_off", note=note, velocity=120)
                    else:
                        msg = mido.Message("note_on", note=note, velocity=120)
                    self.midi_out.send(msg)
                time.sleep(note_value)

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
        """Read a Hydrogen MIDI file and get the notes of each step."""
        mid = mido.MidiFile(filename, clip=True)
        track = mid.tracks[0]
        meta_messages = track[:4]

        # Calculate BPM and note value
        tempo = meta_messages[2].tempo
        bpm = round(int(60000000)/tempo)
        note_duration = bpm/60
        note_value = .5 / note_duration

        # Get the notes of each step
        messages = track[4:-1]
        steps = defaultdict(list)
        step_ = 0
        for msg in messages:
            if msg.type == "note_on":
                step_ += msg.time
                print(step_)
                steps[step_].append(msg.note)

        # Send the MIDI messages of each step
        for step in steps.values():
            for note in step:
                if note == 0:
                    msg = mido.Message("note_off", note=note, velocity=120)
                else:
                    msg = mido.Message("note_on", note=note, velocity=120)
                self.midi_out.send(msg)
            time.sleep(note_value)

        return_obj = {
            "tempo": tempo,
            "bpm": bpm,
            "note_value": note_value,
            "messages": messages,
            "steps": steps
            }
        return return_obj
