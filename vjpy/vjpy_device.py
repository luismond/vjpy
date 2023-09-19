"""vjpy backend."""

from vjpy import NoteValue, drum_kits


class VjPyDevice:
    """vjpy device."""

    def __init__(self, bpm=200, resolution="1/2"):
        self.bpm = bpm
        self.drumkit = drum_kits["myfunkkit"]
        self.note_duration = self.bpm/60
        self.resolution = resolution
        self.note_value = self.note_values[resolution].relative_value / self.note_duration

    @property
    def note_values(self):
        """Musical definitions of notes' values."""
        note_values = {
            '1': NoteValue(name='whole_note', relative_value=1.0),
            '1/2': NoteValue(name='half_note', relative_value=0.5),
            '1/4': NoteValue(name='quarter_note', relative_value=0.25),
            '1/8': NoteValue(name='eigth_note', relative_value=0.125),
            '1/16': NoteValue(name='sixteenth_note', relative_value=0.0625),
            '1/32': NoteValue(name='thirty-second_note', relative_value=0.0312)
            }
        return note_values

    @property
    def drumkit_sh_names(self):
        """Mapping short-hand-names <-> full-names."""
        drumkit_sh_names = {}
        for drum in self.drumkit.drums.values():
            drumkit_sh_names[drum.short_hand] = drum.name
        return drumkit_sh_names

    @property
    def drumkit_sh_notes(self):
        """Mapping short-hand-names <-> notes."""
        drumkit_sh_notes = {}
        for drum in self.drumkit.drums.values():
            drumkit_sh_notes[drum.short_hand] = drum.note
        return drumkit_sh_notes

    @property
    def drumkit_note_names(self):
        """Mapping notes <-> full-names."""
        drumkit_note_names = {}
        for drum in self.drumkit.drums.values():
            drumkit_note_names[drum.note] = drum.name
        return drumkit_note_names
