# -*- coding: utf-8 -*-
"""vjpy controller."""
import os
import mido
from time import sleep
from vjpy import VjPyDevice#, Bar

vjpd = VjPyDevice(bpm=90)
md = vjpd.midi_device

# Play MIDI note
#md.play_note(note=38, velocity=120, duration=0)

n1 = [36, 44]
n2 = [44]
n3 = [38, 44]
n4 = [46]

ns = [n1, n2, n3, n4]

for _ in range(8):
    for n in ns:
        msgs = []
        for e in n:
            msg = mido.Message('note_on', note=e, velocity=120)
            msgs.append(msg)
        print(msgs)
        for msg in msgs:
            md.midi_out.send(msg)
        sleep(.5)

md.midi_out.close()


#%%
for _ in range(4):
    for msg in msgs:
        midi_out.send(msg)
    sleep(.5)

#%%
    midi_out.send(msg1)
    midi_out.send(msg2)
    midi_out.send(msg3)
    midi_out.send(msg4)
    midi_out.send(msg5)
    midi_out.send(msg6)
    midi_out.send(msg7)
    midi_out.send(msg8)
    sleep(.5)
    


#%%
# Play MIDI pattern
#         1.2.3.4.5.6.7.8.
patt_1 = "k h s h k h s h "
patt_2 = "k h s k k h o ss"

# #       1.2.3.4.5.6.7.8.
# hats = "....x.....x.x.x."
# kick = "x.....x.x......."
# snre = "..x.......x....."


for _ in range(4):
    md.play_pattern(patt_1)
    md.play_pattern(patt_2)

# %%  Play bar
# bar_1 = Bar(bar_num=1, patterns=['🥾👟🧂🔇', ' 👏🔇🔔🔔'])
# bar_2 = Bar(bar_num=1, patterns=['🥾🧂🧂🧂', ' 🥁🔔🪘🔔'])
# bar_3 = Bar(bar_num=1, patterns=['🥾🔇🧂🔇', ' 👏🔔🔔🔔'])
# bar_4 = Bar(bar_num=1, patterns=['🥾🧂🧂🧂', ' 🥁🪘🪘🪘'])

# bar_5 = Bar(bar_num=1, patterns=['🥾🧂🧂🧂', ' 👏🔇🐍🔇'])
# bar_6 = Bar(bar_num=1, patterns=['🥾👟🥾🥾', ' 🥾👟🥾🥾'])
# bar_7 = Bar(bar_num=1, patterns=['🥾🔇🧂🔇', ' 👏🔇🐍🔇'])
# bar_8 = Bar(bar_num=1, patterns=['🥾🔇🪵🪵', ' 🐄🐄🐄🐄'])

# for _ in range(4):
#     md.play_bar(bar_1)
#     md.play_bar(bar_2)
#     md.play_bar(bar_3)
#     md.play_bar(bar_4)
#     print('\n')
#     md.play_bar(bar_5)
#     md.play_bar(bar_6)
#     md.play_bar(bar_7)
#     md.play_bar(bar_8)
#     print('\n')

# %%Loop bar
md.loop_bar(bar_1, num_loops=4)


#%% Generate pattern
rp = md.generate_random_pattern(patt_len=8)
md.play_pattern(rp)

# %%
for msg in md.yield_midi_msg():                       # Receive MIDI msg
    wv.play_drum_wav_from_midi_msg(msg)

# %%
md.send_note(40)                                      # Send MIDI note

# %%
wv.write_concatenated_wavs(['k','h','c','h'])         # Concat wavs


# %%
soundbank_name = 'drums_03'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_videoclip = vjpd.get_videoclip(soundbank_video_path)

# %%
bpm = 140
value = .5
dur = (60/bpm)*value
print(dur)

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
patt_03 = [_,   _,   r,   _,   _,   _,   r,   _,   _,   _,   r,   _,    _,  _,   r,   r,   ]

#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_04 = [_,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   _,   u,   ]

# ...........................................................................................


# BARS
        # |1 . . .|2 . . . |3 . . . |4 . . . |5 . . . |6 . . . |7 . . . |8 . . . 
bar_01 = [patt_05, patt_01,]# patt_01, patt_01, patt_05, patt_05, patt_05, patt_05]
        # |1 . . .|2 . . . |#3 . . . |4 . . . |5 . . . |6 . . . |7 . . . |8 . . . 
bar_02 = [patt_06, patt_06,]# patt_02, patt_02, patt_06, patt_06, patt_06, patt_06]
        # |1 . . .|2 . . . |3 . . . |4 . . . |5 . . . |6 . . . |7 . . . |8 . . . 
bar_03 = [patt_03, patt_03,]# patt_03, patt_03, patt_03, patt_07, patt_03, patt_07]
        # |1 . . .|2 . . . |3 . . . |4 . . . |5 . . . |6 . . . |7 . . . |8 . . . 
bar_04 = [patt_04, patt_04]#, patt_04, patt_04, patt_04, patt_08, patt_04, patt_08]
        # |1 . . .|2 . . . |3 . . . |4 . . . |5 . . . |6 . . . |7 . . . |8 . . . 


bars_d = {
        'hats': [bar_01],#, bar_01],
        'kick_snare': [bar_02],#, bar_02],
        'cymbs': [bar_03],#, bar_03],
        'toms': [bar_04],#, bar_04]
        }

# Make and save final clip
for drum_name, bars in bars_d.items():
    beat_n = '14'
    bars = bars*8
    subclips = vjpd.get_bars_subclips(bars)
    final_clip = vjpd.concatenate_subclips(subclips)
    final_clip_path = os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', f'{drum_name}.mp4')
    vjpd.write_concatenated_subclips(final_clip, final_clip_path)


#%% compositing

clip1 = VideoFileClip(os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', 'hats.mp4'))
clip1 = clip1.fx(vfx.mirror_x)
clip1 = clip1.fx(volumex, 0.4)

clip2 = VideoFileClip(os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', 'kick_snare.mp4'))

clip3 = VideoFileClip(os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', 'cymbs.mp4'))
clip3 = clip3.fx(vfx.mirror_x)

clip4 = VideoFileClip(os.path.join(soundbank_dir_path, 'beats', f'{beat_n}', 'toms.mp4'))

video = clips_array([[clip1,],
                     [clip2,],
                     [clip3,],
                     [clip4,]])

video.resize(width=960).write_videofile("my_comp.mp4")
