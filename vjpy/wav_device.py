"""vjpy wav device."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.io import wavfile
from playsound import playsound
from vjpy.drumkits import get_my808kit_paths


class WavDevice:
    """vjpy wav device to write, read and play wavs."""

    def __init__(self):
        self.sound_paths = get_my808kit_paths()
        pass

    def play_wav_from_midi_msg(self, midi_msg):
        """Play a wav file associated with a midi message."""
        wav_name = self.sound_paths[midi_msg.note]
        print(f"Playing: {midi_msg}\n{wav_name}\n\n")
        playsound(wav_name)

    @staticmethod
    def create_sine_wave():
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
        WAV_FILENAME = 'wavs/sine_wave_example.wav'
        SAMPLE_RATE = 44100
        FS = 300  # Hz
        amplitude = np.iinfo(np.int16).max
        time = np.linspace(start=0., stop=1., num=SAMPLE_RATE)
        data = amplitude * np.sin(2 * np.pi * FS * time)
        write(WAV_FILENAME, SAMPLE_RATE, data)

        # play wav
        input("This will play a loud sinewave! Continue?")
        playsound(WAV_FILENAME)

        # plot wav
        length = data.shape[0] / SAMPLE_RATE
        time = np.linspace(0., length, data.shape[0])
        plt.plot(time, data)
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

    @staticmethod
    def test_wav_reading():
        """Read a wav, rewrite it, plot it."""
        WAV_FILENAME = 'wavs/my808kit/snare.wav'
        SAMPLE_RATE, data = wavfile.read(WAV_FILENAME)
        print(f"number of channels = {data.shape[1]}")
        length = data.shape[0] / SAMPLE_RATE
        print(f"length = {length}s")

        # re-write read wav
        write(f"{WAV_FILENAME}_test.wav", SAMPLE_RATE, data)

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
        x = np.linspace(-np.pi, np.pi, 201)
        plt.plot(x, np.sin(x))
        plt.xlabel('Angle [rad]')
        plt.ylabel('sin(x)')
        plt.axis('tight')
        plt.show()

    @staticmethod
    def write_concatenated_wavs():
        """Take a wav file, concatenate it n times, write the result."""
        kit_path = "wavs/myfunkkit"
        wav_array_c_name = "wavs/concat.wav"
        sample_rate = 44100

        # read wav files, store them in an array
        wav_array = []
        for _ in range(4):
            _, data = wavfile.read(f"{kit_path}/kick.wav")
            wav_array.append(data)
            _, data = wavfile.read(f"{kit_path}/hat.wav")
            wav_array.append(data)
            _, data = wavfile.read(f"{kit_path}/clap.wav")
            wav_array.append(data)
            _, data = wavfile.read(f"{kit_path}/hat.wav")
            wav_array.append(data)

        # concatenate wavs
        wav_array_c = np.concatenate(wav_array)

        # write concatenated wav
        write(wav_array_c_name, sample_rate, wav_array_c)

        # play concatenated wav
        playsound(wav_array_c_name)
