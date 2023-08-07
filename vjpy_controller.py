"""vjpy controller."""

# devices
from vjpy_app import MidiDevice, WavDevice

# data
from vjpy_app import TR808EmulationKit, MyFunkKit
from vjpy_app import bar_example, bars_example
drumkit = MyFunkKit

# maps
drumkit_note_names = {} # drumkit midi notes
for drum in drumkit.drums.values():
    drumkit_note_names[drum.note] = drum.name

drumkit_sh_names = {}  # drumkit shorthand names
for drum in drumkit.drums.values():
    drumkit_sh_names[drum.short_hand] = drum.name

# initialize devices
md = MidiDevice(
    drumkit=TR808EmulationKit,
    drumkit_sh_names=drumkit_sh_names
    )
wd = WavDevice(drumkit=MyFunkKit)

# %% Test wav device
notes = [43, 38, 43, 40]
wd.write_concatenated_wavs(drumkit_note_names, notes)

# Pattern
print("Playing a pattern.")
md.play_pattern("k.h.c.h.")

# Bar
print(f"Playing a bar:\n{bar_example.patterns}")
md.play_bar(bar_example)

# Loop a bar
print("Looping a bar")
md.loop_bar(bars_example[0], num_loops=2)

# Loop a sequence of bars
print("Looping a sequence of bars")
md.loop_bars(bars_example, num_loops=1)

# Generate random patterns
rp = md.generate_random_pattern(patt_len=8)
print(f"Playing random pattern:{rp}")
md.play_pattern(rp)

# %% Test midi receiving
midi_in = md.open_midi_in()
wd = WavDevice(drumkit=MyFunkKit)

for msg in md.yield_midi_msg(midi_in):
    wd.play_drum_wav_from_midi_msg(drumkit_note_names, msg)

# %% Test midi sending
md.send_note(40)
