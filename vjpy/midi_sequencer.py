"""vjpy midi sequencer."""

from time import sleep
import mido
from mido import Message
from vjpy import NoteValue
from vjpy import TR808EmulationKit


class MidiSequencer:
    """vjpy midi sequencer."""

    def __init__(self, bpm=120):
        self.outport = mido.open_output()
        self.bpm = bpm
        self.note_duration = self.bpm/60
        print(f"Sequencer instantiated. BPM: {self.bpm}\n")

    def play_note(self, note, duration=0, velocity=50):
        """
        Send a message to play a note.

        Parameters
        ----------
        note : int
            Midi note.
        duration : int, optional
            Note duration. The default is 0.
        velocity : int, optional
            Note velocity. The default is 50.

        Returns
        -------
        None.

        """
        msg = Message('note_on',  note=note, velocity=velocity)
        self.outport.send(msg)
        sleep(duration)

    def play_drum(self, drum_name, duration=0):
        """
        Send a message to play a drum note.

        Parameters
        ----------
        drum_name : str
            Name of the drum ("kick", "snare", etc.)
        duration : int, optional
            Note duration. The default is 0.

        Returns
        -------
        None.

        """
        drum_note = TR808EmulationKit.drums[drum_name].note
        self.play_note(note=drum_note, duration=duration)

    @staticmethod
    def play_silence(duration=0):
        """
        Play a silence.

        Parameters
        ----------
        duration : int, optional
            Silence duration. The default is 0.

        Returns
        -------
        None.

        """
        sleep(duration)

    def play_pattern(self, pattern):
        """
        Play a MIDI pattern.

        Parameters
        ----------
        pattern : str
            String representing a MIDI pattern (e.g. "khsh" is "kick-hat-snare-hat").

        Returns
        -------
        None.

        """
        res = '1/4'  # resolution
        note_value = self.note_values[res].relative_value / self.note_duration
        for beat in pattern:
            if beat != '|':
                if beat == '.':
                    self.play_silence(duration=note_value)
                else:
                    drum_name = [
                        drum.name for drum in TR808EmulationKit.drums.values()
                        if drum.short_hand == beat
                        ][0]  # simplify
                    self.play_drum(drum_name=drum_name, duration=note_value)

    def loop_bar(self, bar_, num_loops):
        """
        Iterate over a bar.

        Parameters
        ----------
        bar_ : vjpy.data_classes.Bar
            Musical bar (or measure).
        num_loops : int
            Number of iterations.

        Returns
        -------
        None.

        """
        for _ in range(num_loops):
            print(bar_)
            self.play_pattern("".join(bar_.patterns))

    def loop_bars(self, bars, num_loops):
        """
        Iterate over a sequence of bars.

        Parameters
        ----------
        bars : list
            List of bars.
        num_loops : int
            Number of iterations.

        Returns
        -------
        None.

        """
        for _ in range(num_loops):
            for bar_ in bars:
                self.loop_bar(bar_, 1)


    @property
    def note_values(self):
        """
        Dictionary representing note values.

        Returns
        -------
        note_values : dict
        Note values with names, and fraccional and float representations.

        """
        note_values = {
            '1': NoteValue(name='whole_note', relative_value=1.0),
            '1/2': NoteValue(name='half_note', relative_value=0.5),
            '1/4': NoteValue(name='quarter_note', relative_value=0.25),
            '1/8': NoteValue(name='eigth_note', relative_value=0.125),
            '1/16': NoteValue(name='sixteenth_note', relative_value=0.0625),
            '1/32': NoteValue(name='thirty-second_note', relative_value=0.03125)
            }
        return note_values
