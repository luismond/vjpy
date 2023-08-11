"""vjpy controller."""

from vjpy import VjPyDevice
vjpd = VjPyDevice()

# %% Wav concatenating
print("\nConcatenating wavs.")

notes = [38, 38, 40, 38]
vjpd.write_concatenated_wavs(notes)

# %% Pattern playing
print("\nPlaying a pattern.")
vjpd.play_pattern("k.h.c.h.")

# Bar playing
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
