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

dir_ = 'robodrum-bank-3'
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

a = vjpd.get_video_subclip(video_clips['china'], start=0.05, subclip_duration=.7)
#b = vjpd.get_video_subclip(video_clips['crash1'], start=0.05, subclip_duration=.7)
c = vjpd.get_video_subclip(video_clips['crash2'], start=0.05, subclip_duration=.7)


d = vjpd.get_video_subclip(video_clips['ride1'], start=0.045)
e = vjpd.get_video_subclip(video_clips['bell1'], start=0.05)

# f = vjpd.get_video_subclip(video_clips['hat1']) # pedal
# g = vjpd.get_video_subclip(video_clips['hat2'], start=0.05) 
h = vjpd.get_video_subclip(video_clips['hat3'], start=0.13) 
o = vjpd.get_video_subclip(video_clips['hat4'], start=0.1) # open

# j = vjpd.get_video_subclip(video_clips['kick1'], start=0)
k = vjpd.get_video_subclip(video_clips['kick2'], start=0.075)

s = vjpd.get_video_subclip(video_clips['snare1'], start=0.05)
z = vjpd.get_video_subclip(video_clips['snare2'], start=0.075)

# o = vjpd.get_video_subclip(video_clips['tom1'], start=0.05)
# p = vjpd.get_video_subclip(video_clips['tom2'], start=0.05)
# q = vjpd.get_video_subclip(video_clips['tom3'], start=0.05)
# r = vjpd.get_video_subclip(video_clips['tom4'], start=0.05)

_ = vjpd.get_video_subclip(video_clips['silence'])


patt2 = [
      # 1  2  3  4  5  6  7  8  # intro
        # k, _, k, _, k, _, k, k,
        # k, _, k, _, k, _, k, k,
      
      # 1  2  3  4  5  6  7  8  # bum bap
        k, _, s, _, k, _, s, k,
        k, _, s, _, k, _, s, k,
        k, _, s, _, k, _, s, k,
        k, _, s, _, k, _, s, s,

      # 1  2  3  4  5  6  7  8  # bum bap ts 1
        k, h, z, h, k, h, z, h,
        k, h, z, h, k, h, z, o,
        k, h, z, h, k, h, z, h,
        k, h, z, h, k, h, z, o,

      # 1  2  3  4  5  6  7  8  # bum bap ts 2
        k, h, z, h, k, h, z, h,
        k, h, z, h, k, h, z, o,
        k, h, z, h, k, h, z, h,
        k, h, z, h, k, h, z, s,
        
      # 1  2  3  4  5  6  7  8  # bum bap ts 1b
        k, d, z, d, k, d, z, d,
        k, d, z, d, k, d, z, e,
        k, d, z, d, k, d, z, d,
        k, d, z, d, k, d, z, o,

      # 1  2  3  4  5  6  7  8  # bum bap ts 2b
        k, d, z, d, k, d, z, d,
        k, d, z, d, k, d, z, e,
        k, d, z, d, k, d, z, d,
        k, d, z, d, k, d, z, o, a
        ]

c_subclips = vjpd.concatenate_subclips(patt2*1)
vjpd.write_concatenated_subclips(c_subclips, f'{proj}/{proj}.mp4')