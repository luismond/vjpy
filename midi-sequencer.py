# -*- coding: utf-8 -*-
"""MIDI sequencer."""

import mido
from mido import Message
from time import sleep

# Open port
outport = mido.open_output()

# Define drumkits
drumkits = {
    'TR808EmulationKit':
        {
             'kick': 36,
             'snare': 38,
             'clap': 40,
             'tom': 43,
             'hat': 45,
             'conga': 49,
             'clave': 50,
             'cowbell': 51
            }
        }

#todo: define proper note durations

#todo: define fundamental sequencing objects and actions

def tempo():
    pass

def pattern():
    pass

def instrument():
    pass

def note_values():
    pass


def bpm():
    "rel value 1 = 1 second = 60 bpm"
    pass

# def drumkit():
#     pass

def time_signature():
    "beats / note value (4/4)"
    pass

def beat():
    value = 1
    pass

def velocity():
    pass


def play_note(note, sleep_=0, velocity=50):
    msg = Message('note_on',  note=note, velocity=velocity)
    outport.send(msg)
    sleep(sleep_)

def play_silence(duration=0):
    sleep(duration)

def play_drum(drumkit, drum_name, sleep_):
    drum_note = drumkits[drumkit][drum_name]
    print(f'{drum_note} - {drum_name} - {sleep_}')
    play_note(drum_note, sleep_=sleep_)


note_relative_values = {
    'whole_note': 1,
    'half_note': .5,
    'quarter_note': .25,
    'eigth_note': .125,
    'sixteenth_note': 0.0625,
    'thirty_second_note': 0.03125
    }


def time_line():
    pass


# bar_resolutions = {
#     '1/4': '....',
#     '1/8': '........',
#     '1/16': '................'
#     }

# def get_bar(resolution):
#     return bar_resolutions[resolution]

# bar = get_bar('1/4')

# bars = [get_bar('1/4') for n in range(4)]

patt = 'kk..s.hh'

short_hand = {
    'k': 'kick',
    's': 'snare',
    'h': 'hat',
    '.': 'silence'
    }

drumkit = 'TR808EmulationKit'
    
def parse(patt):
    note_value = note_relative_values['quarter_note']
    for i in patt:
        drum_name = short_hand[i]
        if short_hand[i] == 'silence':
            play_silence(duration=note_value)
        else:
            play_drum(drumkit, drum_name, note_value)

for n in range(4):
    parse(patt)
