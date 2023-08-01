"""pattern generator."""
import random


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
            random_pattern.append(random.choice(abbvs))
        return random_pattern
