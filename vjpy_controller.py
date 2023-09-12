"""vjpy controller."""
import os
from vjpy import VjPyDevice, patterns

vjpd = VjPyDevice()
md = vjpd.midi_device
wv = vjpd.wav_device

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
vd = vjpd.video_device

# Render video pattern
soundbank_name = 'drums_03'
soundbank_dir_path = os.path.join(vd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_videoclip = vd.get_videoclip(soundbank_video_path)
value = .5
dur = (60/vd.bpm)*value

drums = {
    "b": vd.get_videosubclip(soundbank_videoclip, start=00.100, duration=dur), # bell
    "r": vd.get_videosubclip(soundbank_videoclip, start=03.710, duration=dur), # ride
    "x": vd.get_videosubclip(soundbank_videoclip, start=07.137, duration=dur), # china
    "c": vd.get_videosubclip(soundbank_videoclip, start=09.770, duration=dur), # crash1
    "d": vd.get_videosubclip(soundbank_videoclip, start=13.220, duration=dur), # crash2
    "i": vd.get_videosubclip(soundbank_videoclip, start=17.800, duration=dur), # hat1 pedal
    "j": vd.get_videosubclip(soundbank_videoclip, start=19.390, duration=dur), # hat2
    "h": vd.get_videosubclip(soundbank_videoclip, start=21.290, duration=dur), # hat3
    "y": vd.get_videosubclip(soundbank_videoclip, start=23.700, duration=dur), # hat5
    "o": vd.get_videosubclip(soundbank_videoclip, start=23.113, duration=dur), # hat4 open
    "k": vd.get_videosubclip(soundbank_videoclip, start=24.950, duration=dur), # kick1
    "l": vd.get_videosubclip(soundbank_videoclip, start=26.050, duration=dur), # kick2
    "s": vd.get_videosubclip(soundbank_videoclip, start=27.513, duration=dur), # snare1
    "z": vd.get_videosubclip(soundbank_videoclip, start=29.512, duration=dur), # snare2
    "t": vd.get_videosubclip(soundbank_videoclip, start=31.505, duration=dur), # tom1a
    "v": vd.get_videosubclip(soundbank_videoclip, start=34.248, duration=dur), # tom1b
    "w": vd.get_videosubclip(soundbank_videoclip, start=37.160, duration=dur), # tom2a
    "u": vd.get_videosubclip(soundbank_videoclip, start=39.010, duration=dur), # tom2b
    "_": vd.get_videosubclip(soundbank_videoclip, start=01.500, duration=dur)  # silence
}


patterns = {
    "01":
        {
            #      1    2    3    4    5    6    7    8
            "k": ["x", "_", "_", "_", "x", "x", "_", "_"],
            "h": ["_", "x", "x", "x", "x", "x", "x", "x"],
            "s": ["_", "_", "x", "_", "_", "_", "x", "_"],
            "r": ["x", "_", "_", "_", "_", "_", "_", "_"]
            },

    "02":
        {
            #      1    2    3    4    5    6    7    8
            "k": ["x", "_", "_", "_", "x", "x", "_", "_"],
            "h": ["_", "x", "x", "x", "x", "x", "_", "_"],
            "s": ["_", "_", "x", "_", "_", "_", "x", "x"],
            "r": ["x", "_", "_", "_", "_", "_", "_", "_"]
            },
    "03":
        {
            #      1    2    3    4    5    6    7    8
            "k": ["x", "_", "_", "_", "x", "x", "_", "_"],
            "h": ["_", "x", "x", "x", "x", "x", "_", "_"],
            "s": ["_", "_", "x", "_", "_", "_", "x", "_"],
            "r": ["x", "_", "_", "_", "_", "_", "_", "_"]
            },
    "04":
        {
            #      1    2    3    4    5    6    7    8
            "k": ["x", "_", "_", "_", "x", "_", "_", "x"],
            "h": ["_", "x", "x", "x", "x", "_", "_", "_"],
            "s": ["_", "_", "x", "_", "x", "x", "x", "_"],
            "r": ["x", "_", "_", "_", "_", "_", "_", "_"]
            },
        }

beat_n = '14'
vd.concat_drum_subpatterns(patterns, drums, soundbank_dir_path, beat_n)
vd.composite_vertical_videobeat(soundbank_dir_path, beat_n)
