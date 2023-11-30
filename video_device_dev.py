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

key_clips = defaultdict(list)

for key, key_pattern in pattern.items():
    for n, hit in enumerate(key_pattern):
        if hit == "x":
            key_clip = get_subclip(videoclip, start=vdk.drums[key].start, duration=duration)
        else:
            key_clip = get_subclip(videoclip, start=vdk.drums[81].start, duration=duration)
        key_clips[key].append(key_clip)

for key in key_clips:
    concat_clip = concatenate_videoclips(key_clips[key]*1)
    concat_clip_path = os.path.join(SOUNDBANK_DIR_PATH, 'beats', f'{BEATNAME}', f'{key}.mp4')
    concat_clip.write_videofile(concat_clip_path)


# """Composite a polyphonic vertical video array from concatenated drum subclips."""
pattern_keys = list(pattern.keys())
clip_1 = VideoFileClip(os.path.join(BEAT_PATH, f"{pattern_keys[0]}.mp4")).fx(vfx.mirror_x)
clip_2 = VideoFileClip(os.path.join(BEAT_PATH, f"{pattern_keys[1]}.mp4"))
clip_3 = VideoFileClip(os.path.join(BEAT_PATH, f"{pattern_keys[2]}.mp4")).fx(vfx.mirror_x)
clip_4 = VideoFileClip(os.path.join(BEAT_PATH, f"{pattern_keys[3]}.mp4"))
video_array = clips_array([[clip_1], [clip_2], [clip_3], [clip_4]])
video_array.resize(width=960).write_videofile(VIDEO_ARRAY_PATH)


# # Read a monophonic MIDI file, render a 1-array video
# #vd.render_monophonic_video(vdk, videoclip, midi_steps)
