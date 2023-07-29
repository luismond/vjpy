"""vjpy examples script."""

from vjpy import MidiSequencer
from vjpy.patterns import bar_, bars, pattern
from time import sleep

# Instantiate a sequencer device and set the bpm to 120
bpm = 120
seq = MidiSequencer(bpm=bpm)

# Play a pattern
patt = pattern.pattern
print(f"♪♪ Playing a pattern:\n{patt}")
seq.play_pattern(pattern.pattern)
sleep(1)

# Play a bar of patterns
print(f"\n\n♪♪ Playing a bar of patterns:\n{bar_.patterns}")
for pattern_ in bar_.patterns:
    seq.play_pattern(pattern_)
sleep(1)

# Loop a bar
num_loops = 4
print(f"\n\n♪♪ Looping a bar {num_loops} times:")
seq.loop_bar(bars[0], num_loops)
sleep(1)

# Loop a sequence of bars
print("\n\n♪♪ looping a sequence of bars:")
seq.loop_bars(bars, 2)
sleep(1)
