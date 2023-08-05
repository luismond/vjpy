"""vpjy midi device."""
import time
import random
import mido
from vjpy.data_classes import NoteValue


class MidiDevice:
    """vjpy midi device."""

    def __init__(
            self,
            drumkit,
            bpm=90,
            resolution="1/4"
            ):
        self.drumkit = drumkit
        self.bpm = bpm
        self.res = resolution
        self.note_duration = self.bpm/60
        self.outport = mido.open_output()

    @property
    def note_values(self):
        """Musical definition of note durations."""
        note_values = {
            '1': NoteValue(name='whole_note', relative_value=1.0),
            '1/2': NoteValue(name='half_note', relative_value=0.5),
            '1/4': NoteValue(name='quarter_note', relative_value=0.25),
            '1/8': NoteValue(name='eigth_note', relative_value=0.125),
            '1/16': NoteValue(name='sixteenth_note', relative_value=0.0625),
            '1/32': NoteValue(name='thirty-second_note', relative_value=0.03125)
            }  # move to data
        return note_values

    def generate_random_pattern(self, patt_len):
        """generate_random_pattern."""
        abbvs = ["t", "h", "s", ".", "k", "c", "g", "v"]
        random_pattern = []
        for _ in range(patt_len):
            random_pattern.append(random.choice(abbvs))
        return random_pattern

    def open_midi_receiver(self):
        """Open MIDI in."""
        return mido.open_input()

    def open_midi_out(self):
        """Open MIDI out."""
        return mido.open_output()

    def yield_midi_msg(self, inport):
        """Yield MIDI messages from a MIDI in port."""
        for midi_msg in inport:
            yield midi_msg

    def send_note(self, note):
        """Send a MIDI note."""
        msg = mido.Message('note_on', note=note)
        outport = self.open_midi_out()
        outport.send(msg)

    def play_note(self, note, duration=0, velocity=50):
        """Send a MIDI note."""
        msg = mido.Message('note_on',  note=note, velocity=velocity)
        self.outport.send(msg)
        time.sleep(duration)

    def play_drum(self, drum_name, duration=0):
        """Send a drum MIDI note."""
        drum_note = self.drumkit.drums[drum_name].note
        self.play_note(note=drum_note, duration=duration)

    @staticmethod
    def play_silence(duration=0):
        """Play a silence of n duration."""
        time.sleep(duration)

    def play_pattern(self, pattern):
        """Play a sequence of notes."""
        note_value = self.note_values[self.res].relative_value / self.note_duration
        for beat in pattern:
            if beat == '.':
                self.play_silence(duration=note_value)
            else:
                drum_name = [
                    drum.name for drum in self.drumkit.drums.values()
                    if drum.short_hand == beat
                    ][0]  # simplify
                self.play_drum(drum_name=drum_name, duration=note_value)

    def play_bar(self, bar_):
        """Play a sequence of patterns."""
        patterns = "".join(bar_.patterns)
        self.play_pattern(patterns)

    def loop_bar(self, bar_, num_loops):
        """Iterate over a bar_."""
        for _ in range(num_loops):
            print(bar_)
            self.play_bar(bar_)

    def loop_bars(self, bars, num_loops):
        """Iterate over a sequence of bars_."""
        for _ in range(num_loops):
            for bar_ in bars:
                self.loop_bar(bar_, 1)
