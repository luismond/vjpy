"""vjpy controller."""

# devices
from vjpy_device import VjPyDevice

# data
from vjpy_device import MyFunkKit
from vjpy_device import bar_example, bars_example
drumkit = MyFunkKit

# maps
drumkit_note_names = {}  # drumkit midi notes
for drum in drumkit.drums.values():
    drumkit_note_names[drum.note] = drum.name

drumkit_sh_names = {}  # drumkit shorthand names
for drum in drumkit.drums.values():
    drumkit_sh_names[drum.short_hand] = drum.name

# initialize device
vjpd = VjPyDevice(
    drumkit=MyFunkKit,
    drumkit_sh_names=drumkit_sh_names
    )


# %% Test wav verbs
notes = [43, 38, 43, 40]
vjpd.write_concatenated_wavs(drumkit_note_names, notes)

# Pattern
print("Playing a pattern.")
vjpd.play_pattern("k.h.c.h.")

# Bar
print(f"Playing a bar:\n{bar_example.patterns}")
vjpd.play_bar(bar_example)

# Loop a bar
print("Looping a bar")
vjpd.loop_bar(bars_example[0], num_loops=2)

# Loop a sequence of bars
print("Looping a sequence of bars")
vjpd.loop_bars(bars_example, num_loops=1)

# Generate random patterns
rp = vjpd.generate_random_pattern(patt_len=8)
print(f"Playing random pattern:{rp}")
vjpd.play_pattern(rp)

# %% Test midi receiving
midi_in = vjpd.open_midi_in()

for msg in vjpd.yield_midi_msg(midi_in):
    vjpd.play_drum_wav_from_midi_msg(drumkit_note_names, msg)

# %% Test midi sending
vjpd.send_note(40)
