"""sound player"""
import wave
import sys
import pyaudio
from time import sleep 

CHUNK = 1024

sound_dir = 'wavs/my808kit'
sound = f'{sound_dir}/hat.wav'


def play(sound):
    with wave.open(sound, 'rb') as wf:
        # Instantiate PyAudio and initialize PortAudio system resources (1)
        p = pyaudio.PyAudio()
    
        # Open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
    
        # Play samples from the wave file (3)
        while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
            stream.write(data)
    
        # Close stream (4)
        stream.close()
    
        # Release PortAudio system resources (5)
        p.terminate()
        

for n in range(8):
    play(sound)
    sleep(.125)