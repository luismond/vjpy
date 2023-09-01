"""vjpy controller."""

import os
from vjpy import VjPyDevice
vjpd = VjPyDevice()

# %% Wav concatenation
pattern = [
    #1...2...3...4...
    'k','h','c','h',
    'k','k','c','h'
    ]
vjpd.write_concatenated_wavs(pattern)

# %% Pattern playing
print("\nPlaying a pattern.")
vjpd.play_pattern(
    #12341234
    "khchkkch"
    )

# %% Bar playing
from vjpy import Bar

print("\nPlaying a bar.")
vjpd.play_bar(vjpd.bar_example)

vjpd.play_bar(
    Bar(
        bar_num=1, patterns=[
            # 1...2...3...4...
             'k...k...k...k...'
            ]
        )
    )

#%% Bar looping
print("\nLooping a bar.")
vjpd.loop_bar(vjpd.bars_example[0], num_loops=2)

# Bars looping
print("\nLooping a sequence of bars.")
vjpd.loop_bars(vjpd.bars_example, num_loops=1)

# Random pattern generation
print("\nPlaying random pattern.")
rp = vjpd.generate_random_pattern(patt_len=4)
vjpd.play_pattern(rp)

# %% Test midi receiving
for msg in vjpd.yield_midi_msg():
    vjpd.play_drum_wav_from_midi_msg(msg)

# %% Test midi sending
vjpd.send_note(40)

# %% Test video sequencing


# video-sound banks directory
sound_banks_path = os.path.join('vjpy_media', 'sound_banks')
sound_bank_path = os.path.join(sound_banks_path, 'robodrum_bank_3')

# video-sound bank file names
sound_bank_video_filenames = sorted(
    [
     video_fn for video_fn in os.listdir(
         sound_bank_path
         ) if video_fn.endswith('mp4')])

# beats directory
beats_path = os.path.join('vjpy_media', 'beats')
beat_name = 'videobeat-012'
if not beat_name in os.listdir(beats_path):
    os.mkdir(os.path.join(beats_path, beat_name))

beat_path = os.path.join(beats_path, beat_name)


#%% make video clip objects from sound bank video files

video_clips = {}
for video_filename in sound_bank_video_filenames:
    video_path = os.path.join(sound_bank_path, video_filename)
    video_clip = vjpd.get_video_clip(video_path)
    video_clips[video_filename[:-4]] = video_clip


# %% video clips corresponding to 1 drum sound each

fn = 'robodrum_bank_3_clean'

dur = 0.14

b = vjpd.get_video_subclip(video_clips[fn], start=00.100, duration=dur) # bell
r = vjpd.get_video_subclip(video_clips[fn], start=03.710, duration=dur) # ride

x = vjpd.get_video_subclip(video_clips[fn], start=07.137, duration=dur) # china
c = vjpd.get_video_subclip(video_clips[fn], start=09.770, duration=dur) # crash1
d = vjpd.get_video_subclip(video_clips[fn], start=13.220, duration=dur) # crash2

i = vjpd.get_video_subclip(video_clips[fn], start=17.800, duration=dur) # hat1 pedal
j = vjpd.get_video_subclip(video_clips[fn], start=19.390, duration=dur) # hat2
h = vjpd.get_video_subclip(video_clips[fn], start=21.290, duration=dur) # hat3
y = vjpd.get_video_subclip(video_clips[fn], start=23.700, duration=dur) # hat5
o = vjpd.get_video_subclip(video_clips[fn], start=23.113, duration=dur) # hat4 open


k = vjpd.get_video_subclip(video_clips[fn], start=24.950, duration=dur) # kick1
l = vjpd.get_video_subclip(video_clips[fn], start=26.050, duration=dur) # kick2

s = vjpd.get_video_subclip(video_clips[fn], start=27.513, duration=dur) # snare1
z = vjpd.get_video_subclip(video_clips[fn], start=29.512, duration=dur) # snare2

t = vjpd.get_video_subclip(video_clips[fn], start=31.505, duration=dur) # tom1a
v = vjpd.get_video_subclip(video_clips[fn], start=34.248, duration=dur) # tom1b
w = vjpd.get_video_subclip(video_clips[fn], start=37.160, duration=dur) # tom2a
u = vjpd.get_video_subclip(video_clips[fn], start=39.010, duration=dur) # tom2b

_ = vjpd.get_video_subclip(video_clips[fn], start=01.500, duration=dur) # silence


# %% patterns and bars

# PATTERNS

         # 1.2.3.4.
patt_01 = [k,_,h,_ ] # bar 01
patt_02 = [s,_,h,_ ]
patt_03 = [k,_,h,h ]
patt_04 = [z,_,h,_ ]

         # 1.2.3.4.
patt_05 = [k,_,h,_ ] # bar 02
patt_06 = [s,_,h,_ ]
patt_07 = [k,k,h,h ]
patt_08 = [z,_,o,_ ]

         # 1.2.3.4.
patt_09 = [k,_,h,_ ] # bar 03
patt_10 = [s,_,h,s ]
patt_11 = [k,_,h,h ]
patt_12 = [z,_,h,_ ]

         # 1.2.3.4.
patt_13 = [k,_,h,_ ] # bar 04
patt_14 = [s,_,h,h ]
patt_15 = [w,_,u,_ ]
patt_16 = [s,z,s,z ]

         # 1.2.3.4.
patt_17 = [k,_,h,k ] # bar 05
patt_18 = [s,_,h,b ]
patt_19 = [k,_,h,_ ]
patt_20 = [z,_,h,x ]

         # 1.2.3.4.
patt_21 = [k,_,h,k ] # bar 06
patt_22 = [s,_,h,b ]
patt_23 = [k,_,h,_ ]
patt_24 = [z,_,h,c ]

         # 1.2.3.4.
patt_25 = [k,_,h,k ] # bar 07
patt_26 = [s,_,h,b ]
patt_27 = [k,_,h,_ ]
patt_28 = [z,_,h,d ]

         # 1.2.3.4.
patt_29 = [k,_,h,k ] # bar 08
patt_30 = [s,_,h,b ]
patt_31 = [k,_,h,_ ]
patt_32 = [z,s,w,u ]


# BARS
        # |1 . . . |2 . . . |3 . . . |4 . . . 
bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
bar_02 = [patt_05, patt_06, patt_07, patt_08 ]
bar_03 = [patt_09, patt_10, patt_11, patt_12 ]
bar_04 = [patt_13, patt_14, patt_15, patt_16 ]

        # |1 . . . |2 . . . |3 . . . |4 . . . 
bar_05 = [patt_17, patt_18, patt_19, patt_20 ]
bar_06 = [patt_21, patt_22, patt_23, patt_24 ]
bar_07 = [patt_25, patt_26, patt_27, patt_28 ]
bar_08 = [patt_29, patt_30, patt_31, patt_32 ]


bars = [
        bar_01, bar_02, bar_03, bar_04,
        bar_01, bar_02, bar_03, bar_04,
        bar_05, bar_06, bar_07, bar_08,
        bar_05, bar_06, bar_07, bar_08,
        ]


# make final clip
subclips = []
for bar_ in bars:
    for patt in bar_:
        for subclip in patt:
            subclips.append(subclip)

final_clip = vjpd.concatenate_subclips(subclips)


# save final clip
iteration = '005'
video_result_path = os.path.join(
    beats_path,
    beat_name,
    f'{beat_name}_{iteration}.mp4'
    )
vjpd.write_concatenated_subclips(final_clip, video_result_path)


# %%


# video-sound banks directory
sound_banks_path = os.path.join('vjpy_media', 'sound_banks')
sound_bank_path = os.path.join(sound_banks_path, 'cello_bank_1')

# video-sound bank file names
sound_bank_video_filenames = sorted(
    [
     video_fn for video_fn in os.listdir(
         sound_bank_path
         ) if video_fn.endswith('mp4')])

# beats directory
beats_path = os.path.join('vjpy_media', 'beats')
beat_name = 'videobeat-013'
if not beat_name in os.listdir(beats_path):
    os.mkdir(os.path.join(beats_path, beat_name))

beat_path = os.path.join(beats_path, beat_name)


#%% make video clip objects from sound bank video files

video_clips = {}
for video_filename in sound_bank_video_filenames:
    video_path = os.path.join(sound_bank_path, video_filename)
    video_clip = vjpd.get_video_clip(video_path)
    video_clips[video_filename[:-4]] = video_clip


# %% video clips corresponding to 1 sound each

fn = 'cello_bank_1_clean'
# beat duration aprox: 1.1s

dur = 1.1

a = vjpd.get_video_subclip(video_clips[fn], start=01.015, duration=dur)
b = vjpd.get_video_subclip(video_clips[fn], start=03.205, duration=dur)
c = vjpd.get_video_subclip(video_clips[fn], start=04.271, duration=dur)
# d = vjpd.get_video_subclip(video_clips[fn], start=07.710, duration=dur)



# patterns and bars

# PATTERNS

         # 1.2.3.4.
patt_01 = [a,a,b,b]
patt_02 = [a,a,c,c]

# BARS
       # |1 . . . |2 . . . |3 . . . |4 . . . 
bar_01 = [patt_01, patt_01, patt_02, patt_02 ]

bars = [bar_01]


# make final clip
subclips = []
for bar_ in bars:
    for patt in bar_:
        for subclip in patt:
            subclips.append(subclip)

final_clip = vjpd.concatenate_subclips(subclips)


# save final clip
iteration = '001'
video_result_path = os.path.join(
    beats_path,
    beat_name,
    f'{beat_name}_{iteration}.mp4'
    )
vjpd.write_concatenated_subclips(final_clip, video_result_path)
print(f'\nResult written to {video_result_path}.')