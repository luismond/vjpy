"""pattern generator."""
import random
from vjpy.midi_sequencer import MidiSequencer
from vjpy.drumkits import TR808EmulationKit


class PatternGenerator:
    """Pattern generator."""

    def __init__(self):
        pass
        #self.sequencer = seq

    def generate_random_pattern(self):
        """
        Generate random pattern.

        Returns
        -------
        None.

        """
        abbvs = ["t", "h", "s", ".", "k", "c", "g", "v"]
        random_pattern = []
        for _ in range(4):
            r = random.choice(abbvs)
            random_pattern.append(r)
        return random_pattern
