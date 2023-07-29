#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from moviepy.editor import VideoFileClip, CompositeVideoClip

video_name = "/home/user/Videos/python-mido-hydrogen-drum_pattern.webm"
video = VideoFileClip(video_name).subclip(0, 2)
result = CompositeVideoClip([video])
result.write_videofile(f"{video_name}_test.webm", fps=10)
