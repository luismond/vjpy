"""vjpy examples script."""

from vjpy import MidiSequencer
from vjpy import TR808EmulationKit
from vjpy import pattern_examples, bar_example, bars_example
from vjpy import WavPlayer
from vjpy import MidiReceiver
from vjpy import MidiSender
from vjpy import PatternGenerator
from vjpy.drumkits import my808kit
from time import sleep
from vjpy import MidiSender
from vjpy import MidiReceiver
from vjpy import WavPlayer
import mido
from mido import Message

# %% Instantiate a sequencer and set the bpm to 120
seq = MidiSequencer(drumkit=my808kit, bpm=90)

# Play a pattern
patt = "khshkhshkhshkhsh"
print(f"Playing a pattern:\n{patt}")
seq.play_pattern(patt)


# %% Play a bar of patterns
print(f"Playing a bar:\n{bar_example.patterns}")
seq.play_bar(bar_example)


# %% Loop a bar
NUM_LOOPS = 4
print(f"Looping a bar {NUM_LOOPS} times:")
seq.loop_bar(bars_example[0], NUM_LOOPS)


# %% Loop a sequence of bars
NUM_LOOPS = 2
print(f"Looping a sequence of bars {NUM_LOOPS} times:")
seq.loop_bars(bars_example, NUM_LOOPS)


# %% Test midi receiver and wav player
midi_receiver = MidiReceiver()
wav_player = WavPlayer()

# Play each midi message received.
for m in midi_receiver.yield_midi_msg():
    wav_player.play_wav_from_midi_msg(m)

# %% Test wav player

wav_player = WavPlayer()

# play a hat
msg = Message('note_on', note=50, velocity=50, time=0)
wav_player.play_wav_from_midi_msg(msg)


# %% Test midi sender

sender = MidiSender()
for _ in range(4):
    for note in [43, 38, 43, 45]:
        sender.send_note(note)
        sleep(.5)

# %% Test pattern generator
PatternGenerator().generate_random_pattern()