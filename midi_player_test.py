#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""midi player test"""
from vjpy import MidiSequencer
from vjpy.patterns import pattern_1

seq = MidiSequencer()  # create sequencer instance
seq.play_pattern(pattern_1.pattern) # play sequence
