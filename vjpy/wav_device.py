"""MIDI device class."""
import os
import time
import librosa
from playsound import playsound
from scipy.io import wavfile
from scipy.io.wavfile import write
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


class WavDevice:
    """Audio device to manipulate wav files."""

    def __init__(self, vj):
        self.wav_dir = os.path.join("vjpy", "data", "wav")
        self.drumkit = vj.drumkit
        self.drumkit_dir = os.path.join(self.wav_dir, "drumkits", self.drumkit.name)
        self.note_value = vj.note_value
        self.sample_rate = 44100
        self.frames_duration = round(self.sample_rate*self.note_value)
        self.drumkit_note_names = vj.drumkit_note_names

    def play_wav(self, filepath, block=True):
        """Play a wav file."""
        playsound(filepath, block=block)

    def concatenate_wavs(self, wav_paths):
        """Concatenate an array of wavs."""
        wav_array = []
        for wav_path in wav_paths:
            _, data = wavfile.read(wav_path)
            wav_array.append(data[:self.frames_duration])
        wav_concat = np.concatenate(wav_array)
        return wav_concat

    def write_wav(self, filepath, wav_object):
        """Write a wav file."""
        write(filepath, self.sample_rate, wav_object)

    def mix_wavs(self, wav_paths):
        """Mix an array of wavs."""
        wav_array = []
        for wav_path in wav_paths:
            _, data = wavfile.read(wav_path)
            wav_array.append(data[:self.frames_duration])
        wav_mixed = wav_array[0]
        for wav in wav_array[1:]:
            wav_mixed += wav
        return wav_mixed

    def render_midi_steps(self, steps):
        """Mix & concatenate wav files from a dictionary of midi notes."""
        wavs_mixed = []
        for _, step in steps.items():
            # for note in step:
            #     print(note)
            #     self.play_wav(os.path.join(
            #         self.drumkit_dir,
            #         f"{self.drumkit_note_names[note]}.wav"
            #         )
            #         )
            wav_list = [os.path.join(
                self.drumkit_dir,
                f"{self.drumkit_note_names[note]}.wav") for note in step]

            wav_mixed = self.mix_wavs(wav_list)
            wavs_mixed.append(wav_mixed)
        wav_concat = np.concatenate(wavs_mixed)
        return wav_concat

    def find_local_energy_peaks(self, filepath, prominence=3):
        """Find local energy peaks."""
        wav_object, _ = librosa.load(filepath)
        N = 2048
        w = signal.hann(N)
        x_square = wav_object**2
        energy_local = np.convolve(x_square, w**2, 'same')
        peaks = signal.find_peaks(energy_local, prominence=prominence)[0]
        return peaks

    def play_peaks(self, filepath, sample_rate, peaks):
        """Play wav energy peaks."""
        wav_object, _ = librosa.load(filepath)
        for peak in peaks:
            wav_chunk = wav_object[peak-500:peak+7000]
            self.plot_wav(wav_chunk)
            write('test.wav', sample_rate, wav_chunk)
            self.play_wav('test.wav', block=True)
            time.sleep(.5)
        os.remove("test.wav")

    def plot_wav(self, wav_object):
        """Plot wav object."""
        length = wav_object.shape[0] / self.sample_rate
        time_ = np.linspace(0., length, wav_object.shape[0])
        plt.figure(figsize=(8, 1))
        x = time_
        plt.xticks(np.arange(min(x), max(x)+1, 0.2))
        plt.plot(time_, wav_object, label="data")
        plt.legend()
        plt.xlabel("Time [s]", fontsize=8)
        plt.ylabel("Amplitude")
        plt.show()

    @staticmethod
    def wav_stereo_to_mono(wav_object):
        """Wav stereo to mono."""
        return np.int16(wav_object.sum(axis=1) / 2)
