"""vjpy backend."""

from vjpy import NoteValue, MidiDevice, WavDevice, VideoDevice, drum_kits


class VjPyDevice:
    """vjpy device."""

    def __init__(self, soundbank_name, bpm=90, resolution="1/4"):
        self.bpm = bpm
        self.resolution = resolution
        self.drum_kit = drum_kits["TR808EmulationKit"]
        self.soundbank_name = soundbank_name
        self.note_duration = self.bpm/60

        self.midi_device = MidiDevice(
            bpm=self.bpm,
            resolution=self.resolution,
            note_values=self.note_values,
            drumkit_sh_notes=self.drumkit_sh_notes
            )

        self.wav_device = WavDevice()

        self.video_device = VideoDevice(
            bpm=self.bpm,
            soundbank_name=self.soundbank_name,
            resolution=self.resolution,
            note_values=self.note_values,
            note_duration=self.note_duration
            )

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
        for drum in self.drum_kit.drums.values():
            drumkit_sh_names[drum.short_hand] = drum.name
        return drumkit_sh_names

    @property
    def drumkit_sh_notes(self):
        """Mapping short-hand-names <-> notes."""
        drumkit_sh_notes = {}
        for drum in self.drum_kit.drums.values():
            drumkit_sh_notes[drum.short_hand] = drum.note
        return drumkit_sh_notes

    @property
    def drumkit_note_names(self):
        """Mapping notes <-> note names."""
        drumkit_note_names = {}
        for drum in self.drum_kit.drums.values():
            drumkit_note_names[drum.note] = drum.name
        return drumkit_note_names
