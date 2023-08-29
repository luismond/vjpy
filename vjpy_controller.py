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

# crash2
d2 = vjpd.get_video_subclip(video_clips[7], 10.3, 10.8)

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
        c, c, e, c,
        
        c, b, g, b, #2
        c, b, g, b, 
        c, b, g, c,
        c, c, e, e,
        
        c, b, g, b, #3
        c, b, g, b, 
        c, b, g, c,
        c, c, e, c,
        
        c, b, g, b, #4
        c, b, g, b, 
        c, b, g, c,
        c2, c2, c2, c2, g, g,
        
        c, b, g, b, #1b
        c, b, g, b, 
        c, b, g, c,
        c, c, e, c,
        
        c, b, g, b, #2b
        c, b, g, b, 
        c, b, g, c,
        e, e, e, e,
        
        c, b, g, b, #3b
        c, b, g, b, 
        c, b, g, c,
        c, c, e, c,
        
        c, b, g, b, #4b
        c, b, g, b, 
        c, b, g, g,
        c2, c2, c2, c2, g, g, d2
        
        ]

patt_l = loop_patt(patt, 1)

c_subclips = vjpd.concatenate_subclips(patt_l)

vjpd.write_concatenated_subclips(c_subclips, 'subclip_test.mp4')
#%%

# %% Test video 3
import os
d = 'robodrum-bank'
video_filenames = sorted([v for v in os.listdir(d)])

#%%
video_clips = []
for v in video_filenames:
    vp = os.path.join(d, v)
    video_clip = vjpd.get_video_clip(vp)
    video_clips.append(video_clip)
    
#%%
clip_duration = .25


# sticks
a_clip = video_clips[1]
a_clip_start = 1.6
a = vjpd.get_video_subclip(a_clip, a_clip_start, a_clip_start+clip_duration)

# hat sticked
b_clip = video_clips[4]
b_clip_start = 18.45
b = vjpd.get_video_subclip(b_clip, b_clip_start, b_clip_start+clip_duration)

# crash
c_clip = video_clips[4]
c_clip_start = 21
c = vjpd.get_video_subclip(c_clip, c_clip_start, c_clip_start+clip_duration)

# rim
d_clip = video_clips[4]
d_clip_start = 25.9
d = vjpd.get_video_subclip(d_clip, d_clip_start, d_clip_start+clip_duration)

# hat open
e_clip = video_clips[5]
e_clip_start = 20.8
e = vjpd.get_video_subclip(e_clip, e_clip_start, e_clip_start+clip_duration)

# tom
f_clip = video_clips[6]
f_clip_start = 20.13
f = vjpd.get_video_subclip(f_clip, f_clip_start, f_clip_start+clip_duration)

# snare
g_clip = video_clips[10]
g_clip_start = 20.745
g = vjpd.get_video_subclip(g_clip, g_clip_start, g_clip_start+clip_duration)



c_subclips = vjpd.concatenate_subclips([g])

vjpd.write_concatenated_subclips(c_subclips, 'subclip_test.mp4')