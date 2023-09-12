"""vjpy video class."""

import os
from collections import defaultdict
from moviepy.editor import (
    VideoFileClip,
    # CompositeVideoClip,
    concatenate_videoclips,
    clips_array,
    vfx
    )
# from moviepy.audio.fx.all import volumex



class VideoDevice:
    """vjpy video class."""

    def __init__(self, bpm):
        self.soundbanks_path = 'soundbanks'
        self.bpm = bpm

    def get_videoclip(self, video_filename):
        """Make a video object."""
        return VideoFileClip(video_filename)

    def get_videosubclip(self, video_clip, start=0, duration=.075):
        """Get a subclip from a video object."""
        return video_clip.subclip(start, start + duration)

    def concatenate_subclips(self, subclips):
        """Concatenate an array of subclips."""
        return concatenate_videoclips(subclips)

    def get_bars_subclips(self, bars):
        """Get all the subclips from a pattern."""
        subclips = []
        for bar_ in bars:
            for patt in bar_:
                for subclip in patt:
                    subclips.append(subclip)
        return subclips

    def write_concatenated_subclips(self, concatenated_subclips, subclip_name):
        """Write concatenated subclips."""
        concatenated_subclips.write_videofile(subclip_name)

    def concat_drum_subpatterns(self, patterns, drums, soundbank_dir_path, beat_n):
        """Concatenate and write each drum sub-pattern separately."""
        key_clips = defaultdict(list)
        for pattern in patterns.values():
            for key, key_pattern in pattern.items():
                for hit in key_pattern:
                    if hit == "x":
                        key_clip = drums[key]
                    else:
                        key_clip = drums["_"]
                    key_clips[key].append(key_clip)
                final_clip = self.concatenate_subclips(key_clips[key]*2)
                final_clip_path = os.path.join(
                    soundbank_dir_path,
                    'beats', f'{beat_n}', f'{key}.mp4'
                    )
                self.write_concatenated_subclips(final_clip, final_clip_path)

    def composite_vertical_videobeat(self, soundbank_dir_path, beat_n):
        """Mix 4 video patterns in a vertical array."""
        beat_path = os.path.join(soundbank_dir_path, 'beats', f'{beat_n}')
        clip1 = VideoFileClip(os.path.join(beat_path, 'k.mp4'))
        clip1 = clip1.fx(vfx.mirror_x)
        clip2 = VideoFileClip(os.path.join(beat_path, 'h.mp4'))
        clip3 = VideoFileClip(os.path.join(beat_path, 's.mp4'))
        clip3 = clip3.fx(vfx.mirror_x)
        clip4 = VideoFileClip(os.path.join(beat_path, 'r.mp4'))
        video = clips_array([[clip1,],
                              [clip2,],
                              [clip3,],
                              [clip4,]])
        video.resize(width=960).write_videofile("my_comp.mp4")

    #  todo: implement compositing
