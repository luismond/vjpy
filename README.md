# vjpy
Python module to create audiovisual sequences

![logo by dall-e mini](https://i.imgur.com/HmeYbDU.jpg)

## Concept

Use midi, audio and video python modules to create audiovisual sequences. 


## Basic usage

```python
>>> from vjpy import MidiSequencer, TR808EmulationKit
>>> from vjpy.patterns import bar_, bars, pattern
>>> from time import sleep
```

### Pattern example
```python
>>> pattern = Pattern(pattern='k.h.')
```

### Bar example
```python
>>> bar_ = Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh'])
```

### Bars example
```python
>>> bars = [
    Bar(bar_num=1, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=2, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
    Bar(bar_num=3, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=4, patterns=['k.h.', 'chhh', 'kkvv', 'cccc']),
    Bar(bar_num=5, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=6, patterns=['k.h.', 'chhh', 'khhh', 'cchh']),
    Bar(bar_num=7, patterns=['k.h.', 'chhh', 'khhh', 'chhh']),
    Bar(bar_num=8, patterns=['k.h.', 'chhh', 'kkkk', 'cccc'])
]
```


### Instantiate a sequencer device and set the bpm to 120

```python
>>> bpm = 120
>>> seq = MidiSequencer(bpm=bpm)
```


### Print drumkit info
```python
>>> print("Drumkit info:\n")
>>> pp(TR808EmulationKit.drums)
```

```python
Drumkit info:

{'clap': Drum(name='clap', note=40, short_hand='c'),
 'clave': Drum(name='clave', note=50, short_hand='v'),
 'conga': Drum(name='conga', note=49, short_hand='g'),
 'cowbell': Drum(name='cowbell', note=51, short_hand='w'),
 'hat': Drum(name='hat', note=45, short_hand='h'),
 'kick': Drum(name='kick', note=36, short_hand='k'),
 'snare': Drum(name='snare', note=38, short_hand='s'),
 'tom': Drum(name='tom', note=43, short_hand='t')}
```


### Play a pattern

```python
>>> patt = pattern.pattern
>>> seq.play_pattern(pattern.pattern)
```

```python
♪♪ Playing a pattern (a dot represents silence)
k.h.:
```

### Play a bar of patterns

```python
>>> seq.play_bar(bar_)
```

```python
♪♪ Playing a bar:
['k.h.', 'chhh', 'khhh', 'chhh']
```

### Loop a bar
```python
>>> num_loops = 4
>>> seq.loop_bar(bars[0], num_loops)
```

```python
♪♪ Looping a bar 4 times:
bar_num=1 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=1 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=1 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=1 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
```

### Loop a sequence of bars

```python
>>> num_loops = 2
>>> seq.loop_bars(bars, num_loops)
```

```python
bar_num=1 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=2 patterns=['k.h.', 'chhh', 'khhh', 'cchh']
bar_num=3 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=4 patterns=['k.h.', 'chhh', 'kkvv', 'cccc']
bar_num=5 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=6 patterns=['k.h.', 'chhh', 'khhh', 'cchh']
bar_num=7 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=8 patterns=['k.h.', 'chhh', 'kkkk', 'cccc']
bar_num=1 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=2 patterns=['k.h.', 'chhh', 'khhh', 'cchh']
bar_num=3 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=4 patterns=['k.h.', 'chhh', 'kkvv', 'cccc']
bar_num=5 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=6 patterns=['k.h.', 'chhh', 'khhh', 'cchh']
bar_num=7 patterns=['k.h.', 'chhh', 'khhh', 'chhh']
bar_num=8 patterns=['k.h.', 'chhh', 'kkkk', 'cccc']
```

## Roadmap

Define the following devices:

### MIDI
- Midi sequencer ✓
- Midi player ✓
- Midi receiver ✓

### AUDIO
- Audio player

### VIDEO
- Video player
- Video processor

### Other TODOs:
- Merge MIDI modules into a MIDI device
- Test suite

## Log

26-jul-23:
- Setup audio and midi libraries in ubuntu. 
- Wrote drum pattern logic.
- Defined communication from Python to Hydrogen.

27-jul-23:
- Defined a midi drum sequencer.

28-jul-23:
- Bootstrap a wav writer, video writer

29-jul-23:
- Add looping logic
- Add MIDI sending & receiving logic

04-ago-23:
- Add wav concatenation logic

## Related work

Hexstatic, Coldcut music videos from the early 2000's, created with VJPro. 

Example: https://www.youtube.com/watch?v=f1SLN3LpDiA

# Glossary

### sample rate
The sampling frequency or sampling rate, fs, is the number of samples divided by the interval length over in which occur, thus fs = 1/T, with the unit sample per second, sometimes referred to as hertz, for example e.g. 48 kHz is 48,000 samples per second.

### Hz
The hertz (symbol: Hz) is the unit of frequency in the International System of Units, equivalent to one cycle per second

### amplitude
In a standing wave, the amplitude of vibration has nulls at some positions where the wave amplitude appears smaller or even zero.



