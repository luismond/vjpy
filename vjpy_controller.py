"""vjpy controller."""

# devices
from vjpy.devices.midi_device import MidiDevice
from vjpy.devices.wav_device import WavDevice

# data
from vjpy.data.midi.drumkits import TR808EmulationKit, My808kit, MyFunkKit
from vjpy.data.midi.patterns import bar_example, bars_example

# initialize devices
md = MidiDevice(drumkit=TR808EmulationKit)
wd = WavDevice(drumkit=MyFunkKit)

# %% Test wav device
wd.write_concatenated_wavs(sound_names=["kick", "hat", "clap", "hat"])

# %% Play

# Pattern
print("Playing a pattern.")
md.play_pattern("k.h.c.h.")

# Bar
print(f"Playing a bar:\n{bar_example.patterns}")
md.play_bar(bar_example)


# %% Loop

# Loop a bar
print("Looping a bar")
md.loop_bar(bars_example[0], num_loops=2)

# Loop a sequence of bars
print("Looping a sequence of bars")
md.loop_bars(bars_example, num_loops=1)

# %% Generate

# Generate random patterns
rp = md.generate_random_pattern(patt_len=4)
print(f"Playing random pattern:{rp}")
md.play_pattern(rp)

# %% Test midi receiving
midi_in = md.open_midi_in()
for msg in md.yield_midi_msg(midi_in):
    wd.play_drum_wav_from_midi_msg(My808kit, msg)

# %% Test midi sending
midi_sender = md.open_midi_out()
for _ in range(4):
    for note in [43, 43]:
        md.send_note(note)
