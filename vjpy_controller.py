# -*- coding: utf-8 -*-
"""vjpy controller."""
import os
from moviepy.editor import CompositeVideoClip, VideoFileClip, clips_array, vfx
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
soundbank_name = 'drums_03'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_videoclip = vjpd.get_videoclip(soundbank_video_path)

dur = 0.15

b = vjpd.get_videosubclip(soundbank_videoclip, start=00.100, duration=dur) # bell
r = vjpd.get_videosubclip(soundbank_videoclip, start=03.710, duration=dur) # ride
x = vjpd.get_videosubclip(soundbank_videoclip, start=07.137, duration=dur) # china
c = vjpd.get_videosubclip(soundbank_videoclip, start=09.770, duration=dur) # crash1
d = vjpd.get_videosubclip(soundbank_videoclip, start=13.220, duration=dur) # crash2
i = vjpd.get_videosubclip(soundbank_videoclip, start=17.800, duration=dur) # hat1 pedal
j = vjpd.get_videosubclip(soundbank_videoclip, start=19.390, duration=dur) # hat2
h = vjpd.get_videosubclip(soundbank_videoclip, start=21.290, duration=dur) # hat3
y = vjpd.get_videosubclip(soundbank_videoclip, start=23.700, duration=dur) # hat5
o = vjpd.get_videosubclip(soundbank_videoclip, start=23.113, duration=dur) # hat4 open
k = vjpd.get_videosubclip(soundbank_videoclip, start=24.950, duration=dur) # kick1
l = vjpd.get_videosubclip(soundbank_videoclip, start=26.050, duration=dur) # kick2
s = vjpd.get_videosubclip(soundbank_videoclip, start=27.513, duration=dur) # snare1
z = vjpd.get_videosubclip(soundbank_videoclip, start=29.512, duration=dur) # snare2
t = vjpd.get_videosubclip(soundbank_videoclip, start=31.505, duration=dur) # tom1a
v = vjpd.get_videosubclip(soundbank_videoclip, start=34.248, duration=dur) # tom1b
w = vjpd.get_videosubclip(soundbank_videoclip, start=37.160, duration=dur) # tom2a
u = vjpd.get_videosubclip(soundbank_videoclip, start=39.010, duration=dur) # tom2b
_ = vjpd.get_videosubclip(soundbank_videoclip, start=01.500, duration=dur) # silence

# patterns and bars

# ...........................................................................................

##         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
#patt_00 = [_,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   ]

# ...........................................................................................

#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_01 = [_,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   ]

#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_02 = [k,   k,   _,   _,   s,   _,   _,   _,   _,   _,   _,   _,   z,   _,   k,   _,   ]

#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_03 = [_,   _,   r,   _,   _,   _,   r,   _,   _,   _,   r,   _,   _,   _,   r,   _,   ]

#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_04 = [_,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   u,   ]

# ...........................................................................................

#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_05 = [h,   _,   h,   _,   j,   _,   h,   _,   h,   h,   h,   _,   j,   _,   o,   _    ]

#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_06 = [k,   k,   k,   _,   s,   _,   _,   _,   _,   _,   _,   _,   z,   _,   k,   _,   ]

#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_07 = [_,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   x,   _,   _,   c,   c,   ]

#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_08 = [_,   _,   _,   _,   _,   _,   v,   v,   _,   _,   _,   _,   w,   u,   w,   u,   ]

# ...........................................................................................

# BARS
        # |1 . . .|2 . . . |3 . . . |4 . . . 
bar_01 = [patt_01, patt_05, patt_05, patt_05, patt_01, patt_05, patt_05, patt_05]
        # |1 . . . |2 . . . |3 . . . |4 . . .
bar_02 = [patt_02, patt_06, patt_02, patt_06, patt_02, patt_06, patt_02, patt_06]
        # |1 . . . |2 . . . |3 . . . |4 . . .
bar_03 = [patt_01, patt_01, patt_03, patt_03, patt_03, patt_03, patt_03, patt_03]
        # |1 . . . |2 . . . |3 . . . |4 . . .
bar_04 = [patt_01, patt_01, patt_04, patt_04, patt_04, patt_04, patt_04, patt_08]

bars_d = {
        'hats': 
            [bar_01],
        'kick_snare':
            [bar_02],
        'cymbs':
            [bar_03],
        'toms':
            [bar_04]
        }

# Make and save final clip
for drum_name, bars in bars_d.items():
    bars = bars*2
    beat_n = '14'
    print(drum_name)
    subclips = vjpd.get_bars_subclips(bars)
    final_clip = vjpd.concatenate_subclips(subclips)
    final_clip_path = os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', f'{drum_name}.mp4')
    vjpd.write_concatenated_subclips(final_clip, final_clip_path)


##%% compositing



clip1 = VideoFileClip(os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', 'hats.mp4'))
clip1 = clip1.fx(vfx.mirror_x)
clip2 = VideoFileClip(os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', 'kick_snare.mp4'))

clip3 = VideoFileClip(os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', 'cymbs.mp4'))
clip3 = clip3.fx(vfx.mirror_x)

clip4 = VideoFileClip(os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', 'toms.mp4'))

video = clips_array([[clip1, clip2],
                     [clip3, clip4]])

video.resize(width=960).write_videofile("my_comp.mp4")