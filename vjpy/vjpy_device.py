"""vjpy backend."""

import os
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write
from playsound import playsound
from vjpy import Drumkit, Drum, NoteValue, MidiDevice # Bar, Pattern,
from moviepy.editor import (
    VideoFileClip,
    CompositeVideoClip,
    concatenate_videoclips,
    clips_array,
    vfx
    )
from moviepy.audio.fx.all import volumex


class VjPyDevice:
    """vjpy device."""

    def __init__(self, bpm=90):
        self.bpm = bpm
        self.midi_device = MidiDevice(
            bpm=self.bpm,
            drumkit=self.drumkit,
            note_values=self.note_values,
            drumkit_sh_names=self.drumkit_sh_names
            )
        self.wav_device = WavDevice(
            drumkit_note_names=self.drumkit_note_names,
            drumkit_sh_names=self.drumkit_sh_names
            )
        self.video_device = VideoDevice()

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
    def drumkit(self):
        """Sample drumkit object."""
        drumkit = Drumkit(
            name='MyDrumKit',
            drums={
                'kick1': Drum(name='kick', note=36, short_hand='k'),
                'kick2': Drum(name='kick', note=37, short_hand='q'),
                'snare1': Drum(name='kick', note=38, short_hand='s'),
                'snare2': Drum(name='kick', note=39, short_hand='z'),
                'clap1': Drum(name='kick', note=40, short_hand='c'),
                'tom1': Drum(name='kick', note=41, short_hand='t'),
                'tom2': Drum(name='kick', note=42, short_hand='u'),
                'tom3': Drum(name='kick', note=43, short_hand='v'),
                'hat1': Drum(name='kick', note=44, short_hand='h'),
                'hatp': Drum(name='kick', note=45, short_hand='i'),
                'hato': Drum(name='kick', note=46, short_hand='o'),

                }
            )
        return drumkit

    @property
    def drumkit_sh_names(self):
        """Mapping short-hand-names <-> full-names."""
        drumkit_sh_names = {}
        for drum in self.drumkit.drums.values():
            drumkit_sh_names[drum.short_hand] = drum.name
        return drumkit_sh_names

    @property
    def drumkit_note_names(self):
        """Mapping notes <-> note names."""
        drumkit_note_names = {}
        for drum in self.drumkit.drums.values():
            drumkit_note_names[drum.note] = drum.name
        return drumkit_note_names


class WavDevice:
    """Audio device to manipulate wav files."""

    def __init__(self, drumkit_note_names, drumkit_sh_names):
        self.sample_rate = 44100
        self.drumkit_note_names = drumkit_note_names
        self.drumkit_sh_names = drumkit_sh_names

    def play_drum_wav_from_midi_msg(self, midi_msg):
        """Play a drum wav file associated with a midi message."""
        wav_name = self.drumkit_note_names[midi_msg.note]
        playsound(f"vjpy/data/wav/drumkits/myfunkkit/{wav_name}.wav")

    def write_concatenated_wavs(self, shs):  # notes):
        """
        1. Take integers or shorthands, pass them as MIDI notes to mido.

        2. Associate them with wav file paths.
        3. Concatenate resulting wav files.
        4. Write and play resulting concatenated wav.
        """
        # msgs = [mido.Message('note_on', note=note) for note in notes]
        wav_array = []
        for sh in shs:  # for msg in msgs:
            wav_name = f"{self.drumkit_sh_names[sh]}.wav"
            # wav_name = f"{self.drumkit_note_names[msg.note]}.wav"
            wav_path = f"vjpy/data/wav/drumkits/myfunkkit/{wav_name}"
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        wav_array_c = np.concatenate(wav_array)
        wav_array_c_name = "vjpy/data/wav/wav_examples/concat.wav"
        write(wav_array_c_name, self.sample_rate, wav_array_c)
        playsound(wav_array_c_name)
        
class VideoDevice:
    def __init__(self):
        self.soundbanks_path = os.path.join('soundbanks')
        
    def get_videoclip(self, video_filename):
        return VideoFileClip(video_filename)
    
    def get_videosubclip(self, video_clip, start=0, duration=.075):
        return video_clip.subclip(start, start + duration)
    
    def concatenate_subclips(self, subclips):
        return concatenate_videoclips(subclips)
    
    def get_bars_subclips(self, bars):
        subclips = []
        for bar_ in bars:
            for patt in bar_:
                for subclip in patt:
                    subclips.append(subclip)
        return subclips

    def write_concatenated_subclips(self, concatenated_subclips, subclip_name):
        concatenated_subclips.write_videofile(subclip_name)
        
    # todo: implement compositing
