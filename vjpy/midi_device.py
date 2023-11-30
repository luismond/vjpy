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
        """
        Parse and play a MIDI file.

        Hydrogen setup:
            MIDI driver: ALSA
            Input: Midi through port-0
            Output: none
            Use output note as input note: True
        """
        msgs = self.get_sorted_midi_messages(filename)
        steps = self.get_midi_steps(msgs)

        for n, step in enumerate(list(steps.values())):
            for note in step["notes"]:
                if note == 0:
                    msg = mido.Message("note_off", note=note, velocity=120)
                else:
                    msg = mido.Message("note_on", note=note, velocity=120)
                self.midi_out.send(msg)
            if n < len(list(steps.values()))-1:
                time.sleep(step["duration"])
        time.sleep(1)

    def get_midi_steps(self, msgs):
        steps = {msg[0]: {"notes": []} for msg in msgs}
        for n, msg in enumerate(msgs):
            steps[msg[0]]["notes"].append(msg[1])
            if n < len(msgs)-1:
                steps[msg[0]]["duration"] = msgs[n+1][0]-msg[0]
            else:
                steps[msg[0]]["duration"] = self.note_value

        return steps

    @staticmethod
    def get_sorted_midi_messages(filename):
        """Get a sorted array of midi messages."""
        midi_data = pretty_midi.PrettyMIDI(filename)
        midi_messages = []
        for instrument in midi_data.instruments:
            for note in instrument.notes:
                midi_messages.append([note.start, note.pitch])
        midi_messages = sorted(midi_messages, key=lambda x: (x[0], x[1]))
        return midi_messages