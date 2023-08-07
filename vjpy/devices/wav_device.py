"""vjpy wav device."""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.io import wavfile
from playsound import playsound
from dotenv import load_dotenv
load_dotenv()

LOCAL_DRUMKIT_PATH = os.environ.get("LOCAL_DRUMKIT_PATH")
SINE_WAVE_EXAMPLE_FILEPATH = os.environ.get("SINE_WAVE_EXAMPLE_FILEPATH")
SNARE_WAV_FILEPATH = os.environ.get("SNARE_WAV_FILEPATH")
FUNK_KIT_PATH = os.environ.get("FUNK_KIT_PATH")
WAV_ARRAY_C_NAME = os.environ.get("WAV_ARRAY_C_NAME")


class WavDevice:
    """vjpy wav device to write, read and play wavs."""

    def __init__(self):
        self.sample_rate = 44100
        pass

    @staticmethod
    def get_local_drumkit_paths(drumkit):
        """Get local drumkit drum paths."""
        local_drumkit_paths = {}
        for drum in drumkit.drums.values():
            local_drumkit_paths[drum.note] = f"{LOCAL_DRUMKIT_PATH}/{drum.name}.wav"
        return local_drumkit_paths

    def play_drum_wav_from_midi_msg(self, drumkit, midi_msg):
        """Play a drum wav file associated with a midi message."""
        local_drumkit_paths = self.get_local_drumkit_paths(drumkit)
        wav_name = local_drumkit_paths[midi_msg.note]
        playsound(wav_name)

    def create_sine_wave(self):
        """
        Write and plot a wave.

        100Hz sine wave, sampled at 44100Hz.
        Write to 16-bit PCM, Mono.
        Plot with matplotlib

        linspace returns num evenly spaced samples,
        calculated over the interval [start, stop].
        Todo: find out how to change the duration.
        """
        # write wav
        fs_var = 300  # Hz
        amplitude = np.iinfo(np.int16).max
        time = np.linspace(start=0., stop=1., num=self.sample_rate)
        data = amplitude * np.sin(2 * np.pi * fs_var * time)
        write(SINE_WAVE_EXAMPLE_FILEPATH, self.sample_rate, data)

        # play wav
        # input("This will play a loud sinewave! Continue?")
        # playsound(SINE_WAVE_EXAMPLE_FILEPATH)

        # plot wav
        length = data.shape[0] /self.sample_rate
        time = np.linspace(0., length, data.shape[0])
        plt.plot(time, data)
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

    @staticmethod
    def test_wav_reading():
        """Read a wav, rewrite it, plot it."""
        sample_rate, data = wavfile.read(SNARE_WAV_FILEPATH)
        print(f"number of channels = {data.shape[1]}")
        length = data.shape[0] / sample_rate
        print(f"length = {length}s")

        # re-write read wav
        write(f"{SNARE_WAV_FILEPATH}_test.wav", sample_rate, data)

        #  plot read wav
        time = np.linspace(0., length, data.shape[0])
        plt.plot(time, data[:, 0], label="Left channel")
        plt.plot(time, data[:, 1], label="Right channel")
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

    @staticmethod
    def plot_sine():
        """Plot a sine with matplotlib and numpy."""
        equis_var = np.linspace(-np.pi, np.pi, 201)
        plt.plot(equis_var, np.sin(equis_var))
        plt.xlabel('Angle [rad]')
        plt.ylabel('sin(equis_var)')
        plt.axis('tight')
        plt.show()

    def write_concatenated_wavs(self, sound_names):
        """Take a wav file, concatenate it n times, write the result."""
        wav_array = []
        for _ in range(4):
            for sn in sound_names:
                wav_name = f"{FUNK_KIT_PATH}/{sn}.wav"
                _, data = wavfile.read(wav_name)
                wav_array.append(data)

        wav_array_c = np.concatenate(wav_array) # concatenate wavs
        write(WAV_ARRAY_C_NAME, self.sample_rate, wav_array_c) # write concatenated wav
        playsound(WAV_ARRAY_C_NAME) # play concatenated wav
