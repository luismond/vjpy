# vjpy
Python module to sequence music videos

## Concept

Use MIDI, audio and video python modules to create audiovisual beats. 

## Inspiration

Hexstatic, Coldcut music videos from the early 2000's, created with VJPro. 

## Motivation

I am not inclined to use point-and-click GUI software. I wish to compose music videos programatically.

## Log

26-jul-23:
	Managed to setup audio/midi libraries in ubuntu. 
	Wrote drum pattern logic.
	Achieved sending messages from python to Hydrogen.


## To-do

### MIDI
- Midi sequencing logic		 				[midi-sequencer.py]
- Midi reading logic						[midi-reader.py]

### AUDIO
- Generate sound without Hydrogen			[sound-midi-player.py]

### VIDEO
- Associate sound+midi with video chunks	[video-associator.py]
- Sequence video chunks with midi 			[video-midi-player.py]
- Automate video chunking 					[video-chunker.py]

