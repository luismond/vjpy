#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""midi player"""
from vjpy import MidiSequencer, PATTERNS

seq = MidiSequencer()

for n in range(8):
    for pattern_num in PATTERNS:
        seq.play_pattern(PATTERNS[pattern_num].pattern)
