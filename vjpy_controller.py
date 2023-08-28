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

# %% Test video

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
            sc_0, sc_0, sc_1, sc_3, sc_3, sc_3, sc_3]


c_subclips = vjpd.concatenate_subclips(subclips)

vjpd.write_concatenated_subclips(c_subclips, video_data['subclip_name'])
