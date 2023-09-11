# vjpy
Python module to create MIDI, audio and visual rhythms.

![logo by dall-e mini](https://i.imgur.com/HmeYbDU.jpg)

## Concept
A text-based approach to rhythm sequencing, with a focus on visual rhythmic sequences.

## Basic usage

```python
>>> from vjpy import VjPyDevice
>>> vjpd = VjPyDevice()
>>> md = vjpd.midi_device
>>> md.play_patterns(patterns)
```

### Pattern example
```python
patterns = {
    "01":
        {
            #      1    2    3    4    5    6    7    8
            "h": ["x", "x", "x", "x", "x", "_", "x", "_"], # hi-hat
            "k": ["x", "_", "_", "_", "_", "_", "_", "_"], # kick
            "c": ["_", "_", "_", "_", "x", "_", "_", "_"]  # clap
        }
```

### Drumkit example 

A drumkit features drums. Each Drum is accesible by name, MIDI note, a shorthand and an emoji.

```python

"myfunkkit": Drumkit(
    name="myfunkkit",
    drums={
        "kick1": Drum(name="kick1", note=36, short_hand="k", emoji="🥾"),
        "clap1": Drum(name="clap1", note=40, short_hand="c", emoji="👏"),
        "hat1": Drum(name="hat1", note=44, short_hand="h", emoji="🔔")
        }
    )
```


## Hydrogen MIDI file (modus SMF0)

```python
MD = VJPD.midi_device                               # device
MID_NAME = "drum_beat.mid")                         # file
mid = mido.MidiFile(MID_NAME, clip=True)            # object
track = mid.tracks[0]                               # track

meta_messages = [msg for msg in track[:4]]          # meta messages
copyright_ = meta_messages[0]                           # copyright
track_name = meta_messages[1]                           # name
tempo = meta_messages[2]                                # tempo
time_signature = meta_messages[3]                       # signature

messages = [msg for msg in track[4:-1]]             # messages
msg = messages[0]
m_type = msg.type                                       # type ('note on', 'note off')
m_note = msg.note                                       # note (int)
m_time = msg.time                                       # time (int)
m_velo = msg.velocity                                   # velocity (int)
```


## Video sounbank structure
```
soundbank name: "drums_01"

|soundbanks             # soundbanks directory
|_ drums_01             # soundbank directory
  |_ drums_01.mp4       # source video file
  |_ drums_01.mp3       # audio-only .mp3 file
  |_ drums_01.wav       # audio-only .wav file
  |_ drums_01.aup3      # audacity project file
  |_ drums_01.osp       # openshot project file
    |_ drums_01_assets  # openshot project assets
  |_ beats              # videobeats directory
    |_ beat_01.mp4      # videobeat file
```
 
## Roadmap

Define the following devices:

### MIDI
- MIDI device ✓

### AUDIO
- Audio device ✓

### VIDEO
- Video device ✓

### Other TODOs:
- Test suite

## Log

26-jul-23:
- Setup audio and midi libraries in ubuntu.
- Wrote drum pattern logic.
- Defined communication from Python to Hydrogen.

27-jul-23:
- Defined a midi drum sequencer.

28-jul-23:
- Bootstrap a wav writer, video writer.

29-jul-23:
- Add looping logic
- Add MIDI sending & receiving logic.

04-ago-23:
- Add wav concatenation logic.

06-ago-23:
- Implement receiving of MIDI messages in the wav player.

30-ago-23:
- Implemented video sequencing logic.

10-sep-23:
- Implemented polyphonic MIDI and WAV patterns

## Related work

Hexstatic, Coldcut music videos from the early 2000's, created with VJPro. 

Example: https://www.youtube.com/watch?v=f1SLN3LpDiA

## Glossary

### sample rate
The sampling frequency or sampling rate, fs, is the number of samples divided by the interval length over in which occur, thus fs = 1/T, with the unit sample per second, sometimes referred to as hertz, for example e.g. 48 kHz is 48,000 samples per second.

### Hz
The hertz (symbol: Hz) is the unit of frequency in the International System of Units, equivalent to one cycle per second

### amplitude
In a standing wave, the amplitude of vibration has nulls at some positions where the wave amplitude appears smaller or even zero.


## How to create a new video sound bank

- Record video clips hitting drums.
- Slice the video clips in a video editing software (one video per sound)
-- If the sound bank has several clips, load them all into the time line
-- Merge, edit, condense and separate the audio
-- Clean the audio in an audio software
--- Volume, normalization, high-pass, low-pass effects on drum
-- Re-import video+audio for further processing

- Try to set the starting frame to a point where the sound is at its peak
- Name the subvideo clips with the name of the corresponding sound
- Load the video files into video objects and use them to compose video beats


