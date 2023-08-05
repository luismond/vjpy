"""Musical definition of note durations."""

from vjpy.data_classes import NoteValue

note_values = {
    '1': NoteValue(name='whole_note', relative_value=1.0),
    '1/2': NoteValue(name='half_note', relative_value=0.5),
    '1/4': NoteValue(name='quarter_note', relative_value=0.25),
    '1/8': NoteValue(name='eigth_note', relative_value=0.125),
    '1/16': NoteValue(name='sixteenth_note', relative_value=0.0625),
    '1/32': NoteValue(name='thirty-second_note', relative_value=0.03125)
    }
