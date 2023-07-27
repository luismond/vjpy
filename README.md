# vjpy
Python module to sequence music videos

![logo by dall-e mini](https://i.imgur.com/HmeYbDU.jpg)

## Concept

Use MIDI, audio and video python modules to create audiovisual beats. 

## Inspiration

Hexstatic, Coldcut music videos from the early 2000's, created with VJPro. 

Example: https://www.youtube.com/watch?v=f1SLN3LpDiA

## Motivation

Create audiovisual sequences programatically.

## To-do

### MIDI
- Midi sequencing logic		 				[midi-sequencer.py]
    - Define basic objects and actions (notes, tempo, play, etc.)
    
- Midi reading logic						[midi-reader.py]

### AUDIO
- Generate sound without Hydrogen			[sound-midi-player.py]

### VIDEO
- Associate sound+midi with video chunks	[video-associator.py]
- Sequence video chunks with midi 			[video-midi-player.py]
- Automate video chunking 					[video-chunker.py]

## Log

26-jul-23:
- Managed to setup audio/midi libraries in ubuntu. 
- Wrote drum pattern logic.
- Achieved sending messages from python to Hydrogen. Video: https://youtu.be/PWLScepLk58

27-jul-23:
- Began defining a linear drum sequencer. 