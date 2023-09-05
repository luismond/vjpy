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
soundbank_name = 'drums_07'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_video = vjpd.get_videoclip(soundbank_video_path)

# VJPY!
dur = .15
h = vjpd.get_videosubclip(soundbank_video, start=00.8070 ,duration=dur) # hat
k = vjpd.get_videosubclip(soundbank_video, start=23.8760, duration=dur) # kick
s = vjpd.get_videosubclip(soundbank_video, start=03.0156, duration=dur) # snare
t = vjpd.get_videosubclip(soundbank_video, start=39.1680, duration=dur) # snare
r = vjpd.get_videosubclip(soundbank_video, start=33.4865, duration=dur) # ride
_ = vjpd.get_videosubclip(soundbank_video, start=02.6210, duration=dur) # silence


# PATTERN
#         |01   02   03   04   05   06   07   08    09   10   11   12   13   14   15   16   
patt_00 = [k,   _,   k,   _,   k,   _,   k,   _,    s,   s,   h,   h,   r,   r,   t,   t   ]

#         |01   02   03   04   05   06   07   08    09   10   11   12   13   14   15   16   
patt_01 = [k,   _,   k,   _,   s,   h,   h,   s,    k,   _,   h,   _,   s,   _,   h,   _   ]
patt_02 = [k,   h,   k,   _,   s,   _,   h,   s,    k,   _,   k,   _,   s,   k,   k,   s   ]
patt_03 = [k,   _,   k,   _,   s,   h,   h,   s,    k,   _,   h,   _,   s,   _,   h,   _   ]
patt_04 = [k,   h,   k,   _,   s,   _,   h,   s,    k,   _,   k,   _,   s,   r,   r,   r   ]

#         |01   02   03   04   05   06   07   08    09   10   11   12   13   14   15   16   
#patt_05 = [k,   _,   k,   _,   s,   _,   h,   s,    k,   _,   h,   _,   s,   _,   h,   _   ]
#patt_06 = [k,   h,   k,   _,   s,   _,   h,   s,    k,   _,   k,   _,   s,   k,   k,   s   ]
#patt_07 = [k,   _,   k,   _,   s,   _,   h,   s,    k,   _,   h,   _,   s,   _,   h,   _   ]
patt_08 = [k,   h,   h,   h,   s,   h,   h,   s,    k,   h,   h,   h,   s,   r,   r,   r   ]

#         |01   02   03   04   05   06   07   08    09   10   11   12   13   14   15   16   
patt_09 = [k,   k,   k,   _,   s,   h,   h,   h,    k,   _,   r,   r,   s,   s,   t,   t   ]


# patt_13 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
# patt_14 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
# patt_15 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
# patt_16 = [k,   _,   k,   _,   k,   _,   k,   _,   s,   s,   s,   s,   h,   h,   h,   h   ]

# patt_17 = [k,   k,   h,   _,   s,   _,   k,   _,   k,   k,   h,   _,   s,   _,   k,   _,  ]
# patt_18 = [k,   k,   h,   _,   s,   _,   k,   _,   k,   k,   h,   _,   s,   s,   x,   x,  ]


# BARS
bar_00 = [patt_00]
bar_01 = [patt_01, patt_02, patt_03, patt_02 ]
bar_02 = [patt_01, patt_02, patt_03, patt_04 ]
bar_03 = [patt_01, patt_02, patt_03, patt_08 ]
bar_04 = [patt_01, patt_02, patt_03, patt_09 ]

bars = [
        bar_00,
        bar_01, bar_02, bar_03, bar_04,
        ]

# make final clip
subclips = []
for bar_ in bars:
    for patt in bar_:
        for subclip in patt:
            subclips.append(subclip)
final_clip = vjpd.concatenate_subclips(subclips)
# save final clip
vjpd.write_concatenated_subclips(final_clip, f'{soundbank_name}_beat_1.mp4')

