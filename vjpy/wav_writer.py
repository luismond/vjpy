"""vjpy WavWriter."""

#  scipy.io.wavfile

from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from playsound import playsound

#
# write wav
# create a 100Hz sine wave, sampled at 44100Hz.
# Write to 16-bit PCM, Mono.
WAV_FILENAME = 'wavs/example.wav'

SAMPLE_RATE = 44100

FS = 300  # Hz

amplitude = np.iinfo(np.int16).max

time = np.linspace(start=0., stop=1., num=SAMPLE_RATE)
# Returns num evenly spaced samples, calculated over the interval [start, stop].

# how to change the duration?
data = amplitude * np.sin(2 * np.pi * FS * time)
write(WAV_FILENAME, SAMPLE_RATE, data)
playsound(WAV_FILENAME)

# plot written wav
length = data.shape[0] / SAMPLE_RATE
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data)
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()


#  read wav
WAV_FILENAME = 'wavs/my808kit/snare2.wav'
SAMPLE_RATE, data = wavfile.read(WAV_FILENAME)
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / SAMPLE_RATE
print(f"length = {length}s")

# write read wav
write(WAV_FILENAME+'test.wav', SAMPLE_RATE, data)

#  plot read wav
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

#  plot a sine with matplotlib and numpy

x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()
