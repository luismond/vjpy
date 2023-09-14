"""MIDI device class."""
import os
from collections import defaultdict
from playsound import playsound
from scipy.io import wavfile
from scipy.io.wavfile import write
import numpy as np


class WavDevice:
    """Audio device to manipulate wav files."""

    def __init__(self, vj):
        self.drumkit = vj.drumkit
        self.wav_dir = os.path.join("vjpy", "data", "wav")
        self.drumkit_dir = os.path.join(self.wav_dir, "drumkits", self.drumkit.name)
        self.drumkit_sh_names = vj.drumkit_sh_names
        self.drumkit_note_names = vj.drumkit_note_names
        self.note_value = vj.note_value

    def play_wav(self, filepath, block=False):
        """Play a wav file."""
        playsound(filepath, block=block)

    def concatenate_wavs(self, wav_paths, output_filename, play=False):
        """Concatenate an array of wavs."""
        wav_array = []
        for wav_path in wav_paths:
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        wav_concat = np.concatenate(wav_array)
        concat_wav_path = os.path.join(self.wav_dir, "examples", output_filename)
        self.write_wav(concat_wav_path, wav_concat)
        if play:
            self.play_wav(concat_wav_path)
        return wav_concat

    def write_wav(self, filepath, wav_object):
        """Write a wav file."""
        sample_rate = 44100
        write(filepath, sample_rate, wav_object)

    def mix_wavs(self, wav_paths, output_filename, play=False):
        """Mix an array of wavs."""
        wav_array = []
        for wav_path in wav_paths:
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        wav_mixed = wav_array[0]
        for wav in wav_array[1:]:
            wav_mixed += wav
        mixed_wav_path = os.path.join(self.wav_dir, "examples", output_filename)
        self.write_wav(mixed_wav_path, wav_mixed)
        if play:
            self.play_wav(mixed_wav_path)
        return wav_mixed

    def wav_patterns_to_steps(self, patterns):
        """Convert a list of pattern dictionaries to arrays of wav names."""
        steps = defaultdict(list)
        for pattern in patterns.values():
            for key in pattern:
                for _, step in enumerate(pattern[key]):
                    if step == "x":
                        wav_name = f"{self.drumkit_sh_names[key]}.wav"
                        steps[key].append(wav_name)
                    else:
                        steps[key].append("silence.wav")
        return steps

    def render_wav_steps(self, steps, output_filename, play=False):
        """Concatenate & mix wav files from a dictionary of wav names."""
        wavs_concat = []
        for dname, step in steps.items():
            wav_paths = [os.path.join(self.drumkit_dir, wn) for wn in step]
            wav_concat = self.concatenate_wavs(wav_paths, f"{dname}.wav")
            wavs_concat.append(wav_concat)

        wav_mixed = wavs_concat[0]
        for wav in wavs_concat[1:]:
            wav_mixed += wav
        mixed_wav_path = os.path.join(self.wav_dir, "examples", output_filename)
        self.write_wav(mixed_wav_path, wav_mixed)
        if play:
            self.play_wav(mixed_wav_path)
        return wav_mixed

    def render_midi_steps(self, steps, output_filename, play=False):
        """Mix & concatenate wav files from a dictionary of midi notes."""
        wavs_mixed = []
        for dname, step in steps.items():
            wav_list = [os.path.join(
                self.drumkit_dir,
                f"{self.drumkit_note_names[note]}.wav") for note in step]
            wav_mixed = self.mix_wavs(wav_list, f"{dname}.wav")
            wavs_mixed.append(wav_mixed)

        wav_concat = np.concatenate(wavs_mixed)
        concat_wav_path = os.path.join(self.wav_dir, "examples", output_filename)
        self.write_wav(concat_wav_path, wav_concat)
        if play:
            self.play_wav(concat_wav_path)
        return wav_concat
