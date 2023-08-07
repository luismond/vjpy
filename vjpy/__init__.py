"""vjpy initialization."""

__author__ = "Luis Mondragon (luismondragon@protonmail.com)"

from vjpy.data.midi.drumkits import TR808EmulationKit
from vjpy.data.midi.drumkits import MyFunkKit
from vjpy.data.midi.patterns import bar_example, bars_example

from vjpy.devices.midi_device import MidiDevice
from vjpy.devices.wav_device import WavDevice
