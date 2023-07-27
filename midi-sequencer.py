# # -*- coding: utf-8 -*-
"""vjpy midi sequencer."""

from pydantic import BaseModel
import mido
from mido import Message
from time import sleep

# GLOBAL VARIABLES
OUTPORT = mido.open_output()
BPM = 120

# Data Classes


class Pattern(BaseModel):
    timeline: str
    pattern: str


class Drumkit(BaseModel):
    name: str
    drums: dict


class Drum(BaseModel):
    name: str
    note: int
    short_hand: str


class NoteValue(BaseModel):
    name: str
    relative_value: float


DRUMKIT = Drumkit(
    name='TR808EmulationKit',  # choose this drumkit in Hydrogen
    drums={
        'kick': Drum(name='kick', note=36, short_hand='k'),
        'snare': Drum(name='snare', note=38, short_hand='s'),
        'clap': Drum(name='clap', note=40, short_hand='c'),
        'tom': Drum(name='tom', note=43, short_hand='t'),
        'hat': Drum(name='hat', note=45, short_hand='h'),
        'conga': Drum(name='conga', note=49, short_hand='g'),
        'clave': Drum(name='clave', note=50, short_hand='v'),
        'cowbell': Drum(name='cowbell', note=51, short_hand='w'),
        }
    )


class MidiSequencer:
    def __init__(self):
        self.BPM = BPM
        self.note_duration = self.BPM/60

    def play_note(self, note, duration=0, velocity=50):
        msg = Message('note_on',  note=note, velocity=velocity)
        OUTPORT.send(msg)
        sleep(duration)

    def play_drum(self, drum_name, duration=0):
        drum_note = DRUMKIT.drums[drum_name].note
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
                        drum.name for drum in DRUMKIT.drums.values()
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


seq = MidiSequencer()


# Pattern example
# PATTERNS = {
#     '1': Pattern(
#         timeline='01..|02..|03..|04..|',
#         pattern='|kk..|s.hh|kk..|swht|'),
#     '2': Pattern(
#         timeline='05..|06..|07..|08..|',
#         pattern='|kk..|s.hh|kk..|s.gg|'),
#     '3': Pattern(
#         timeline='09..|10..|11..|12..|',
#         pattern='|kk..|s.hh|kk..|swht|'),
#     '4': Pattern(
#         timeline='13..|14..|15..|16..|',
#         pattern='|k.h.|s.h.|k.h.|cccc|')
#     }


PATTERNS = {
    '1': Pattern(
        timeline='....|....|....|....|',
        pattern='|k.h.|k.h.|k.h.|k.h.|')
    }


for n in range(8):
    for pattern_num in PATTERNS:
        seq.play_pattern(PATTERNS[pattern_num].pattern)
