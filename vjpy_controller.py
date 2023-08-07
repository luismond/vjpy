"""vjpy controller."""

from vjpy_app import MidiDevice, WavDevice
from vjpy_app import TR808EmulationKit, MyFunkKit
from vjpy_app import bar_example, bars_example


def get_drum_midi_notes_to_names(drumkit):
    """Drum-midi-notes <-> Drum-wav-names map."""
    drum_names = {}
    for drum in drumkit.drums.values():
        drum_names[drum.note] = drum.name
    return drum_names


# %% Test wav device
dmnn = get_drum_midi_notes_to_names(drumkit=MyFunkKit)
wd = WavDevice(drumkit=MyFunkKit)
notes = [43, 38, 43, 40]
wd.write_concatenated_wavs(dmnn, notes)

# %% Test MIDI device
md = MidiDevice(drumkit=TR808EmulationKit)
# Pattern
print("Playing a pattern.")
md.play_pattern("k.h.c.h.")
# Bar
print(f"Playing a bar:\n{bar_example.patterns}")
md.play_bar(bar_example)
# Loop a bar
print("Looping a bar")
md.loop_bar(bars_example[0], num_loops=2)
# Loop a sequence of bars
print("Looping a sequence of bars")
md.loop_bars(bars_example, num_loops=1)

# %% Generate random patterns
md = MidiDevice(drumkit=TR808EmulationKit)
rp = md.generate_random_pattern(patt_len=8)
print(f"Playing random pattern:{rp}")
md.play_pattern(rp)

# %% Test midi receiving
md = MidiDevice(drumkit=TR808EmulationKit)
midi_in = md.open_midi_in()
wd = WavDevice(drumkit=MyFunkKit)
dmnn = get_drum_midi_notes_to_names(drumkit=MyFunkKit)

for msg in md.yield_midi_msg(midi_in):
    wd.play_drum_wav_from_midi_msg(dmnn, msg)

# %% Test midi sending
md = MidiDevice(drumkit=TR808EmulationKit)
md.send_note(40)
