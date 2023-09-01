"""vjpy controller."""

import os
from vjpy import VjPyDevice
vjpd = VjPyDevice()

# %% Wav concatenating
print("\nConcatenating wavs.")

notes = [
    38, 38, 40, 38,
    38, 38, 40, 38
    ]
vjpd.write_concatenated_wavs(notes)

# %% Pattern playing
print("\nPlaying a pattern.")
vjpd.play_pattern("khckhkckkhckhkkckhckhkhkckhkchkc")

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

duration = 0.15

a = vjpd.get_video_subclip(video_clips[fn], start=00.10, duration=duration) # bell
b = vjpd.get_video_subclip(video_clips[fn], start=03.71, duration=duration) # ride
c = vjpd.get_video_subclip(video_clips[fn], start=07.12, duration=duration) # china
d = vjpd.get_video_subclip(video_clips[fn], start=09.71, duration=duration) # crash1
e = vjpd.get_video_subclip(video_clips[fn], start=13.19, duration=duration) # crash2
f = vjpd.get_video_subclip(video_clips[fn], start=17.87, duration=duration) # hat1
g = vjpd.get_video_subclip(video_clips[fn], start=19.39, duration=duration) # hat2
h = vjpd.get_video_subclip(video_clips[fn], start=21.29, duration=duration) # hat3
i = vjpd.get_video_subclip(video_clips[fn], start=23.07, duration=duration) # hat4
j = vjpd.get_video_subclip(video_clips[fn], start=23.66, duration=duration) # hat5

k = vjpd.get_video_subclip(video_clips[fn], start=24.95, duration=duration) # kick1
l = vjpd.get_video_subclip(video_clips[fn], start=26.05, duration=duration) # kick2
m = vjpd.get_video_subclip(video_clips[fn], start=27.51, duration=duration) # snare1
n = vjpd.get_video_subclip(video_clips[fn], start=29.50, duration=duration) # snare2

o = vjpd.get_video_subclip(video_clips[fn], start=31.46, duration=duration) # tom1a
p = vjpd.get_video_subclip(video_clips[fn], start=34.23, duration=duration) # tom1b
q = vjpd.get_video_subclip(video_clips[fn], start=37.16, duration=duration) # tom2a
r = vjpd.get_video_subclip(video_clips[fn], start=38.97, duration=duration) # tom2b

_ = vjpd.get_video_subclip(video_clips[fn], start=01.5, duration=duration) # silence


patt2 = [
     # |1 . . . |2 . . . |3 . . . |4 . . . 
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,k,_, k,_,k,_, k,_,k,_, k,_,k,_,
        k,_,k,k, k,_,k,_, k,_,k,k, k,_,k,_,
        k,_,k,k, k,_,k,_, k,_,k,k, k,_,k,_,
        
        k,_,b,b, m,_,b,_, k,_,b,b, m,_,b,_,
        k,_,b,b, m,_,b,_, k,_,b,b, m,_,b,_,
        k,_,b,b, m,_,b,_, k,_,b,b, m,_,b,_,
        k,_,b,b, m,_,b,_, k,_,a,a, m,n,o,r,
        
        c,_,b,b, m,_,b,_, k,_,b,b, m,_,b,_,
        k,_,b,b, m,_,b,_, k,_,b,b, m,_,b,_,
        k,_,b,b, m,_,b,_, k,_,b,b, m,_,b,_,
        k,_,b,b, m,_,b,_, k,_,a,a, m,k,m,k,
        
        k,_,b,b, m,_,b,_, k,_,b,b, m,_,b,_,
        k,_,b,b, m,_,b,_, k,_,b,b, m,_,b,_,
        k,_,b,b, m,_,b,_, k,_,b,b, m,_,b,_,
        k,_,b,b, m,_,b,_, k,_,a,a, m,n,o,r,
        
        k,_,k,k, k,_,k,_, k,_,k,k, k,_,k,_,
        k,_,k,k, k,_,k,_, k,_,k,k, k,_,k,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,k,_, k,_,k,_, k,_,k,_, k,_,k,_,

        ]


c_subclips = vjpd.concatenate_subclips(patt2 * 2)

video_result_path = os.path.join(beats_path, beat_name, f'{beat_name}.mp4')
vjpd.write_concatenated_subclips(c_subclips, video_result_path)
