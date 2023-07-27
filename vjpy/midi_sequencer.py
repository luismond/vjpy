# # -*- coding: utf-8 -*-
"""vjpy midi sequencer."""

import mido
from mido import Message
from time import sleep
from vjpy import NoteValue
from vjpy import TR808EmulationKit

# GLOBAL VARIABLES
OUTPORT = mido.open_output()
BPM = 120


class MidiSequencer:
    def __init__(self):
        self.BPM = BPM
        self.note_duration = self.BPM/60

    def play_note(self, note, duration=0, velocity=50):
        msg = Message('note_on',  note=note, velocity=velocity)
        OUTPORT.send(msg)
        sleep(duration)

    def play_drum(self, drum_name, duration=0):
        drum_note = TR808EmulationKit.drums[drum_name].note
        self.play_note(note=drum_note, duration=duration)

    @staticmethod
    def play_silence(duration=0):
        sleep(duration)

    def play_pattern(self, pattern):
        res = '1/4'  # resolution
        note_value = self.note_values[res].relative_value / self.note_duration
        for beat in pattern:
            if beat != '|':
                if beat == '.':
                    self.play_silence(duration=note_value)
                else:
                    drum_name = [
                        drum.name for drum in TR808EmulationKit.drums.values()
                        if drum.short_hand == beat
                        ][0]  # simplify
                    self.play_drum(drum_name=drum_name, duration=note_value)

    @property
    def note_values(self):
        note_values = {
            '1': NoteValue(name='whole_note', relative_value=1.0),
            '1/2': NoteValue(name='half_note', relative_value=0.5),
            '1/4': NoteValue(name='quarter_note', relative_value=0.25),
            '1/8': NoteValue(name='eigth_note', relative_value=0.125),
            '1/16': NoteValue(name='sixteenth_note', relative_value=0.0625),
            '1/32': NoteValue(name='thirty-second_note', relative_value=0.03125)
            }
        return note_values
