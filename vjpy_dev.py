"""vjpy examples script."""

from vjpy import MidiSequencer
from vjpy import TR808EmulationKit
from vjpy.patterns import *
from playsound import playsound
import scipy
from scipy.io import wavfile
from scipy.io.wavfile import write


# %% Instantiate a sequencer
seq = MidiSequencer(drumkit=TR808EmulationKit, bpm=90)

# Play a pattern
#patt = pattern_examples[1].pattern
for _ in range(8):
    patt = "khckhkchkhckhckchkchkkchkhckkccc"
    print(f"Playing a pattern:\n{patt}")
    seq.play_pattern(patt)


# %% Play a bar of patterns
print(f"Playing a bar:\n{bar_example.patterns}")
seq.play_bar(bar_example)


# %% Loop a bar
NUM_LOOPS = 8
print(f"Looping a bar {NUM_LOOPS} times:")
seq.loop_bar(bars_example[0], NUM_LOOPS)


# %% Loop a sequence of bars
NUM_LOOPS = 2
print(f"Looping a sequence of bars {NUM_LOOPS} times:")
seq.loop_bars(bars_example, NUM_LOOPS)



# %% Test pattern generator
from vjpy import PatternGenerator
from vjpy.midi_sequencer import MidiSequencer
from vjpy.drumkits import TR808EmulationKit

seq = MidiSequencer(drumkit=TR808EmulationKit, bpm=100)
pg = PatternGenerator()

for _ in range(8):
    rp = pg.generate_random_pattern()
    print(f"\n\n♪♪ Playing random pattern:\n{rp}")
    seq.play_pattern(rp)
    print(f"\n\n♪♪ Playing random pattern:\n{rp}")
    seq.play_pattern(rp)



# %% Test wav player
kit_path = "wavs/myfunkkit"
# read a wav and store it in a list n times
SAMPLE_RATE = 44100

datas = []
for _ in range(4):
    _, data = wavfile.read(f"{kit_path}/kick.wav")
    datas.append(data)
    _, data = wavfile.read(f"{kit_path}/hat.wav")
    datas.append(data)
    _, data = wavfile.read(f"{kit_path}/clap.wav")
    datas.append(data)
    _, data = wavfile.read(f"{kit_path}/hat.wav")
    datas.append(data)

# concatenate wavs
wav_c_name = "wavs/concat.wav"
data_c = scipy.concatenate(datas)

# write concatenated wav
write(wav_c_name, SAMPLE_RATE, data_c)

# play concatenated wav
playsound(wav_c_name)


# %% Test midi receiver and wav player

midi_receiver = MidiReceiver()
wav_player = WavPlayer()

# Play each midi message received.
for m in midi_receiver.yield_midi_msg():
    wav_player.play_wav_from_midi_msg(m)
    
# %% Test midi sender

sender = MidiSender()
for _ in range(4):
    for note in [43, 38, 43, 45]:
        sender.send_note(note)
        sleep(.5)






