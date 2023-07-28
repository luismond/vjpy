#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""midi player test"""

from vjpy import MidiSequencer, Pattern
from pydantic import BaseModel

seq = MidiSequencer()

patt = Pattern(
    bars=   '1...2...3...4...5...6...7...8...',
    beats=  '................................',
    pattern='k.h.c.h.k.h.c.h.k.h.c.h.k.h.c.h.'
    )

for n in range(4):
    print(patt.bars)
    print(patt.pattern)
    seq.play_pattern(patt.pattern)

