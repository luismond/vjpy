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
proj = 'videobeat-008'
if not proj in os.listdir():
    os.mkdir(proj)

# kick.mp4, snare.mp4, etc.
video_filenames = sorted([v for v in os.listdir(dir_)])

video_clips = {}
for v in video_filenames:
    vp = os.path.join(dir_, v)
    video_clip = vjpd.get_video_clip(vp)
    video_clips[v[:-4]] = video_clip


# %% video clips corresponding to 1 drum sound each

a = vjpd.get_video_subclip(video_clips['china'], start=0.05)
b = vjpd.get_video_subclip(video_clips['crash1'], start=0.03)
c = vjpd.get_video_subclip(video_clips['crash2'], start=0.03)
d = vjpd.get_video_subclip(video_clips['ride1'], start=0.1)
e = vjpd.get_video_subclip(video_clips['bell1'], start=0.05)

f = vjpd.get_video_subclip(video_clips['hat1'], start=0) # pedal
g = vjpd.get_video_subclip(video_clips['hat2'], start=0.05) # stick 1
h = vjpd.get_video_subclip(video_clips['hat3'], start=0.05) # stick 2
i = vjpd.get_video_subclip(video_clips['hat4'], start=0.05) # open

j = vjpd.get_video_subclip(video_clips['kick1'], start=0.06)
k = vjpd.get_video_subclip(video_clips['kick2'], start=0.095)

m = vjpd.get_video_subclip(video_clips['snare1'], start=0.13)
n = vjpd.get_video_subclip(video_clips['snare2'], start=0.09)

o = vjpd.get_video_subclip(video_clips['tom1'], start=0.1)
p = vjpd.get_video_subclip(video_clips['tom2'], start=0.07)
q = vjpd.get_video_subclip(video_clips['tom3'], start=0.075)
r = vjpd.get_video_subclip(video_clips['tom4'], start=0.1)

s = vjpd.get_video_subclip(video_clips['silence'], start=0)


patt = [a, b, c, d,
        a, b, c, e,
        a, b, f, f,
        a, c, g, g,
        a, g, h, h,
        a, b, i, i,
        
        j, j, k, k,
        j, j, m, m,
        j, j, k, k,
        j, j, n, n,
        
        j, j, o, o,
        j, j, p, p,
        j, j, q, q,
        k, k, r, r,
        
        j, s, j, s,
        j, s, j, s]

c_subclips = vjpd.concatenate_subclips(patt*2)
vjpd.write_concatenated_subclips(c_subclips, 'test.mp4')