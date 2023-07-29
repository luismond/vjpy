"""WavWriter"""

# %% scipy.io.wavfile

from scipy.io.wavfile import write
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# write wav
# create a 100Hz sine wave, sampled at 44100Hz. Write to 16-bit PCM, Mono.
wav_filename = 'wavs/example.wav'
samplerate = 22050
fs = 250
t = np.linspace(10, 1.2, samplerate)
amplitude = np.iinfo(np.int16).max
data = amplitude * np.sin(2. * np.pi * fs * t)
write(wav_filename, samplerate, data.astype(np.int16))

# %% read wav
wav_filename = 'wavs/my808kit/snare2.wav'
samplerate, data = wavfile.read(wav_filename)
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")

# plot wav
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# %% play wav

from playsound import playsound
playsound(wav_filename)

# %% plot a sine with matplotlib and numpy

import matplotlib.pylab as plt
x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

# %% numpy.linspace
'''
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)[source]

Return evenly spaced numbers over a specified interval.

Returns num evenly spaced samples, calculated over the interval [start, stop].

The endpoint of the interval can optionally be excluded.
'''

from numpy import array
np.linspace(2.0, 3.0, num=5)
array([2.  , 2.25, 2.5 , 2.75, 3.  ])
np.linspace(2.0, 3.0, num=5, endpoint=False)
array([2. ,  2.2,  2.4,  2.6,  2.8])
np.linspace(2.0, 3.0, num=5, retstep=True)
(array([2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)


import matplotlib.pyplot as plt
N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)
plt.plot(x1, y, 'o')

plt.plot(x2, y + 0.5, 'o')

plt.ylim([-0.5, 1])
(-0.5, 1)
plt.show()