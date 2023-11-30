"""vjpy video dev."""
import os
from vjpy import VjPyDevice, MidiDevice, VideoDevice
from collections import defaultdict
from moviepy.editor import (
    VideoFileClip,
    concatenate_videoclips,
    clips_array,
    vfx
    )
from vjpy import VideoDrumkit, VideoDrum


vj = VjPyDevice()
md = MidiDevice(vj)
vd = VideoDevice(vj)

fn = "jazz.mid"
filename = os.path.join(md.midi_data_dir, fn)
msgs = md.get_sorted_midi_messages(filename)
steps = md.get_midi_steps(msgs)

BANKNAME = 'drums_03'
BEATNAME = 15


# def make vid(BANKNAME, BEATNAME)

SOUNDBANK_DIR_PATH = os.path.join("soundbanks", BANKNAME)
SOUNDBANK_PATH = os.path.join("soundbanks", BANKNAME, f"{BANKNAME}.mp4")
BEAT_PATH = os.path.join(SOUNDBANK_DIR_PATH, "beats", f"{BEATNAME}")
VIDEO_ARRAY_PATH = os.path.join(BEAT_PATH, f"{BEATNAME}_array.mp4")
videoclip = VideoFileClip(SOUNDBANK_PATH)


duration = list(steps.keys())[1]-list(steps.keys())[0]


def get_subclip(videoclip, start=0, duration=None):
    """Get a subclip from a video object."""
    if duration is None:
        duration = vd.note_value
    return videoclip.subclip(start, start + duration)  # + step duration


# Define a video drum kit
vdk = VideoDrumkit(
    name="videokit",
    drums={
        36: VideoDrum(name="kick", note=36, short_hand="k", start=24.950),
        38: VideoDrum(name="snare", note=38, short_hand="s", start=27.5128),
        37: VideoDrum(name="snare2", note=37, short_hand="z", start=29.5085),
        45: VideoDrum(name="tom1", note=45, short_hand="t", start=31.4610),
        41: VideoDrum(name="tom2", note=41, short_hand="w", start=38.9788),
        43: VideoDrum(name="tom3", note=43, short_hand="p", start=38.9788),
        51: VideoDrum(name='ride', note=51, short_hand="r", start=03.7158),
        49: VideoDrum(name="china", note=49, short_hand="x", start=07.1222),
        57: VideoDrum(name="crash", note=57, short_hand="c", start=09.7210),
        42: VideoDrum(name="hat", note=42, short_hand="h", start=21.2910),
        44: VideoDrum(name="hat", note=44, short_hand="f", start=21.2910),
        46: VideoDrum(name="hat_open", note=46, short_hand="o", start=23.0869),
        81: VideoDrum(name="silence", note=81, short_hand="_", start=06.005),
        }
    )

# drumkit_note_shs = {}
# for drum in vdk.drums.values():
#     drumkit_note_shs[drum.note] = drum#.short_hand

# # # collect unique notes
notes_set = set()
for s, notes in steps.items():
    for note in notes:
        if note != 81:
            notes_set.add(note)
'''
{42, 51, 36, 38}
'''

# create empty pattern dictionary with the necessary drum keys
pattern = defaultdict(list)
for note in notes_set:
    for n in range(len(steps.items())):
        pattern[note].append("_")

'''
k : ['_', '_', '_', '_', '_', '_', ...]
s : ['_', '_', '_', '_', '_', '_', ...]
'''

# replace empty slots with corresponding drum hits
for n, s in enumerate(steps.items()):
    notes = s[1]
    for note in notes:
        if note != 81:
            pattern[note][n] = "x"

'''
k : ['x', '_', '_', '_', 'x', '_', ...]
s : ['_', '_', 'x', '_', '_', '_', ...]
'''


def render_drum_patterns(pattern):
    """Render a video representing one drum pattern."""
    key_clips = defaultdict(list)

    for key, key_pattern in pattern.items():
        for hit in key_pattern:
            if hit == "x":
                key_clip = get_subclip(videoclip, start=vdk.drums[key].start, duration=duration)
            else:
                key_clip = get_subclip(videoclip, start=vdk.drums[81].start, duration=duration)
            key_clips[key].append(key_clip)

    for key in key_clips:
        concat_clip = concatenate_videoclips(key_clips[key]*1)
        concat_clip_path = os.path.join(SOUNDBANK_DIR_PATH, 'beats', f'{BEATNAME}', f'{key}.mp4')
        concat_clip.write_videofile(concat_clip_path)


def render_video_array(pattern):
    """Composite a polyphonic vertical video array from concatenated drum pattern subclips."""
    pattern_keys = list(pattern.keys())
    clips = []
    for n, patt in enumerate(pattern_keys):
        if n % 2 == 1:
            clip = VideoFileClip(os.path.join(BEAT_PATH, f"{pattern_keys[n]}.mp4")).fx(vfx.mirror_x)
        else:
            clip = VideoFileClip(os.path.join(BEAT_PATH, f"{pattern_keys[n]}.mp4"))
        clips.append(clip)
    clips_array([[clip] for clip in clips]).resize(width=960).write_videofile(VIDEO_ARRAY_PATH)


render_drum_patterns(pattern)
render_video_array(pattern)

# Read a monophonic MIDI file, render a 1-array video
# vd.render_monophonic_video(vdk, videoclip, midi_steps)
