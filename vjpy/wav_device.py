"""MIDI device class."""
import os
import time
from playsound import playsound
from scipy.io import wavfile
from scipy.io.wavfile import write
import numpy as np


class WavDevice:
    """Audio device to manipulate wav files."""

    def __init__(self,
                 drumkit_sh_names,
                 drumkit_note_names,
                 resolution,
                 bpm,
                 note_values):
        self.drumkit = "myfunkkit"
        self.sample_rate = 44100
        self.wav_dir = os.path.join("vjpy", "data", "wav")
        self.drumkit_sh_names = drumkit_sh_names
        self.drumkit_note_names = drumkit_note_names
        
        self.bpm = bpm
        self.note_values = note_values
        self.note_duration = self.bpm/60
        self.resolution = resolution
        self.note_value = self.note_values[resolution].relative_value / self.note_duration

    def play_wav(self, filepath):
        """Play a wav file."""
        print(f"\nPlaying {filepath} wav file.")
        playsound(filepath)

    def write_wav(self, filepath, wav_object):
        """Write a wav file."""
        write(filepath, self.sample_rate, wav_object)
        print(f"\nWav file written to {filepath}.")

    def concatenate_wavs(self, wav_list):
        """Concatenate an array of wavs."""
        wav_array = []
        for wav_path in wav_list:
            _, data = wavfile.read(wav_path)
            wav_array.append(data)
        print("\nWav file concatenation completed.")
        return np.concatenate(wav_array)

    def mix_wavs(self, wav_list):
        """Mix an array of wavs."""
        wav_array = []
        for wav_path in wav_list:
            _, data = wavfile.read(wav_path)
            wav_array.append(data)

        wav_mixed = wav_array[0]
        for wav in wav_array[1:]:
            wav_mixed += wav
        return wav_mixed

    def parse_wav_patterns(self, patterns):
        steps = self.wav_patterns_to_steps(patterns)
        wav_concat = self.concat_wav_steps(steps)
        return wav_concat

    def parse_midi_steps(self, steps):
        for step in steps.values():
            for note in step:
                if note == 0:
                    pass
                else:
                    wav = f"{self.drumkit_note_names[note]}.wav"
                    wav_path = os.path.join(self.wav_dir, "drumkits", self.drumkit, wav)
                playsound(wav_path, block=False)
            time.sleep(self.note_value)

    def wav_patterns_to_steps(self, patterns):
        """Concatenate and mix a drum pattern."""
        for pattern in patterns.values(): # todo: make sure to add all patterns' hits
            steps = {1: [], 2: [], 3: [], 4: [],
                     5: [], 6: [], 7: [], 8: []}
            for key in pattern:
                for step, hit in enumerate(pattern[key]):
                    if hit == "x":
                        wav = f"{self.drumkit_sh_names[key]}.wav"
                        steps[step+1].append(wav)
                    else:
                        steps[step+1].append("silence.wav")
            return steps
        
    def concat_wav_steps(self, steps):
        wavs_mixed = []
        for _, step in steps.items():
            wav_list = [os.path.join(
                self.wav_dir, "drumkits", self.drumkit, wn) for wn in step]
            wav_mixed = self.mix_wavs(wav_list)
            wavs_mixed.append(wav_mixed)
        wav_concat = np.concatenate(wavs_mixed)
        return wav_concat

    def concat_wav_midi_steps(self, steps):
        wavs_mixed = []
        for _, step in steps.items():
            wav_list = [os.path.join(
                self.wav_dir, "drumkits", self.drumkit,
                f"{self.drumkit_note_names[note]}.wav") for note in step]
            wav_mixed = self.mix_wavs(wav_list)
            wavs_mixed.append(wav_mixed)
        wav_concat = np.concatenate(wavs_mixed)
        return wav_concat
