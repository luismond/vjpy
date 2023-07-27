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


def play_note(note, sleep_=0, velocity=50):
    msg = Message('note_on',  note=note, velocity=velocity)
    outport.send(msg)
    sleep(sleep_)


def play_drum(drumkit, drum_name, sleep_):
    drum_note = drumkits[drumkit][drum_name]
    print(f'{drum_note} - {drum_name} - {sleep_}')
    play_note(drum_note, sleep_=sleep_)


def drum_pattern(drumkit):
    print('note - name - sleep')
    play_drum(drumkit, 'kick', .25)
    play_drum(drumkit, 'kick', .75)
    play_drum(drumkit, 'snare', .50)
    play_drum(drumkit, 'hat', .25)
    play_drum(drumkit, 'hat', .25)
    play_drum(drumkit, 'kick', .25)
    play_drum(drumkit, 'kick', .75)
    play_drum(drumkit, 'snare', .50)
    play_drum(drumkit, 'hat', .25)
    play_drum(drumkit, 'clave', .25)
    play_drum(drumkit, 'kick', .25)
    play_drum(drumkit, 'kick', .75)
    play_drum(drumkit, 'snare', .50)
    play_drum(drumkit, 'hat', .25)
    play_drum(drumkit, 'conga', .25)
    play_drum(drumkit, 'kick', .25)
    play_drum(drumkit, 'kick', .75)
    play_drum(drumkit, 'snare', .50)
    play_drum(drumkit, 'hat', .25)
    play_drum(drumkit, 'tom', .25)


drum_pattern('TR808EmulationKit')
