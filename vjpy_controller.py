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

h = vjpd.get_video_subclip(video_clips[fn], start=17.87, duration=dur) # hat1
i = vjpd.get_video_subclip(video_clips[fn], start=19.39, duration=dur) # hat2
j = vjpd.get_video_subclip(video_clips[fn], start=21.29, duration=dur) # hat3
y = vjpd.get_video_subclip(video_clips[fn], start=23.07, duration=dur) # hat4
o = vjpd.get_video_subclip(video_clips[fn], start=23.66, duration=dur) # hat5

k = vjpd.get_video_subclip(video_clips[fn], start=24.95, duration=dur) # kick1
l = vjpd.get_video_subclip(video_clips[fn], start=26.05, duration=dur) # kick2

s = vjpd.get_video_subclip(video_clips[fn], start=27.51, duration=dur) # snare1
z = vjpd.get_video_subclip(video_clips[fn], start=29.50, duration=dur) # snare2

t = vjpd.get_video_subclip(video_clips[fn], start=31.46, duration=dur) # tom1a
v = vjpd.get_video_subclip(video_clips[fn], start=34.23, duration=dur) # tom1b
w = vjpd.get_video_subclip(video_clips[fn], start=37.16, duration=dur) # tom2a
u = vjpd.get_video_subclip(video_clips[fn], start=39.01, duration=dur) # tom2b

_ = vjpd.get_video_subclip(video_clips[fn], start=01.50, duration=dur) # silence



# test pattern
# patt1 = [
#      # |1 . . . |2 . . . |3 . . . |4 . . . 
#         k,_,_,_, k,_,_,_, k,_,k,_, k,_,k,_,
        
#         k,_,b,_, k,_,b,_, k,_,r,_, k,_,r,_,
#         k,_,x,_, k,_,x,_, k,_,c,_, k,_,d,_,
        
#         k,_,h,_, k,_,i,_, k,_,j,_, k,_,y,_,
#         k,_,o,_, k,_,o,_, k,_,l,_, k,_,l,_,
        
#         k,_,s,_, k,_,z,_, k,_,t,_, k,_,v,_,
#         k,_,w,_, k,_,w,_, k,_,u,_, k,_,u,_,
#         ]

# pattern template
patt = [
      #|1 . . . |2 . . . |3 . . . |4 . . . 
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        
      #|5 . . . |6 . . . |7 . . . |8 . . . 
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        ]



patts = patt1*2
c_subclips = vjpd.concatenate_subclips(patts)
iteration = '001'
video_result_path = os.path.join(beats_path, beat_name, f'{beat_name}_{iteration}.mp4')
vjpd.write_concatenated_subclips(c_subclips, video_result_path)
