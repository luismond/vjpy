"""vjpy examples script."""

from vjpy import MidiSequencer, TR808EmulationKit
from vjpy.patterns import bar_, bars, pattern
from time import sleep
from pprint import pprint as pp

# Instantiate a sequencer device and set the bpm to 120
bpm = 120
seq = MidiSequencer(bpm=bpm)

# Print drumkit info
print("Drumkit info:\n")
pp(TR808EmulationKit.drums)

# Play a pattern
patt = pattern.pattern
print(f"\n\n♪♪ Playing a pattern (a dot represents silence)\n{patt}:")
seq.play_pattern(pattern.pattern)
sleep(1)

# Play a bar of patterns
print(f"\n\n♪♪ Playing a bar:\n{bar_.patterns}")
seq.play_bar(bar_)
sleep(1)

# Loop a bar
num_loops = 4
print(f"\n\n♪♪ Looping a bar {num_loops} times:")
seq.loop_bar(bars[0], num_loops)
sleep(1)

# Loop a sequence of bars
num_loops = 2
print(f"\n\n♪♪ Looping a sequence of bars {num_loops} times:")
seq.loop_bars(bars, num_loops)
sleep(1)
