"""midi player test"""

from vjpy import MidiSequencer
from pydantic import BaseModel

seq = MidiSequencer(bpm=60)
sequence = 'thsh'


def loop(sequence, n):
    for _ in range(n):
        seq.play_pattern(sequence)


loop(sequence, 8)
