"""vjpy controller."""
import os
from vjpy import VjPyDevice, MidiDevice, WavDevice, VideoDevice, patterns

vj = VjPyDevice(bpm=100)

md = MidiDevice(vj)
wd = WavDevice(vj)
vd = VideoDevice(vj, bankname="drums_03", beatname="15")

# Play MIDI note
md.play_note(note=44, velocity=120, duration=0)
# Play MIDI patterns
md.play_patterns(patterns)
# Play MIDI file
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
md.play_midi_file(filename)

# Play wav
wav_names = ["snare.wav", "hat.wav", "kick.wav"]
wav_paths = [os.path.join(wd.drumkit_dir, wav_name) for wav_name in wav_names]
wd.play_wav(wav_paths[0])
# Concatenate wavs
wav_concat = wd.concatenate_wavs(wav_paths)
concat_wav_path = os.path.join(wd.wav_dir, "examples", "concat_wavs.wav")
wd.write_wav(concat_wav_path, wav_concat)
wd.play_wav(concat_wav_path)
# Mix wavs
wav_mixed = wd.mix_wavs(wav_paths)
mixed_wav_path = os.path.join(wd.wav_dir, "examples", "mixed_wavs.wav")
wd.write_wav(mixed_wav_path, wav_mixed)
wd.play_wav(mixed_wav_path)

# Render wav pattern
steps = wd.wav_patterns_to_steps(patterns)
patt_concat = wd.render_wav_steps(steps)
mixed_wav_path = os.path.join(wd.wav_dir, "examples", "rendered_wav_pattern.wav")
wd.write_wav(mixed_wav_path, patt_concat)
wd.play_wav(mixed_wav_path)

# Parse a MIDI file, render a target wav and play it
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
midi_steps = md.parse_midi_file(filename)
midi_patt_wav = wd.render_midi_steps(midi_steps)

concat_wav_path = os.path.join(wd.wav_dir, "examples", "rendered_midi_pattern.wav")
wd.write_wav(concat_wav_path, midi_patt_wav)
wd.play_wav(concat_wav_path)

# Onset detection (poor man's Propellerheads' Recycle)
filepath = os.path.join(wd.wav_dir, "examples", "drums_03.wav")
peaks = wd.find_local_energy_peaks(filepath, 44100, prominence=3)
wd.play_peaks(filepath, 44100, peaks)

# Make a video object
videoclip = vd.make_videoclip()
# Make a video subclip
subclip = vd.get_subclip(videoclip, start=03.710) # ride

# Define a video drum kit
vdk = vd.get_vdk(videoclip)
# Concatenate drum subclips acordding to patterns
vd.concat_drum_subpatterns(patterns, vdk, loops_n=2)
#  Composite a polyphonic, vertical video array from the concatenated drum subclips
vd.composite_vertical_videobeat(patterns)

# Read a MIDI file, render a target video
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
midi_steps = md.parse_midi_file(filename)
patterns = vd.midi_steps_to_pattern(midi_steps, vdk)
vd.concat_drum_subpatterns(patterns, vdk, loops_n=1)
vd.composite_vertical_videobeat(patterns)

# Read a monophonic MIDI file, render a 1-array video
vd.render_monophonic_video(vdk, videoclip, midi_steps)