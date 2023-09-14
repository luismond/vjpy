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
wav_names = ["clap.wav", "hat.wav", "kick.wav"]
wav_paths = [os.path.join(wv.drumkit_dir, wav_name) for wav_name in wav_names]
wv.play_wav(wav_paths[0])
# %%  Concatenate wavs
wav_concat = wv.concatenate_wavs(wav_paths, "concat_wavs.wav", play=True)
# %%   Mix wavs
wav_mixed = wv.mix_wavs(wav_paths, "mixed_wavs.wav", play=True)
# %%  Render wav pattern
steps = wv.wav_patterns_to_steps(patterns)
patt_concat = wv.render_wav_steps(steps, "rendered_wav_pattern.wav", play=True)
# %% Parse a MIDI file, render a target wav and play it
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
midi_steps = md.parse_midi_file(filename)
midi_patt_wav = wv.render_midi_steps(midi_steps, "rendered_midi_pattern.wav", play=True)

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
