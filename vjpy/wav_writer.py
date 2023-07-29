"""WavWriter"""

# %% scipy.io.wavfile

from scipy.io.wavfile import write
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from playsound import playsound
#%%
# write wav
# create a 100Hz sine wave, sampled at 44100Hz. 
# Write to 16-bit PCM, Mono.
wav_filename = 'wavs/example.wav'

samplerate = 44100
# The sampling frequency or sampling rate, fs, is the number of samples divided by the interval length over in which occur, thus fs = 1/T, with the unit sample per second, sometimes referred to as hertz, for example e.g. 48 kHz is 48,000 samples per second.

fs = 300 # Hz
# The hertz (symbol: Hz) is the unit of frequency in the International System of Units, equivalent to one cycle per second

amplitude = np.iinfo(np.int16).max
# In a standing wave, the amplitude of vibration has nulls at some positions where the wave amplitude appears smaller or even zero.

time = np.linspace(start=0., stop=1., num=samplerate)
# Returns num evenly spaced samples, calculated over the interval [start, stop].

# how to change the duration?
data = amplitude * np.sin(2 * np.pi * fs * time)
write(wav_filename, samplerate, data)
playsound(wav_filename)

# plot written wav
length = data.shape[0] / samplerate
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data)
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()


# %% read wav
wav_filename = 'wavs/my808kit/snare2.wav'
samplerate, data = wavfile.read(wav_filename)
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")

# write read wav
write(wav_filename+'test.wav', samplerate, data)

#  plot read wav
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# %% plot a sine with matplotlib and numpy

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
