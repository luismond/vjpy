"""MIDI device class."""

import os
import time
from collections import defaultdict
import mido
import pretty_midi

class MidiDevice:
    """MIDI device."""

    def __init__(self, vj):
        self.midi_out = mido.open_output()
        self.midi_data_dir = os.path.join("vjpy", "data", "midi")
        self.note_value = vj.note_value

    def play_midi_file(self, filename):
        """Parse and play a MIDI file."""
        steps = self.parse_midi_file(filename)
        for step in steps.values():
            for note in step:
                if note == 0:
                    msg = mido.Message("note_off", note=note, velocity=120)
                else:
                    msg = mido.Message("note_on", note=note, velocity=120)
                self.midi_out.send(msg)
            time.sleep(self.note_value)
    
    def parse_midi_file(self, filename):
        """Read a MIDI file and get the notes of each step."""
        midi_messages = self.get_sorted_midi_messages(filename)
        steps = self.midi_messages_to_steps(midi_messages)
        return steps
    
    @staticmethod
    def get_sorted_midi_messages(filename):
        '''Get a sorted array of midi messages.'''
        midi_data = pretty_midi.PrettyMIDI(filename)
        midi_messages = []
        for instrument in midi_data.instruments:
            for note in instrument.notes:
                start = note.start
                end = note.end
                pitch = note.pitch
                velocity = note.velocity
                midi_messages.append([start, end, pitch, velocity, instrument.name])
        midi_messages = sorted(midi_messages, key=lambda x: (x[0], x[2]))
        return midi_messages
    
    def midi_messages_to_steps(self, midi_messages):
        '''Convert sorted midi messages to stepped array.'''
        first = midi_messages[0][0]
        last = midi_messages[-1][0]+self.note_value
        steps_range = [i/1000 for i in list(range(round(first*1000),
                                                  round(last*1000),
                                                  round(self.note_value*1000)))]
        steps = defaultdict(list)
        for step in steps_range:
            steps[step] = []
        
        for msg in midi_messages:
            start = msg[0]
            pitch = msg[2]
            steps[start].append(pitch)
        
        return steps
       