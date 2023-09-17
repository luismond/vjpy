"""vjpy controller."""
import os
from vjpy import VjPyDevice, MidiDevice, WavDevice, VideoDevice, patterns
from vjpy import Drumkit, Drum

vj = VjPyDevice()

md = MidiDevice(vj)
wd = WavDevice(vj)
vd = VideoDevice(vj, bankname="drums_03", beatname="14")

# %% Play MIDI note
md.play_note(note=44, velocity=120, duration=0)
# %% Play MIDI patterns
md.play_patterns(patterns)
# %% Play MIDI file
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
md.play_midi_file(filename)

# %% Play wav
wav_names = ["snare.wav", "hat.wav", "kick.wav"]
wav_paths = [os.path.join(wd.drumkit_dir, wav_name) for wav_name in wav_names]
wd.play_wav(wav_paths[0])
# %%  Concatenate wavs
wav_concat = wd.concatenate_wavs(wav_paths)
concat_wav_path = os.path.join(wd.wav_dir, "examples", "concat_wavs.wav")
wd.write_wav(concat_wav_path, wav_concat)
wd.play_wav(concat_wav_path)

# %%   Mix wavs
wav_mixed = wd.mix_wavs(wav_paths)
mixed_wav_path = os.path.join(wd.wav_dir, "examples", "mixed_wavs.wav")
wd.write_wav(mixed_wav_path, wav_mixed)
wd.play_wav(mixed_wav_path)

# %%  Render wav pattern
steps = wd.wav_patterns_to_steps(patterns)
patt_concat = wd.render_wav_steps(steps)
mixed_wav_path = os.path.join(wd.wav_dir, "examples", "rendered_wav_pattern.wav")
wd.write_wav(mixed_wav_path, patt_concat)
wd.play_wav(mixed_wav_path)

# %% Parse a MIDI file, render a target wav and play it
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
midi_steps = md.parse_midi_file(filename)
midi_patt_wav = wd.render_midi_steps(midi_steps)

concat_wav_path = os.path.join(wd.wav_dir, "examples", "rendered_midi_pattern.wav")
wd.write_wav(concat_wav_path, midi_patt_wav)
wd.play_wav(concat_wav_path)

# %% Make a video object
videoclip = vd.make_videoclip()
# %% Make a video subclip
subclip = vd.get_subclip(videoclip, start=03.710) # ride
# %% Define a video drum kit
vdk = Drumkit(
    name="videokit",
    drums={
        "k": Drum(name="kick", note=36, short_hand="k", clip=vd.get_subclip(videoclip, start=24.950)),
        "h": Drum(name="hat", note=42, short_hand="h", clip=vd.get_subclip(videoclip, start=21.290)),
        "s": Drum(name="snare", note=38, short_hand="s", clip=vd.get_subclip(videoclip, start=27.513)),
        "z": Drum(name="snare2", note=40, short_hand="z", clip=vd.get_subclip(videoclip, start=29.512)),
        "r": Drum(name='ride', note=51, short_hand="r", clip=vd.get_subclip(videoclip, start=03.710)),
        "x": Drum(name="china", note=57, short_hand="x", clip=vd.get_subclip(videoclip, start=07.137)),
        "c": Drum(name="crash", note=49, short_hand="c", clip=vd.get_subclip(videoclip, start=09.770)),
        "o": Drum(name="hat_open", note=82, short_hand="o", clip=vd.get_subclip(videoclip, start=23.113)),
        "t": Drum(name="tom1", note=45, short_hand="t", clip=vd.get_subclip(videoclip, start=31.505)),
        "w": Drum(name="tom2", note=41, short_hand="w", clip=vd.get_subclip(videoclip, start=37.160)),
        "_": Drum(name="silence", note=0, short_hand="_", clip=vd.get_subclip(videoclip, start=06.005)),
        }
    )


# %% Concatenate drum subclips acordding to patterns
vd.concat_drum_subpatterns(patterns, vdk, loops_n=2)
# %% Composite a polyphonic, vertical video array from the concatenated drum subclips
vd.composite_vertical_videobeat(patterns)

# %% Read a MIDI file, render a target video
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
midi_steps = md.parse_midi_file(filename)
#%%
patterns = vd.midi_steps_to_pattern(midi_steps, vdk)
vd.concat_drum_subpatterns(patterns, vdk, loops_n=2)
vd.composite_vertical_videobeat(patterns)

#%% Read a MIDI file, render a three-array video
