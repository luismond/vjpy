# # -*- coding: utf-8 -*-
# """MIDI sequencer."""

from pydantic import BaseModel
import mido
from mido import Message
from time import sleep

# # todo: define proper note durations
# # todo: define fundamental sequencing objects and actions

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


# Dicts

note_relative_values = {
    'whole_note': 1,
    'half_note': .5,
    'quarter_note': .25,
    'eigth_note': .125,
    'sixteenth_note': 0.0625,
    'thirty_second_note': 0.03125
    }


# Objects

drumkit = Drumkit(
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

outport = mido.open_output()

patterns = {
    '1': Pattern(
        timeline='01...|02...|03...|04...|',
        pattern='kk..|s.hh|kk..|swht|'),
    '2': Pattern(
        timeline='05...|06...|07...|08...|',
        pattern='kk..|s.hh|kk..|s.gg|'),
    '3': Pattern(
        timeline='09...|10...|11...|12...|',
        pattern='kk..|s.hh|kk..|swht|'),
    '4': Pattern(
        timeline='13...|14...|15...|16...|',
        pattern='kk..|shhh|kk..|ssss|')
    }

# Functions


def play_note(note, duration=0, velocity=50):
    msg = Message('note_on',  note=note, velocity=velocity)
    outport.send(msg)
    sleep(duration)


def play_drum(drum_name, duration):
    drum_note = drumkit.drums[drum_name].note
    play_note(note=drum_note, duration=duration)


def play_silence(duration=0):
    sleep(duration)


def parse_pattern(pattern):
    note_value = note_relative_values['quarter_note']
    for hit in pattern:
        if hit != '|':
            if hit == '.':
                play_silence(duration=note_value)
            else:
                drum_name = [
                    drum.name for drum in drumkit.drums.values()
                    if drum.short_hand == hit
                    ][0]
                print(drum_name)
                play_drum(drum_name=drum_name, duration=note_value)


for pattern_n in patterns:
    parse_pattern(patterns[pattern_n].pattern)

# %% to_do

# def tempo():
#     pass


# # def pattern():
# #     pass


# # def instrument():
# #     pass


# # def note_values():
# #     pass


# # def bpm():
# #     "rel value 1 = 1 second = 60 bpm"
# #     pass


# # def time_signature():
# #     "beats / note value (4/4)"
# #     pass


# # def beat():
# #     pass


# # def velocity():
# #     pass


# def time_line():
#     pass


# bar_resolutions = {
#     '1/4': '....',
#     '1/8': '........',
#     '1/16': '................'
#     }


# def get_bar(resolution):
#     return bar_resolutions[resolution]


# bar = get_bar('1/4')

# bars = [get_bar('1/4') for n in range(4)]


# short_hand = dict()
# for d in drumkit.drums:
#     short_hand[drumkit.drums[d].short_hand] = drumkit.drums[d].name
