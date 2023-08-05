"""vjpy controller."""

# devices
from vjpy.devices.midi_device import MidiDevice
from vjpy.devices.wav_device import WavDevice

# data
from vjpy.data.midi.drumkits import TR808EmulationKit, My808kit
from vjpy.data.midi.patterns import bar_example, bars_example

# initialize devices
md = MidiDevice(drumkit=TR808EmulationKit)
wd = WavDevice(drumkit=My808kit)

# %% Test midi device

# %% Play

# Play a pattern
print("Playing a pattern.")
md.play_pattern("k.h.c.h.")

# Play a bar of patterns
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
for _ in range(4):
    rp = md.generate_random_pattern(patt_len=4)
    print(f"Playing random pattern:{rp}")
    md.play_pattern(rp)

# %% Test midi receiving
midi_in = md.open_midi_in()
for m in md.yield_midi_msg(midi_in):
    wd.play_wav_from_midi_msg(m)

# %% Test midi sending
midi_sender = md.open_midi_out()
for _ in range(4):
    for note in [43, 38, 43, 45]:
        md.send_note(note)

# %% Test wav device
wd.create_sine_wave()
wd.plot_sine()
wd.test_wav_reading()
wd.write_concatenated_wavs()
