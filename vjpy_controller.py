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

b = vjpd.get_video_subclip(video_clips[fn], start=00.10, duration=dur) # bell
r = vjpd.get_video_subclip(video_clips[fn], start=03.71, duration=dur) # ride

x = vjpd.get_video_subclip(video_clips[fn], start=07.12, duration=dur) # china
c = vjpd.get_video_subclip(video_clips[fn], start=09.71, duration=dur) # crash1
d = vjpd.get_video_subclip(video_clips[fn], start=13.19, duration=dur) # crash2

h = vjpd.get_video_subclip(video_clips[fn], start=17.91, duration=dur) # hat1
i = vjpd.get_video_subclip(video_clips[fn], start=19.39, duration=dur) # hat2
j = vjpd.get_video_subclip(video_clips[fn], start=21.29, duration=dur) # hat3
y = vjpd.get_video_subclip(video_clips[fn], start=23.70, duration=dur) # hat5
o = vjpd.get_video_subclip(video_clips[fn], start=23.12, duration=dur) # hat4 open


k = vjpd.get_video_subclip(video_clips[fn], start=24.95, duration=dur) # kick1
l = vjpd.get_video_subclip(video_clips[fn], start=26.05, duration=dur) # kick2

s = vjpd.get_video_subclip(video_clips[fn], start=27.51, duration=dur) # snare1
z = vjpd.get_video_subclip(video_clips[fn], start=29.55, duration=dur) # snare2

t = vjpd.get_video_subclip(video_clips[fn], start=31.46, duration=dur) # tom1a
v = vjpd.get_video_subclip(video_clips[fn], start=34.23, duration=dur) # tom1b
w = vjpd.get_video_subclip(video_clips[fn], start=37.16, duration=dur) # tom2a
u = vjpd.get_video_subclip(video_clips[fn], start=38.98, duration=dur) # tom2b

_ = vjpd.get_video_subclip(video_clips[fn], start=01.50, duration=dur) # silence


# %% test patterns and bars

         # 1.2.3.4.
patt_01 = [k,_,k,_ ] # kick
patt_02 = [x,x,x,_ ] # china
patt_03 = [c,c,c,_ ] # crash1
patt_04 = [d,d,d,_ ] # crash2

         # 1.2.3.4.
patt_05 = [h,h,h,_ ] # hat1
patt_06 = [i,i,i,_ ] # hat2
patt_07 = [j,j,j,_ ] # hat1
patt_08 = [o,o,o,_ ] # hat2

         # 1.2.3.4.
patt_09 = [s,s,s,_ ] # snare1
patt_10 = [z,z,z,_ ] # snare2
patt_11 = [s,z,s,_ ]
patt_12 = [z,s,z,_ ]

         # 1.2.3.4.
patt_13 = [t,t,t,_ ] # tom1a (clips!)
patt_14 = [v,v,v,_ ] # tom1b
patt_15 = [w,w,w,_ ] # tom2a
patt_16 = [u,u,u,_ ] # tom2b

         # 1.2.3.4.
patt_17 = [k,_,h,_ ] # 
patt_18 = [s,_,i,_ ] # 
patt_19 = [k,_,h,h ] # 
patt_20 = [z,_,i,_ ] # 

         # 1.2.3.4.
patt_21 = [k,_,h,_ ] # 
patt_22 = [s,_,i,_ ] # 
patt_23 = [k,k,h,h ] # 
patt_24 = [z,_,o,_ ] # 


        # |1 . . . |2 . . . |3 . . . |4 . . . 
barr_00 = [
           # patt_01, patt_02, patt_03, patt_04 ,
           # patt_05, patt_06, patt_07, patt_08 ,
           # patt_09, patt_10, patt_11, patt_12 ,
           # patt_13, patt_14, patt_15, patt_16 ,
           
           patt_17, patt_18, patt_19, patt_20 ,
           patt_21, patt_22, patt_23, patt_24 ,
           
           ]


# make final clip
final_clip = vjpd.concatenate_subclips(
    [subclip for patt in barr_00 for subclip in patt]
    )


# save final clip
iteration = '002'
video_result_path = os.path.join(
    beats_path,
    beat_name,
    f'{beat_name}_{iteration}.mp4'
    )
vjpd.write_concatenated_subclips(final_clip, video_result_path)
