"""WavWriter"""

from scipy.io.wavfile import write
import numpy as np
from playsound import playsound


class WavWriter:
    def __init__(self, wav_name):
        self.wav_name = wav_name
        self.samplerate = 44100
        self.fs = 50  # ?
        self.t = np.linspace(1, 6, self.samplerate)  # ?
        self.amplitude = np.iinfo(np.int16).max  # ?
        self.x = np.sin(10 * np.pi * self.fs * self.t)  # ?
        self.data = self.amplitude * self.x  # ? s
        self.k = self.data.astype(np.int16)  # ?

    def write_wav(self):
        write(self.wav_name, self.samplerate, self.k)
        print('wrote wav')

    def play_wav(self):
        playsound(self.wav_name)


ss = WavWriter(wav_name='example.wav')
ss.write_wav()
ss.play_wav()
