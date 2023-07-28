#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from moviepy.editor import *


video = VideoFileClip("python-mido-hydrogen-drum_pattern.webm").subclip(0, 2)
result = CompositeVideoClip([video])
result.write_videofile("python-mido-hydrogen-drum_pattern_.webm", fps=10)
