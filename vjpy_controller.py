"""vjpy controller."""
import os
from vjpy import VjPyDevice, MidiDevice, WavDevice, VideoDevice
from vjpy import patterns, patterns_01

vj = VjPyDevice()
md = MidiDevice(vj)
wv = WavDevice(vj)


# %% Play MIDI note
md.play_note(note=44, velocity=120, duration=0)
# %% Play MIDI patterns
md.play_patterns(patterns)
# %% Generate pattern
rp = md.generate_random_pattern(patt_len=8)
md.play_pattern(rp)
# %% Play MIDI file
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
md.play_midi_file(filename)


# %% Play wav

drumkit = "myfunkkit"
wav_shs = ["c", "h", "k"] # clap, hihat, kick
wav_list = [os.path.join(wv.drumkit_dir,
                          f"{vj.drumkit_sh_names[wn]}.wav") for wn in wav_shs]
wav_path = os.path.join(wv.drumkit_dir, f"{vj.drumkit_sh_names['c']}.wav") 
wv.play_wav(wav_path)

#  Concatenate wavs
wav_concat = wv.concatenate_wavs(wav_list)
concat_wav_path = os.path.join(wv.wav_dir, "examples", "concat_wavs.wav")
wv.write_wav(concat_wav_path, wav_concat)
wv.play_wav(concat_wav_path)

#   Mix wavs
wav_mixed = wv.mix_wavs(wav_list)
mixed_wav_path = os.path.join(wv.wav_dir, "examples", "mixed_wavs.wav")
wv.write_wav(mixed_wav_path, wav_mixed)
wv.play_wav(mixed_wav_path)

#  Render wav pattern
steps = wv.wav_patterns_to_steps(patterns)
patt_concat = wv.concat_wav_steps(steps)
concat_wav_path = os.path.join(wv.wav_dir, "examples", "rendered_pattern.wav")
wv.write_wav(concat_wav_path, patt_concat)
wv.play_wav(concat_wav_path)

# Parse MIDI file and play wavs
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
midi_note_steps = md.parse_midi_file(filename)
wv.play_midi_steps(midi_note_steps)

# Parse MIDI file and render pattern
midi_patt_concat = wv.render_midi_note_steps(midi_note_steps)
concat_wav_path = os.path.join(wv.wav_dir, "examples", "rendered_midi_pattern.wav")
wv.write_wav(concat_wav_path, midi_patt_concat)
wv.play_wav(concat_wav_path)

# %% Video device
vd = VideoDevice(vj, soundbank_name="drums_03")
# Get subclips corresponding to a drumkit hit.
drum_subclips = {
    "r": vd.get_subclip(start=03.710), # ride
    "x": vd.get_subclip(start=07.137), # china
    "c": vd.get_subclip(start=09.770), # crash
    "h": vd.get_subclip(start=21.290), # hat
    "o": vd.get_subclip(start=23.113), # hat open
    "k": vd.get_subclip(start=24.950), # kick
    "s": vd.get_subclip(start=27.513), # snare1
    "z": vd.get_subclip(start=29.512), # snare2
    "t": vd.get_subclip(start=31.505), # tom1a
    "v": vd.get_subclip(start=34.248), # tom1b
    "w": vd.get_subclip(start=37.160), # tom2a
    "u": vd.get_subclip(start=39.010), # tom2b
    "_": vd.get_subclip(start=06.005)  # silence
}
beat_n = '14'
vd.concat_drum_subpatterns(patterns_01, drum_subclips, beat_n)
vd.composite_vertical_videobeat(beat_n)
