# -*- coding: utf-8 -*-
"""vjpy controller."""
import os
from vjpy import VjPyDevice, Bar
vjpd = VjPyDevice()
# vjpd.write_concatenated_wavs(['k','h','c','h'])         # Concat wavs
# vjpd.play_pattern("khchkkch")                           # Play pattern
# vjpd.play_bar(vjpd.bar_example)                         # Play bar
# vjpd.loop_bar(vjpd.bars_example[0], num_loops=2)        # Loop bar
# vjpd.loop_bars(vjpd.bars_example, num_loops=1)          # Loop bars
# rp = vjpd.generate_random_pattern(patt_len=4)           # Generate pattern
# vjpd.play_pattern(rp)
# for msg in vjpd.yield_midi_msg():                       # Receive MIDI msg
#     vjpd.play_drum_wav_from_midi_msg(msg)
# vjpd.send_note(40)                                      # Send MIDI note

#%%
soundbank_name = 'drums_06'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_videoclip = vjpd.get_videoclip(soundbank_video_path)

dur = .3

# chunks
a = vjpd.get_videosubclip(soundbank_videoclip, start=02.1120, duration=dur)
b = vjpd.get_videosubclip(soundbank_videoclip, start=02.6340, duration=dur)
c = vjpd.get_videosubclip(soundbank_videoclip, start=03.1240, duration=dur)
d = vjpd.get_videosubclip(soundbank_videoclip, start=03.6450, duration=dur)

e = vjpd.get_videosubclip(soundbank_videoclip, start=04.1694, duration=dur)
f = vjpd.get_videosubclip(soundbank_videoclip, start=04.6664, duration=dur)
g = vjpd.get_videosubclip(soundbank_videoclip, start=05.1600, duration=dur)
h = vjpd.get_videosubclip(soundbank_videoclip, start=05.6600, duration=dur)

i = vjpd.get_videosubclip(soundbank_videoclip, start=06.1514, duration=dur)
j = vjpd.get_videosubclip(soundbank_videoclip, start=06.6787, duration=dur)
k = vjpd.get_videosubclip(soundbank_videoclip, start=07.1909, duration=dur)
l = vjpd.get_videosubclip(soundbank_videoclip, start=07.6833, duration=dur)

m = vjpd.get_videosubclip(soundbank_videoclip, start=08.1850, duration=dur)
n = vjpd.get_videosubclip(soundbank_videoclip, start=08.7360, duration=dur)


# PATTERNS 
          # 12345678
patt_01 = [a,b,c,d]
patt_02 = [a,a,c,d]
patt_03 = [a,b,c,d]
patt_04 = [a,a,c,e]

patt_05 = [a,b,c,d]
patt_06 = [a,a,c,d]
patt_07 = [a,b,c,d]
patt_08 = [a,a,g,h]

patt_09 = [g,h,g,h]


# BARS
        # |1 . . . |2 . . . |3 . . . |4 . . . 
bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
bar_02 = [patt_05, patt_06, patt_07, patt_08 ]
#bar_03 = [patt_05, patt_06, patt_09, patt_09 ]


bars = [
        bar_01, bar_01, bar_01, bar_02,
        bar_01, bar_01, bar_01, bar_02,]
        # bar_01, bar_02, bar_01, bar_03,
        # ]

# Make and save final clip
subclips = vjpd.get_bars_subclips(bars)
final_clip = vjpd.concatenate_subclips(subclips)
final_clip_path = os.path.join(soundbank_dir_path, 'beats', 'beat_13.mp4')
vjpd.write_concatenated_subclips(final_clip, final_clip_path)


#%%

from moviepy.editor import CompositeVideoClip, VideoFileClip, clips_array, vfx

soundbank_name = 'drums_05'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')

#
clip1 = VideoFileClip(soundbank_video_path)
clip2 = clip1.fx( vfx.mirror_x)
clip3 = clip1.fx( vfx.mirror_y)
clip4 = clip3.fx( vfx.mirror_y)

final_clip = clips_array([[clip1, clip2],
                          [clip3, clip4]])
final_clip.resize(width=960).write_videofile("my_stack.mp4")

#%%

video = CompositeVideoClip([clip1,clip2,clip3,clip4], size=(720,460))
video.resize(width=960).write_videofile("my_comp.mp4")
#%%
video = CompositeVideoClip([clip1,
                           clip2.set_position((45,150)),
                           clip3.set_position((90,100))])
video.resize(width=960).write_videofile("my_comp.mp4")