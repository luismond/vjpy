"""vjpy controller."""

from vjpy_device import VjPyDevice
from vjpy_device import bar_example, bars_example

vjpd = VjPyDevice()

# %%
# Wav concatenating
print("\nConcatenating wavs.")
notes = [43, 38, 43, 40]
vjpd.write_concatenated_wavs(notes)

# Pattern playing
print("\nPlaying a pattern.")
vjpd.play_pattern("k.h.c.h.")

# Bar playing
print("\nPlaying a bar.")
vjpd.play_bar(bar_example)

# Bar looping
print("\nLooping a bar.")
vjpd.loop_bar(bars_example[0], num_loops=2)

# Bars looping
print("\nLooping a sequence of bars.")
vjpd.loop_bars(bars_example, num_loops=1)

# Random pattern generation
print("\nPlaying random pattern.")
rp = vjpd.generate_random_pattern(patt_len=4)
vjpd.play_pattern(rp)

# %% Test midi receiving
for msg in vjpd.yield_midi_msg():
    vjpd.play_drum_wav_from_midi_msg(msg)

# %% Test midi sending
vjpd.send_note(40)
