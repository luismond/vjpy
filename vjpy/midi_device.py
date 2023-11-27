"""MIDI device class."""

import os
import time
from collections import defaultdict
import mido
import pretty_midi


class MidiDevice:
    """MIDI device."""

    def __init__(self, vj):
        self.midi_out = mido.open_output()
        self.midi_data_dir = os.path.join("vjpy", "data", "midi")
        self.note_value = vj.note_value

    def play_midi_file(self, filename):
        """Parse and play a MIDI file."""
        msgs = self.get_sorted_midi_messages(filename)
        steps = defaultdict(list)
        for msg in msgs:
            steps[msg[0]].append(msg[1])

        steps_start = list(steps.keys())
        steps_notes = list(steps.values())
        steps_duration = [(b-a) for (a, b) in list(zip(steps_start, steps_start[1:]))]

        for n, step in enumerate(steps_notes):
            for note in step:
                if note == 0:
                    msg = mido.Message("note_off", note=note, velocity=120)
                else:
                    msg = mido.Message("note_on", note=note, velocity=120)
                self.midi_out.send(msg)
            if n < len(steps_notes)-1:
                time.sleep(steps_duration[n])

    @staticmethod
    def get_sorted_midi_messages(filename):
        """Get a sorted array of midi messages."""
        midi_data = pretty_midi.PrettyMIDI(filename)
        midi_messages = []
        for instrument in midi_data.instruments:
            for note in instrument.notes:
                start = note.start
                pitch = note.pitch
                # velocity = note.velocity
                midi_messages.append([start, pitch])
        midi_messages = sorted(midi_messages, key=lambda x: (x[0], x[1]))
        return midi_messages
