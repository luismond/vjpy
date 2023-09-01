"""vjpy backend."""

import os
import time
import random
import mido
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write
from playsound import playsound
from vjpy import Bar, Pattern, Drumkit, Drum, NoteValue
from moviepy.editor import (
    VideoFileClip,
    CompositeVideoClip,
    concatenate_videoclips
    )


class VjPyDevice:
    """vjpy device."""

    # INIT AND PROPERTIES
    def __init__(self,
                 bpm=90,
                 resolution="1/4"
                 ):
        self.sample_rate = 44100
        self.bpm = bpm
        self.resolution = resolution
        self.my_drumkit = self.get_my_drumkit()

    # NOTE DURATIONS & VALUES
    @property
    def note_duration(self):
        """Note duration expressed in seconds."""
        return self.bpm/60

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


    # I/O
    @property
    def midi_in(self):
        """MIDI in."""
        return mido.open_input()

    @property
    def midi_out(self):
        """MIDI out."""
        return mido.open_output()

    def yield_midi_msg(self):
        """Yield MIDI messages from a MIDI in port."""
        for midi_msg in self.midi_in:
            yield midi_msg

    def send_note(self, note):
        """Send a MIDI note through a MIDI out port."""
        self.midi_out.send(mido.Message('note_on', note=note))

    # DRUMS
    @property
    def drumkit_sh_names(self):
        """Mapping short-hand-names <-> full-names."""
        drumkit_sh_names = {}
        for drum in self.my_drumkit.drums.values():
            drumkit_sh_names[drum.short_hand] = drum.name
        return drumkit_sh_names

    @property
    def drumkit_note_names(self):
        """Mapping notes <-> note names."""
        drumkit_note_names = {}
        for drum in self.my_drumkit.drums.values():
            drumkit_note_names[drum.note] = drum.name
        return drumkit_note_names
    
    def play_drum(self, drum_name, duration=0):
        """Send a drum MIDI note."""
        drum_note = self.my_drumkit.drums[drum_name].note
        self.play_note(note=drum_note, duration=duration)

    def get_my_drumkit(self):
        """Temp 'my drumkit' object."""
        mydrumkit = Drumkit(
        name='MyDrumKit',
        drums={
            'kick': Drum(name='kick', note=43, short_hand='k'),
            'hat': Drum(name='hat', note=38, short_hand='h'),
            'clap': Drum(name='clap', note=40, short_hand='c')
            }
        )
        return mydrumkit

    @staticmethod
    def play_silence(duration=0):
        """Play a silence of n duration."""
        time.sleep(duration)    
    
    # PATTERNS & BARS
    @property
    def pattern_example(self):
        return Pattern(pattern='k.h.sshhh.s.s.k.')
    
    @property
    def bar_example(self):
        return Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh'])

    @property
    def bars_example(self):
        bars_example = [
            Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
            Bar(bar_num=2, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
            Bar(bar_num=3, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
            Bar(bar_num=4, patterns=['k.h.', 'chhh', 'hhhh', 'cccc'])
        ]
        return bars_example


    def play_pattern(self, pattern):
        """Play a sequence of notes."""
        note_value = self.note_values[self.resolution].relative_value \
            / self.note_duration
        for beat in pattern:
            if beat == '.':
                self.play_silence(duration=note_value)
            else:
                drum_name = self.drumkit_sh_names[beat]
                self.play_drum(drum_name=drum_name, duration=note_value)

    def play_note(self, note, duration=0, velocity=50):
        """Send a MIDI note."""
        msg = mido.Message('note_on', note=note, velocity=velocity)
        self.midi_out.send(msg)
        time.sleep(duration)

    def play_bar(self, bar_):
        """Play a sequence of patterns."""
        self.play_pattern("".join(bar_.patterns))

    def loop_bar(self, bar_, num_loops=1):
        """Iterate over a bar_."""
        for _ in range(num_loops):
            self.play_bar(bar_)

    def loop_bars(self, bars, num_loops=1):
        """Iterate over a sequence of bars_."""
        for _ in range(num_loops):
            for bar_ in bars:
                self.loop_bar(bar_)

    def generate_random_pattern(self, patt_len):
        """Generate_random_pattern."""
        abbvs = ["k", "h", "c"]
        random_pattern = []
        for _ in range(patt_len):
            random_pattern.append(random.choice(abbvs))
        return random_pattern

    def play_drum_wav_from_midi_msg(self, midi_msg):
        """Play a drum wav file associated with a midi message."""
        wav_name = self.drumkit_note_names[midi_msg.note]
        playsound(f"{DRUMKIT_PATH}/{wav_name}.wav")

    def write_concatenated_wavs(self, shs):#notes):
        """
        1. Take integers or shorthands, pass them as MIDI notes to mido.
        2. Associate them with wav file paths.
        3. Concatenate resulting wav files.
        4. Write and play resulting concatenated wav.
        """
        #msgs = [mido.Message('note_on', note=note) for note in notes]
        wav_array = []
        for sh in shs:
        #for msg in msgs:
            wav_name = f"{self.drumkit_sh_names[sh]}.wav"
            #wav_name = f"{self.drumkit_note_names[msg.note]}.wav"
            wav_path = f"vjpy/data/wav/drumkits/myfunkkit/{wav_name}"
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        wav_array_c = np.concatenate(wav_array)
        wav_array_c_name = "vjpy/data/wav/wav_examples/concat.wav"
        write(wav_array_c_name, self.sample_rate, wav_array_c)
        playsound(wav_array_c_name)

    ## Video methods

    def get_video_clip(self, video_filename):
        return VideoFileClip(video_filename)
    
    def get_video_subclip(self, video_clip, start=0, duration=.075):
        return video_clip.subclip(start, start + duration)
    
    def concatenate_subclips(self, subclips):
        return concatenate_videoclips(subclips)
    
    # todo: implement compositing
    #from moviepy.editor import clips_array, CompositeVideoClip

    # c_subclips = CompositeVideoClip(
    #     [
    #      k.set_position((300, 0)),
    #      m.set_position((400, 50)),
    #      g.set_position((500, 100))
    #      ]
    #     )
    
    def write_concatenated_subclips(self, concatenated_subclips, subclip_name):
        concatenated_subclips.write_videofile(subclip_name)
