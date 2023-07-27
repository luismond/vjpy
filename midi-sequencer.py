# -*- coding: utf-8 -*-

import mido
from mido import Message
from time import sleep

# Enable MIDI in in Hydrogen

# Send notes to Hydrogen
outport = mido.open_output()

# Define drumkit note names
drumkit = {
    36: 'kick',
    38: 'snare',
    45: 'hat'
    }

def play_note(n, s):
    print(drumkit[n])
    msg = Message('note_on', note=n, velocity=50)
    outport.send(msg)
    sleep(s)

def kick_snare_hats():
    play_note(36, .25)
    play_note(36, .75)
    play_note(38, .50)
    play_note(45, .25)
    play_note(45, .25)
    print('\n')


def kick_snare():
    play_note(36, .25)
    play_note(36, .75)
    play_note(38, .50)
    play_note(45, .25)
    play_note(38, .25)
    print('\n')
    
def pattern1():
    kick_snare_hats()
    kick_snare_hats() 
    kick_snare_hats() 
    kick_snare() 


for n in range(0, 4):
    pattern1()


#play_note(45, .1)