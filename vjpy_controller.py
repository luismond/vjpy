"""vjpy controller."""

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

# %% Test video 1

video_data = {
    "video_filename": 'test.mp4',
    "subclip_name": 'test_subclip.mp4',
    "start": '2.4',
    "end": '3'
    }


video_clip = vjpd.get_video_clip(video_data['video_filename'])

sc_0 = vjpd.get_video_subclip(video_clip, 2.4, 3)
sc_1 = vjpd.get_video_subclip(video_clip, 3, 3.6)
sc_2 = vjpd.get_video_subclip(video_clip, 6.9, 7.2)
sc_3 = vjpd.get_video_subclip(video_clip, 6.9, 7.05)

subclips = [sc_0, sc_0, sc_1, sc_0,
            sc_0, sc_0, sc_1, sc_2, sc_2,
            sc_0, sc_0, sc_1, sc_0,
            sc_0, sc_0, sc_1, sc_3, sc_3, sc_3, sc_3,
            sc_0, sc_0, sc_1, sc_0,
            sc_0, sc_0, sc_1, sc_2, sc_2,
            sc_0, sc_0, sc_1, sc_0,
            sc_0, sc_0, sc_1, sc_3, sc_3, sc_3, sc_3,
            sc_0, sc_0, sc_1, sc_0,
            sc_0, sc_0, sc_1, sc_2, sc_2,
            sc_0, sc_0, sc_1, sc_0,
            sc_0, sc_0, sc_1, sc_3, sc_3, sc_3, sc_3,
            sc_0, sc_0, sc_1, sc_0,
            sc_0, sc_0, sc_1, sc_2, sc_2,
            sc_0, sc_0, sc_1, sc_0,
            sc_0, sc_0, sc_1, sc_3, sc_3, sc_3, sc_3]


c_subclips = vjpd.concatenate_subclips(subclips)

vjpd.write_concatenated_subclips(c_subclips, video_data['subclip_name'])

# %% Test video 2
import os
d = '/home/user/Downloads/vjpy_video_tests'
video_filenames = sorted([v for v in os.listdir(d)])

#%%
video_clips = []
for v in video_filenames:
    vp = os.path.join(d, v)
    video_clip = vjpd.get_video_clip(vp)
    video_clips.append(video_clip)

#%%

# hh_pedal_1
a = vjpd.get_video_subclip(video_clips[0], 10.28, 10.53)

# hh_pedal_2
b = vjpd.get_video_subclip(video_clips[6], 6.23, 6.48)

# hh_pedal_3
b2 = vjpd.get_video_subclip(video_clips[6], 6.23, 6.355)

# tom_1
c = vjpd.get_video_subclip(video_clips[6], 20.3, 20.55)

# tom_2
c2 = vjpd.get_video_subclip(video_clips[6], 20.30, 20.425)

# crash
d = vjpd.get_video_subclip(video_clips[7], 10.3, 10.55)

# snare_bell
e = vjpd.get_video_subclip(video_clips[10], 6.10, 6.35)

# snare_crash_1
f = vjpd.get_video_subclip(video_clips[6], 16.9, 17.15)

# snare
g = vjpd.get_video_subclip(video_clips[6], 20.73, 20.98)

def loop_patt(patt, n):
    return patt*n

patt = [
        c, b, g, b, #1
        c, b, g, b, 
        c, b, g, c,
        c, c, f, c,
        
        c, b, g, b, #2
        c, b, g, b, 
        c, b, g, c,
        c, c, f, e,
        
        c, b, g, b, #3
        c, b, g, b, 
        c, b, g, c,
        c, c, f, c,
        
        c, b, g, b, #4
        c, b, g, b, 
        c, b, g, c,
        c2, c2, c2, c2, g, g,
        
        c, b, g, b, #5
        c, b, g, b, 
        c, b, g, c,
        c, c, f, c,
        
        c, b, g, b, #6
        c, b, g, b, 
        c, b, g, c,
        c, c, f, f,
        
        c, b, g, b, #7
        c, b, g, b, 
        c, b, g, c,
        c, c, f, c,
        
        c, b, g, b, #8
        c, b, g, b, 
        c, b, g, c,
        d, d, c2, c2, c2, c2, d
        
        ]

patt_l = loop_patt(patt, 1)

c_subclips = vjpd.concatenate_subclips(patt_l)

vjpd.write_concatenated_subclips(c_subclips, 'subclip_test.mp4')