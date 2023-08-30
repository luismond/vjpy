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
print("\nPlaying a bar.")
vjpd.play_bar(vjpd.bar_example)

# Bar looping
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

dir_ = 'robodrum-bank-2'
video_filenames = sorted([v for v in os.listdir(dir_)]) # kick.mp4, snare.mp4, etc.

video_clips = []
for v in video_filenames:
    vp = os.path.join(dir_, v)
    video_clip = vjpd.get_video_clip(vp)
    video_clips.append(video_clip)

# %%
duration = .175#.0875#.35#.175

# video clips corresponding to 1 drum sound each

a = vjpd.get_video_subclip(video_clips[0], 0.05, 0.05+duration) # china
b = vjpd.get_video_subclip(video_clips[1], 0, 0+duration) # crash1
c = vjpd.get_video_subclip(video_clips[2], 0, 0+duration) # crash2
d = vjpd.get_video_subclip(video_clips[9], 0.1, 0.1+duration) # ride
e = vjpd.get_video_subclip(video_clips[10], 0.05, 0.05+duration) # ride bell


f = vjpd.get_video_subclip(video_clips[3], 0, 0+duration) # hat pedal
g = vjpd.get_video_subclip(video_clips[4], 0.05, 0.05+duration) # hat stick a
h = vjpd.get_video_subclip(video_clips[5], 0.05, 0.05+duration) # hat stick b
i = vjpd.get_video_subclip(video_clips[6], 0.05, 0.05+duration) # hat open

j = vjpd.get_video_subclip(video_clips[7], 0, 0+duration) # kick a
k = vjpd.get_video_subclip(video_clips[8], 0.05, 0.05+duration) # kick b
l = vjpd.get_video_subclip(video_clips[8], 0.05, 0.05+(duration/2)) # kick b/2

m = vjpd.get_video_subclip(video_clips[11], 0.07, 0.07+duration) # snare right
n = vjpd.get_video_subclip(video_clips[12], 0.04, 0.04+duration) # snare left

o = vjpd.get_video_subclip(video_clips[13], 0.05, 0.05+duration) # tom1 a
p = vjpd.get_video_subclip(video_clips[14], 0.055, 0.055+duration) # tom1 b

q = vjpd.get_video_subclip(video_clips[15], 0.05, 0.05+duration) # tom2 a
r = vjpd.get_video_subclip(video_clips[16], 0.07, 0.07+duration) # tom2 b

s = vjpd.get_video_subclip(video_clips[17], 0, 0+duration) # silence
t = vjpd.get_video_subclip(video_clips[17], 0, 0+(duration/2)) # silence/2



c_subclips = vjpd.concatenate_subclips(cymb_patt*16)
vjpd.write_concatenated_subclips(c_subclips, 'cymbs.mp4')