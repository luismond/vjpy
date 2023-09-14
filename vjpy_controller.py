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
wav_concat = wd.concatenate_wavs(wav_paths, "concat_wavs.wav", play=True)
# %%   Mix wavs
wav_mixed = wd.mix_wavs(wav_paths, "mixed_wavs.wav", play=True)
# %%  Render wav pattern
steps = wd.wav_patterns_to_steps(patterns)
patt_concat = wd.render_wav_steps(steps, "rendered_wav_pattern.wav", play=True)
# %% Parse a MIDI file, render a target wav and play it
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
midi_steps = md.parse_midi_file(filename)
midi_patt_wav = wd.render_midi_steps(midi_steps, "rendered_midi_pattern.wav", play=True)


# %% Make a video object
videoclip = vd.make_videoclip()
# %% Make a video subclip
subclip = vd.get_subclip(videoclip, start=03.710) # ride
# %% Define a video drum kit
vdk = Drumkit(
    name="videokit",
    drums={
        "k": Drum(name="kick", note=36, short_hand="k",
                  clip=vd.get_subclip(videoclip, start=24.950)),
        "h": Drum(name="hat", note=42, short_hand="h",
                  clip=vd.get_subclip(videoclip, start=21.290)),
        "s": Drum(name="snare", note=38, short_hand="s",
                  clip=vd.get_subclip(videoclip, start=27.513)),
        "_": Drum(name="silence", note=41, short_hand="_",
                  clip=vd.get_subclip(videoclip, start=06.005))
        })
# %% Concatenate drum subclips acordding to patterns
vd.concat_drum_subpatterns(patterns, vdk, loops_n=2)
# %% Composite a polyphonic, vertical video array from the concatenated drum subclips
vd.composite_vertical_videobeat(patterns)
# %% Read a MIDI file, render a target video
filename = os.path.join(md.midi_data_dir, "drum_beat.mid")
midi_steps = md.parse_midi_file(filename)
patterns = vd.midi_steps_to_pattern(midi_steps, vdk)
vd.concat_drum_subpatterns(patterns, vdk, loops_n=8)
vd.composite_vertical_videobeat(patterns)
