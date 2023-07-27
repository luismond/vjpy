# # -*- coding: utf-8 -*-
"""vjpy midi sequencer"""

from pydantic import BaseModel
import mido
from mido import Message
from time import sleep


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
    repr_: str


# GLOBAL VARIABLES
OUTPORT = mido.open_output()


def get_bpm(int_):
    return int_/60


BPM = get_bpm(120)


NOTE_VALUES = {
    '1': NoteValue(name='whole_note', relative_value=1.0, repr_='1'),
    '1/2': NoteValue(name='half_note', relative_value=0.5, repr_='1/2'),
    '1/4': NoteValue(name='quarter_note', relative_value=0.25, repr_='1/4'),
    '1/8': NoteValue(name='eigth_note', relative_value=0.125, repr_='1/8'),
    '1/16': NoteValue(name='sixteenth_note', relative_value=0.0625, repr_='1/16'),
    '1/32': NoteValue(name='thirty-second_note', relative_value=0.03125, repr_='1/32')
    }


DRUMKIT = Drumkit(
    name='TR808EmulationKit',
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


PATTERNS = {
    '1': Pattern(
        timeline='01..|02..|03..|04..|',
        pattern='|kk..|s.hh|kk..|swht|'),
    '2': Pattern(
        timeline='05..|06..|07..|08..|',
        pattern='|kk..|s.hh|kk..|s.gg|'),
    '3': Pattern(
        timeline='09..|10..|11..|12..|',
        pattern='|kk..|s.hh|kk..|swht|'),
    '4': Pattern(
        timeline='13..|14..|15..|16..|',
        pattern='|k.h.|s.h.|k.h.|cccc|')
    }


class MidiSequencer:
    def __init__(self):
        pass

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
        note_value = NOTE_VALUES['1/4'].relative_value / BPM
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


seq = MidiSequencer()

for pattern_num in PATTERNS:
    seq.play_pattern(PATTERNS[pattern_num].pattern)

"""
verbs: play, record
nouns: beat, note, silence, message, pattern, drum, value
"""