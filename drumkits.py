#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""vjpy/hydrogen drumkits"""

from data_classes import Drumkit, Drum

TR808EmulationKit = Drumkit(
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
