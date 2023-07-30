"""pattern generator."""
import random
from vjpy.midi_sequencer import MidiSequencer


class PatternGenerator:
    """Pattern generator."""

    def __init__(self, seq=MidiSequencer):
        self.sequencer = seq()

    def generate_random_pattern(self):
        """
        Generate random pattern.

        Returns
        -------
        None.

        """
        abbvs = ["t", "h", "s", "."]
        random_pattern = []
        for _ in range(8):
            random_pattern.append(random.choice(abbvs))
        print(f"\n\n♪♪ Playing random pattern: {random_pattern}")
        self.sequencer.play_pattern(random_pattern)
