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
    vp = os.path.join(d, v)
    video_clip = vjpd.get_video_clip(vp)
    video_clips.append(video_clip)

# %%
duration = .3

# video clips corresponding to 1 drum sound each

ch = vjpd.get_video_subclip(video_clips[0], 0, 0+duration) # china
sh1 = vjpd.get_video_subclip(video_clips[1], 0, 0+duration) # crash1
sh2 = vjpd.get_video_subclip(video_clips[2], 0, 0+duration) # crash2
hp = vjpd.get_video_subclip(video_clips[3], 0, 0+duration) # hat pedal
hha = vjpd.get_video_subclip(video_clips[4], 0, 0+duration) # hat stick a
hhb = vjpd.get_video_subclip(video_clips[5], 0, 0+duration) # hat stick b
hho = vjpd.get_video_subclip(video_clips[6], 0, 0+duration) # hat open
ka = vjpd.get_video_subclip(video_clips[7], 0, 0+duration) # kick a
kb = vjpd.get_video_subclip(video_clips[8], 0, 0+duration) # kick b
r = vjpd.get_video_subclip(video_clips[9], 0, 0+duration) # ride
rb = vjpd.get_video_subclip(video_clips[10], 0, 0+duration) # ride bell
sa = vjpd.get_video_subclip(video_clips[11], 0, 0+duration) # snare right
sb = vjpd.get_video_subclip(video_clips[12], 0, 0+duration) # snare left
t1a = vjpd.get_video_subclip(video_clips[13], 0, 0+duration) # tom1 a
t1b = vjpd.get_video_subclip(video_clips[14], 0, 0+duration) # tom1 b
t2a = vjpd.get_video_subclip(video_clips[15], 0, 0+duration) # tom2 a
t2b = vjpd.get_video_subclip(video_clips[16], 0, 0+duration) # tom2 b


pattern = [ka, ka, sb, hha]
c_subclips = vjpd.concatenate_subclips(pattern*4)
vjpd.write_concatenated_subclips(c_subclips, 'concat_result.mp4')