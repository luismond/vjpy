"""vjpy examples script."""

from time import sleep
from vjpy.midi_sequencer import MidiSequencer
from vjpy.drumkits import TR808EmulationKit
from vjpy.patterns import pattern_examples, bar_example, bars_example
from vjpy.wav_player import WavPlayer
from vjpy.midi_receiver import MidiReceiver
from vjpy.midi_sender import MidiSender

# %% Instantiate a sequencer device and set the bpm to 120
BPM = 90
seq = MidiSequencer(instruments=[TR808EmulationKit], bpm=BPM)

# %% Instantiate a drumkit
print("Drumkit info:\n")
print(TR808EmulationKit.drums)

# %% Play a pattern
patt = pattern_examples[0].pattern
print(f"\n\n♪♪ Playing a pattern:\n{patt}")
seq.play_pattern(patt)
sleep(1)

# %% Play a bar of patterns
print(f"\n\n♪♪ Playing a bar:\n{bar_example.patterns}")
seq.play_bar(bar_example)
sleep(1)

# %% Loop a bar
NUM_LOOPS = 4
print(f"\n\n♪♪ Looping a bar {NUM_LOOPS} times:")
seq.loop_bar(bars_example[0], NUM_LOOPS)
sleep(1)

# %% Loop a sequence of bars
NUM_LOOPS = 2
print(f"\n\n♪♪ Looping a sequence of bars {NUM_LOOPS} times:")
seq.loop_bars(bars_example, NUM_LOOPS)
sleep(1)

# %% Test midi receiver
wav_player_ = WavPlayer()
midi_receiver = MidiReceiver()

for m in midi_receiver.yield_midi_msg():
    print(m)
    wav_player_.play_wav_from_midi_msg(m)

# %% Test midi sender
sender = MidiSender()
for note in [36, 38, 43, 45]:
    sender.send_note(note)
