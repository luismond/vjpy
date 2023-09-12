"""vjpy video class."""

import os

from moviepy.editor import (
    VideoFileClip,
    # CompositeVideoClip,
    concatenate_videoclips,
    # clips_array,
    # vfx
    )
# from moviepy.audio.fx.all import volumex


class VideoDevice:
    """vjpy video class."""

    def __init__(self):
        self.soundbanks_path = os.path.join('soundbanks')

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

    #  todo: implement compositing
