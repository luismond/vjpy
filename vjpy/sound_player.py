#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sound player"""

import os
from playsound import playsound 

sound_dir = 'wavs/my808kit'
sounds = [f for f in os.listdir(sound_dir)]
sound = 'hat.wav'

for n in range(8):
    playsound(f'{sound_dir}/{sound}')
