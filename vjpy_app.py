"""vjpy backend."""

import os
import time
import random
import mido
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write
from playsound import playsound
from pydantic import BaseModel

DRUMKIT_PATH = os.environ.get("LOCAL_DRUMKIT_PATH")
WAV_ARRAY_C_NAME = os.environ.get("WAV_ARRAY_C_NAME")

class MidiDevice:
    """vjpy midi device."""

    def __init__(self, drumkit, dd_shorthands, bpm=90,
                 resolution="1/4"):
        self.drumkit = drumkit
        self.bpm = bpm
        self.resolution = resolution
        self.dd_shorthands = dd_shorthands

    @property
    def note_duration(self):
        return self.bpm/60

    # I/O
    @property
    def outport(self):
        return mido.open_output()
  
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
                drum_name = self.dd_shorthands[beat]
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
        abbvs = ["k", "h", "c"]
        random_pattern = []
        for _ in range(patt_len):
            random_pattern.append(random.choice(abbvs))
        return random_pattern

class WavDevice:
    """vjpy wav device to write, read and play wavs."""

    def __init__(self, drumkit):
        self.sample_rate = 44100
        self.drumkit = drumkit

    def play_drum_wav_from_midi_msg(self, drum_midi_notes_to_names, midi_msg):
        """Play a drum wav file associated with a midi message."""
        wav_name = drum_midi_notes_to_names[midi_msg.note]
        playsound(DRUMKIT_PATH+"/"+wav_name+".wav")

    def write_concatenated_wavs(self, drum_midi_notes_to_names, notes):
        """Take a wav file, concatenate it, write the result."""
        wav_array = []
        msgs = [mido.Message('note_on', note=note) for note in notes]
        for msg in msgs:
            wav_path = DRUMKIT_PATH + "/" + drum_midi_notes_to_names[msg.note] + ".wav"
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        wav_array_c = np.concatenate(wav_array)
        write(WAV_ARRAY_C_NAME, self.sample_rate, wav_array_c)
        playsound(WAV_ARRAY_C_NAME)


# Classes
class Bar(BaseModel):
    """Musical measure containing patterns."""

    bar_num: int
    patterns: list[str]


class Pattern(BaseModel):
    """Pattern."""

    pattern: str


class Drumkit(BaseModel):
    """Object representing a collection of drums."""

    name: str
    drums: dict


class Drum(BaseModel):
    """Object representing a drum (with name, note, shorthand)."""

    name: str
    note: int
    short_hand: str


class NoteValue(BaseModel):
    """Object representing a note value."""

    name: str
    relative_value: float


TR808EmulationKit = Drumkit(
    name='TR808EmulationKit',
    drums={
        'kick': Drum(name='kick', note=36, short_hand='k'),
        'snare': Drum(name='snare', note=38, short_hand='s'),
        'clap': Drum(name='clap', note=40, short_hand='c'),
        'tom': Drum(name='tom', note=43, short_hand='t'),
        'hat': Drum(name='hat', note=45, short_hand='h'),
        'conga': Drum(name='conga', note=49, short_hand='g'),
        'clave': Drum(name='clave', note=50, short_hand='v'),
        'cowbell': Drum(name='cowbell', note=51, short_hand='w'),
        }
    )


My808kit = Drumkit(
    name='my808kit',
    drums={
        'bongo': Drum(name='bongo', note=36, short_hand='b'),
        'conga': Drum(name='conga', note=38, short_hand='g'),
        'crash': Drum(name='crash', note=40, short_hand='x'),
        'hat': Drum(name='hat', note=43, short_hand='h'),
        'kick': Drum(name='kick', note=45, short_hand='k'),
        'ride': Drum(name='ride', note=49, short_hand='r'),
        'snare': Drum(name='snare', note=50, short_hand='c'),
        'snare2': Drum(name='snare2', note=51, short_hand='z'),
        'tom': Drum(name='tom', note=51, short_hand='t')
        }
    )

MyFunkKit = Drumkit(
    name='MyFunkKit',
    drums={
        'kick': Drum(name='kick', note=43, short_hand='k'),
        'hat': Drum(name='hat', note=38, short_hand='h'),
        'clap': Drum(name='clap', note=40, short_hand='c')
        }
    )

# Pattern examples

pattern_example_0 = Pattern(pattern='k.h.sshhh.s.s.k.')
pattern_examples = [pattern_example_0]

# Bar example
bar_example = Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh'])

# Bars example
bars_example = [
    Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=2, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
    Bar(bar_num=3, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=4, patterns=['k.h.', 'chhh', 'hhhh', 'cccc'])
]


note_values = {
    '1': NoteValue(name='whole_note', relative_value=1.0),
    '1/2': NoteValue(name='half_note', relative_value=0.5),
    '1/4': NoteValue(name='quarter_note', relative_value=0.25),
    '1/8': NoteValue(name='eigth_note', relative_value=0.125),
    '1/16': NoteValue(name='sixteenth_note', relative_value=0.0625),
    '1/32': NoteValue(name='thirty-second_note', relative_value=0.03125)
    }


# from moviepy.editor import VideoFileClip, CompositeVideoClip

# VIDEO_NAME = ""
# VIDEO = VideoFileClip(VIDEO_NAME).subclip(0, 2)
# result = CompositeVideoClip([VIDEO])
# result.write_videofile(f"{VIDEO_NAME}_test.webm", fps=10)

# """Wav utils to learn more about the wav format."""

# import os
# import numpy as np
# from scipy.io import wavfile
# from scipy.io.wavfile import write
# import matplotlib.pyplot as plt
# from dotenv import load_dotenv
# load_dotenv()

# SINE_WAVE_EXAMPLE_FILEPATH = os.environ.get("SINE_WAVE_EXAMPLE_FILEPATH")
# SNARE_WAV_FILEPATH = os.environ.get("SNARE_WAV_FILEPATH")


# def create_sine_wave():
#     """
#     Write and plot a wave.

#     100Hz sine wave, sampled at 44100Hz.
#     Write to 16-bit PCM, Mono.
#     Plot with matplotlib

#     linspace returns num evenly spaced samples,
#     calculated over the interval [start, stop].
#     Todo: find out how to change the duration.
#     """
#     # write wav
#     sample_rate = 44100
#     fs_var = 300  # Hz
#     amplitude = np.iinfo(np.int16).max
#     time = np.linspace(start=0., stop=1., num=sample_rate)
#     data = amplitude * np.sin(2 * np.pi * fs_var * time)
#     write(SINE_WAVE_EXAMPLE_FILEPATH, sample_rate, data)

#     # play wav
#     # input("This will play a loud sinewave! Continue?")
#     # playsound(SINE_WAVE_EXAMPLE_FILEPATH)

#     # plot wav
#     length = data.shape[0] / sample_rate
#     time = np.linspace(0., length, data.shape[0])
#     plt.plot(time, data)
#     plt.legend()
#     plt.xlabel("Time [s]")
#     plt.ylabel("Amplitude")
#     plt.show()


# def test_wav_reading():
#     """Read a wav, rewrite it, plot it."""
#     sample_rate, data = wavfile.read(SNARE_WAV_FILEPATH)
#     print(f"number of channels = {data.shape[1]}")
#     length = data.shape[0] / sample_rate
#     print(f"length = {length}s")

#     # re-write read wav
#     write(f"{SNARE_WAV_FILEPATH}_test.wav", sample_rate, data)

#     #  plot read wav
#     time = np.linspace(0., length, data.shape[0])
#     plt.plot(time, data[:, 0], label="Left channel")
#     plt.plot(time, data[:, 1], label="Right channel")
#     plt.legend()
#     plt.xlabel("Time [s]")
#     plt.ylabel("Amplitude")
#     plt.show()


# def plot_sine():
#     """Plot a sine with matplotlib and numpy."""
#     equis_var = np.linspace(-np.pi, np.pi, 201)
#     plt.plot(equis_var, np.sin(equis_var))
#     plt.xlabel('Angle [rad]')
#     plt.ylabel('sin(equis_var)')
#     plt.axis('tight')
#     plt.show()


# create_sine_wave()
# test_wav_reading()
# plot_sine()
