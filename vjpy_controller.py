"""vjpy controller."""
import os
from vjpy import VjPyDevice, patterns, patterns_01

soundbank_name = 'drums_03'
vjpd = VjPyDevice(soundbank_name=soundbank_name)
md = vjpd.midi_device
wv = vjpd.wav_device
vd = vjpd.video_device
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
wav_names = ["kick.wav", "hat.wav", "clap.wav"]
wav_list = [os.path.join(wv.wav_dir, "drumkits", drumkit, wn) for wn in wav_names]
wv.play_wav(wav_list[0])

# %% Concatenate wavs
wav_concat = wv.concatenate_wavs(wav_list)
concat_wav_path = os.path.join(wv.wav_dir, "examples", "concat_wav.wav")
wv.write_wav(concat_wav_path, wav_concat)
wv.play_wav(concat_wav_path)

# %%  Mix wavs
wav_mixed = wv.mix_wavs(wav_list)
mixed_wav_path = os.path.join(wv.wav_dir, "examples", "mixed_wav.wav")
wv.write_wav(mixed_wav_path, wav_mixed)
wv.play_wav(mixed_wav_path)

# %% Render wav pattern
patterns = {
    "01":
        {
            #      1    2    3    4    5    6    7    8
            "k": ["x", "_", "_", "_", "x", "x", "x", "_"],
            "h": ["_", "x", "x", "x", "x", "x", "_", "x"],
            "c": ["_", "_", "x", "_", "_", "_", "_", "x"]
            }
        }

patt_concat = wv.render_wav_patterns(patterns)
concat_wav_path = os.path.join(wv.wav_dir, "examples", "pattern.wav")
wv.write_wav(concat_wav_path, patt_concat)
wv.play_wav(concat_wav_path)

# %% Video device

# Get subclips corresponding to a drum or cymbal hit."""
# todo: adapt the Drumkit data class for this use case

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
    "_": vd.get_subclip(start=01.500)  # silence
}


#%%
beat_n = '14'
vd.concat_drum_subpatterns(patterns_01, drum_subclips, beat_n)
vd.composite_vertical_videobeat(beat_n)
