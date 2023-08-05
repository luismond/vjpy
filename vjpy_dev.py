"""vjpy examples script."""
from time import sleep
from vjpy.midi_sequencer import MidiSequencer
from vjpy.patterns import bar_example, bars_example
from vjpy.pattern_generator import PatternGenerator
from vjpy.midi_receiver import MidiReceiver
from vjpy.wav_device import WavDevice
from vjpy.midi_sender import MidiSender

# %% seq
seq = MidiSequencer(bpm=160)

# %% Play a pattern
seq.play_pattern("k.h.c.h.")

# %% Play a bar of patterns
print(f"Playing a bar:\n{bar_example.patterns}")
seq.play_bar(bar_example)

# %% Loop a bar
print("Looping a bar")
seq.loop_bar(bars_example[0], num_loops=4)

# %% Loop a sequence of bars
print("Looping a sequence of bars")
seq.loop_bars(bars_example, num_loops=2)

# %% Test pattern generator
pg = PatternGenerator()
for _ in range(4):
    rp = pg.generate_random_pattern(patt_len=4)
    print(f"Playing random pattern:\n{rp}")
    seq.play_pattern(rp)

# %% Test wav writer
wd = WavDevice()
wd.create_sine_wave()
wd.plot_sine()
wd.test_wav_reading()
wd.write_concatenated_wavs()

# %% Test midi receiver and wav player
midi_receiver = MidiReceiver()
wd = WavDevice()

# Play each midi message received.
for m in midi_receiver.yield_midi_msg():
    wd.play_wav_from_midi_msg(m)

# %% Test midi sender
sender = MidiSender()
for _ in range(4):
    for note in [43, 38, 43, 45]:
        sender.send_note(note)
        sleep(.5)
