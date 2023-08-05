"""vpjy midi device."""
import time
import random
import mido
from vjpy.data.midi.note_values import note_values


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
        self.resolution = resolution
        self.note_duration = self.bpm/60
        self.outport = mido.open_output()

    # I/O
    def open_midi_in(self):
        """I/O: MIDI in."""
        return mido.open_input()

    def open_midi_out(self):
        """I/O: MIDI out."""
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

    # PLAY
    def play_pattern(self, pattern):
        """Play a sequence of notes."""
        note_value = note_values[self.resolution].relative_value / self.note_duration
        for beat in pattern:
            if beat == '.':
                self.play_silence(duration=note_value)
            else:
                drum_name = [
                    drum.name for drum in self.drumkit.drums.values()
                    if drum.short_hand == beat
                    ][0]  # simplify
                self.play_drum(drum_name=drum_name, duration=note_value)

    def play_drum(self, drum_name, duration=0):
        """Send a drum MIDI note."""
        drum_note = self.drumkit.drums[drum_name].note
        self.play_note(note=drum_note, duration=duration)

    def play_note(self, note, duration=0, velocity=50):
        """Send a MIDI note."""
        msg = mido.Message('note_on',  note=note, velocity=velocity)
        self.outport.send(msg)
        time.sleep(duration)

    @staticmethod
    def play_silence(duration=0):
        """Play a silence of n duration."""
        time.sleep(duration)

    def play_bar(self, bar_):
        """Play a sequence of patterns."""
        self.play_pattern("".join(bar_.patterns))

    # LOOP
    def loop_bar(self, bar_, num_loops=1):
        """Iterate over a bar_."""
        for _ in range(num_loops):
            self.play_bar(bar_)

    def loop_bars(self, bars, num_loops=1):
        """Iterate over a sequence of bars_."""
        for _ in range(num_loops):
            for bar_ in bars:
                self.loop_bar(bar_)

    # GENERATE
    def generate_random_pattern(self, patt_len):
        """Generate_random_pattern."""
        abbvs = ["t", "h", "s", ".", "k", "c", "g", "v"]
        random_pattern = []
        for _ in range(patt_len):
            random_pattern.append(random.choice(abbvs))
        return random_pattern
