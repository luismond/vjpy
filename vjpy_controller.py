"""vjpy controller."""
from time import sleep

# devices
from vjpy.midi_device import MidiDevice
from vjpy.wav_device import WavDevice

# data
from vjpy.data.midi.drumkits import TR808EmulationKit, my808kit
from vjpy.data.midi.patterns import bar_example, bars_example

# %% midi device
md = MidiDevice(drumkit=TR808EmulationKit)

# %% Play a pattern
md.play_pattern("k.h.c.h.")
# Play a bar of patterns
print(f"Playing a bar:\n{bar_example.patterns}\n")
md.play_bar(bar_example)
# Loop a bar
print("Looping a bar")
md.loop_bar(bars_example[0], num_loops=4)
# Loop a sequence of bars
print("Looping a sequence of bars\n")
md.loop_bars(bars_example, num_loops=2)
# Generate random patterns
for _ in range(4):
    rp = md.generate_random_pattern(patt_len=4)
    print(f"Playing random pattern:\n{rp}\n")
    md.play_pattern(rp)

# %% wav device
wd = WavDevice(drumkit=my808kit)
wd.create_sine_wave()
wd.plot_sine()
wd.test_wav_reading()
wd.write_concatenated_wavs()

# %% Test midi receiver and wav player
midi_receiver = md.open_midi_receiver()
wd = WavDevice(drumkit=my808kit)

# Play each midi message received.
for m in md.yield_midi_msg(midi_receiver):
    wd.play_wav_from_midi_msg(m)

# %% Test midi sender
midi_sender = md.open_midi_out()

for _ in range(4):
    for note in [43, 38, 43, 45]:
        md.send_note(note)
        sleep(.5)
