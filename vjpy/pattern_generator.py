"""pattern generator."""
import random


class PatternGenerator:
    """Pattern generator."""

    def __init__(self):
        pass

    def generate_random_pattern(self, patt_len):
        """
        Generate a random pattern.

        Returns
        -------
        None.

        """
        abbvs = ["t", "h", "s", ".", "k", "c", "g", "v"]
        random_pattern = []
        for _ in range(patt_len):
            random_pattern.append(random.choice(abbvs))
        return random_pattern
