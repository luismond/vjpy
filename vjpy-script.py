# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 03:29:00 2023

@author: luism
"""

import rtmidi
midiout = rtmidi.MidiOut()
midiout.open_virtual_port('foo')
note_on = [0x90, 60, 112]
midiout.send_message(note_on)