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

## RIGHT HAND
### CYMBALS
a0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=0.087)     # hat_a_R
a1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=0.9)       # hat_b_R
a2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=2.23)      # hat_c_R
a3 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=3.50)      # hat_c_R silence

b0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=8.8565)    # crash1_R
b1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=18.51)     # crash2_R
c0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=14.77)     # china_R
d0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=11.05)     # ride_R
d1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=13.25)     # bell_R

### DRUMS
f0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=4.62)      # snare_R
g0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=6.989)     # tom1_R
h0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=20.46)     # tom2_R


## LEFT HAND
### CYMBALS
i0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=34.30)     # ride_a_L
i1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=62.47)     # ride_b_L
i2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=65.56)     # bell_b_L
j0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=31.605)    # crash1_a_L
j1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=58.980)    # crash1_b_L
k0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=39.816)    # crash2_a_L
k1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=76.05)     # crash2_b_L
l0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=42.72)     # china_a_L
l1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=68.03)     # china_b_L
l2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=73.14)     # china_c_L

### DRUMS
m0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=27.10)     # snare_a_L
m1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=45.81)     # snare_b_L
m2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=48.09)     # snare_c_L
n0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=29.38)     # tom1_a_L
n1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=51.32)     # tom1_b_L
n2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=51.80)     # tom1_c_L
o0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=37.36)     # tom2_a_L
o1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=78.34)     # tom2_b_L


## RIGHT FOOT
p0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=22.66)     # kick_a
p1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=24.61)     # kick_b

## LEFT FOOT
q0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=84.13)     # hat-pedal_a
q1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=96.29)     # hat-pedal_b

# patt = [a0, a1, a2,
#         b0, b1,
#         c0, d0, d1,
#         f0, g0, h0,
#         i0, i1, i2,
#         j0, j1,
#         k0, k1,
#         l0, l1, l2,
#         m0, m1, m2,
#         n0, n1, n2,
#         o0, o1,
#         p0, p1,
#         q0, q1]


dd = {
      'h': a0,
      'k': p0,
      's': f0,
      '_': a3
      }

patt = [
   #  1   2   3   4   5   6   7   8   
      p0, a0, f0, a0, p0, a0, f0, a0,
    ]

c_subclips = vjpd.concatenate_subclips(patt*2)
video_result_path = os.path.join(beats_path, beat_name, f'{beat_name}.mp4')
vjpd.write_concatenated_subclips(c_subclips, video_result_path)




