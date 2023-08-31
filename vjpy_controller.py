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

# video-sound banks directory
sound_banks_path = os.path.join('vjpy_media', 'sound_banks')
sound_bank_path = os.path.join(sound_banks_path, 'robodrum_bank_4')

# video-sound bank file names
sound_bank_video_filenames = sorted(
    [
     video_fn for video_fn in os.listdir(
         sound_bank_path
         ) if video_fn.endswith('mp4')])

# beats directory
beats_path = os.path.join('vjpy_media', 'beats')
beat_name = 'videobeat-010'
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

video_clip_fn = 'robodrum_bank_4_video_and_sound_cleaned'

a = vjpd.get_video_subclip(video_clips[video_clip_fn], start=0.087)
b = vjpd.get_video_subclip(video_clips[video_clip_fn], start=0.9)
c = vjpd.get_video_subclip(video_clips[video_clip_fn], start=2.23)
d = vjpd.get_video_subclip(video_clips[video_clip_fn], start=4.62)

e = vjpd.get_video_subclip(video_clips[video_clip_fn], start=6.989)
f = vjpd.get_video_subclip(video_clips[video_clip_fn], start=8.8565)
g = vjpd.get_video_subclip(video_clips[video_clip_fn], start=11.05)
h = vjpd.get_video_subclip(video_clips[video_clip_fn], start=13.25)

i = vjpd.get_video_subclip(video_clips[video_clip_fn], start=14.77)
j = vjpd.get_video_subclip(video_clips[video_clip_fn], start=18.51)
k = vjpd.get_video_subclip(video_clips[video_clip_fn], start=20.46)
l = vjpd.get_video_subclip(video_clips[video_clip_fn], start=22.66)

m = vjpd.get_video_subclip(video_clips[video_clip_fn], start=24.61)
n = vjpd.get_video_subclip(video_clips[video_clip_fn], start=27.10)
o = vjpd.get_video_subclip(video_clips[video_clip_fn], start=29.38)
p = vjpd.get_video_subclip(video_clips[video_clip_fn], start=31.605)

q = vjpd.get_video_subclip(video_clips[video_clip_fn], start=34.30)
r = vjpd.get_video_subclip(video_clips[video_clip_fn], start=37.36)
s = vjpd.get_video_subclip(video_clips[video_clip_fn], start=39.816)
t = vjpd.get_video_subclip(video_clips[video_clip_fn], start=42.72)

u = vjpd.get_video_subclip(video_clips[video_clip_fn], start=45.81)
v = vjpd.get_video_subclip(video_clips[video_clip_fn], start=48.09)
w = vjpd.get_video_subclip(video_clips[video_clip_fn], start=51.32)
x = vjpd.get_video_subclip(video_clips[video_clip_fn], start=52.08)

y = vjpd.get_video_subclip(video_clips[video_clip_fn], start=58.88)
z = vjpd.get_video_subclip(video_clips[video_clip_fn], start=62.32)

a1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=65.56)
b1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=68.03)
c1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=73.14)
d1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=76.05)

e1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=78.34)
f1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=84.13)
g1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=96.29)


patt = [a, b, c, d,
        e, f, g, h,
        i, j, k, l,
        m, n, o, p,
        q, r, s, t,
        u, v, w, x,
        y, z, y, z,
        
        a1, b1, c1, d1,
        e1, f1, g1, g1
        
        ]


c_subclips = vjpd.concatenate_subclips(patt*1)
video_result_path = os.path.join(beats_path, beat_name, f'{beat_name}.mp4')
vjpd.write_concatenated_subclips(c_subclips, video_result_path)




