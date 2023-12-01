"""vjpy video class."""

import os
from collections import defaultdict
from moviepy.editor import (
    VideoFileClip,
    concatenate_videoclips,
    clips_array,
    vfx
    )
from vjpy import VideoDrumkit, VideoDrum


class VideoDevice:
    """vjpy video class."""

    def __init__(self, vj):
        self.note_value = vj.note_value
        self.vdk = self.load_vdk()

    def load_vdk(self):
        """Load video drum kit."""
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
        return vdk

    def get_subclip(self, videoclip, start=0, duration=None):
        """Get a subclip from a video object."""
        if duration is None:
            duration = self.note_value
        return videoclip.subclip(start, start + duration)

    def steps_to_pattern(self, steps):
        """Collect unique MIDI notes."""
        notes_set = set()
        for s, notes in steps.items():
            for note in notes['notes']:
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
        k : ['_', '_', '_', '_', '_', '_', ...] # kick
        s : ['_', '_', '_', '_', '_', '_', ...] # snare
        '''

        # replace positions with corresponding drum hits
        for n, s in enumerate(steps.items()):
            notes = s[1]
            for note in notes:
                if note != 81:
                    pattern[note][n] = "x"

        '''
        k : ['x', '_', '_', '_', 'x', '_', ...] # kick
        s : ['_', '_', 'x', '_', '_', '_', ...] # snare
        '''
        return pattern

    def make_vid(self, steps):
        """Make video."""
        bankname = 'drums_03'
        beatname = 15
        soundbank_dir_path = os.path.join("soundbanks", bankname)
        soundbank_path = os.path.join("soundbanks", bankname, f"{bankname}.mp4")
        beat_path = os.path.join(soundbank_dir_path, "beats", f"{beatname}")
        video_array_path = os.path.join(beat_path, f"{beatname}_array.mp4")
        videoclip = VideoFileClip(soundbank_path)
        duration = list(steps.keys())[1]-list(steps.keys())[0]

        def render_drum_patterns(pattern):
            """Render a video representing one drum pattern."""
            key_clips = defaultdict(list)

            for key, key_pattern in pattern.items():
                for hit in key_pattern:
                    if hit == "x":
                        key_clip = self.get_subclip(
                            videoclip, start=self.vdk.drums[key].start, duration=duration
                            )
                    else:
                        key_clip = self.get_subclip(
                            videoclip, start=self.vdk.drums[81].start, duration=duration
                            )
                    key_clips[key].append(key_clip)

            for key in key_clips:
                concat_clip = concatenate_videoclips(key_clips[key]*1)
                concat_clip_path = os.path.join(
                    soundbank_dir_path, 'beats', f'{beatname}', f'{key}.mp4'
                    )
                concat_clip.write_videofile(concat_clip_path)

        def render_video_array(pattern):
            """Composite a vertical video array from concatenated drum pattern subclips."""
            pattern_keys = list(pattern.keys())
            clips = []
            for n, patt in enumerate(pattern_keys):
                if n % 2 == 1:
                    clip = VideoFileClip(os.path.join(
                        beat_path, f"{pattern_keys[n]}.mp4")
                        ).fx(vfx.mirror_x)
                else:
                    clip = VideoFileClip(os.path.join(beat_path, f"{pattern_keys[n]}.mp4"))
                clips.append(clip)
            clips_array([[clip] for clip in clips]).resize(width=960).write_videofile(
                video_array_path
                )

        pattern = self.steps_to_pattern(steps)
        render_drum_patterns(pattern)
        render_video_array(pattern)
