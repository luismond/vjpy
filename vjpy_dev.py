"""vjpy examples script."""

from time import sleep

# %% Instantiate a sequencer device and set the bpm to 120
from vjpy.midi_sequencer import MidiSequencer
bpm = 120
seq = MidiSequencer(bpm=bpm)

# %% Instantiate a drumkit
from vjpy.drumkits import TR808EmulationKit
print("Drumkit info:\n")
print(TR808EmulationKit.drums)

# %% Play a pattern
from vjpy.patterns import pattern_example
patt = pattern_example.pattern
print(f"\n\n♪♪ Playing a pattern (a dot represents silence)\n{patt}:")
seq.play_pattern(pattern_example.pattern)
sleep(1)

# %% Play a bar of patterns
from vjpy.patterns import bar_example
print(f"\n\n♪♪ Playing a bar:\n{bar_example.patterns}")
seq.play_bar(bar_example)
sleep(1)

# %% Loop a bar
from vjpy.patterns import bars_example
num_loops = 4
print(f"\n\n♪♪ Looping a bar {num_loops} times:")
seq.loop_bar(bars_example[0], num_loops)
sleep(1)

# %% Loop a sequence of bars
num_loops = 2
print(f"\n\n♪♪ Looping a sequence of bars {num_loops} times:")
seq.loop_bars(bars_example, num_loops)
sleep(1)

# %% Test midi receiver
from vjpy.midi_receiver import MidiReceiver
from vjpy.wav_player import WavPlayer

wav_player_ = WavPlayer()
midi_receiver = MidiReceiver()

for m in midi_receiver.yield_midi_msg():
    print(m)
    wav_player_.play_wav_from_midi_msg(m)

# %% Test midi sender
from vjpy.midi_sender import MidiSender

sender = MidiSender()
for note in [36, 38, 43, 45]:
    sender.send_note(note)
