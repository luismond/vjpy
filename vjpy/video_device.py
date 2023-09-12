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

    def __init__(self, bpm, soundbank_name, resolution, note_values, note_duration):
        self.soundbanks_path = "soundbanks"
        self.bpm = bpm,
        self.soundbank_dir_path = os.path.join("soundbanks", soundbank_name)
        self.soundbank_video_path = os.path.join(self.soundbank_dir_path,
                                                 f'{soundbank_name}.mp4')
        self.resolution = resolution
        self.note_values = note_values
        self.note_duration = note_duration
        

    @property
    def videoclip(self):
        """Make a video object."""
        return VideoFileClip(self.soundbank_video_path)

    def get_subclip(self, start=0):
        """Get a subclip from a video object."""
        res = self.resolution
        note_value = self.note_values[res].relative_value / self.note_duration
        return self.videoclip.subclip(start, start + note_value)

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

    def concat_drum_subpatterns(self, patterns, drums, beat_n):
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
                    
        print(key_clips)
        for key in key_clips:
            final_clip = self.concatenate_subclips(key_clips[key]*4)
            final_clip_path = os.path.join(
                self.soundbank_dir_path, 'beats', f'{beat_n}', f'{key}.mp4'
                )
            self.write_concatenated_subclips(final_clip, final_clip_path)

    def composite_vertical_videobeat(self, beat_n):
        """Mix 4 video patterns in a vertical array."""
        beat_path = os.path.join(self.soundbank_dir_path, 'beats', f'{beat_n}')
        clip1 = VideoFileClip(os.path.join(beat_path, 'k.mp4')).fx(vfx.mirror_x)
        #clip1 = clip1
        clip2 = VideoFileClip(os.path.join(beat_path, 'h.mp4'))
        clip3 = VideoFileClip(os.path.join(beat_path, 's.mp4')).fx(vfx.mirror_x)
        #clip3 = clip3.fx(vfx.mirror_x)
        clip4 = VideoFileClip(os.path.join(beat_path, 'r.mp4'))
        video = clips_array([[clip1],
                             [clip2],
                             [clip3],
                             [clip4]])
        video.resize(width=960).write_videofile(
            os.path.join(beat_path, f"{beat_n}_composited.mp4"))

    #  todo: implement compositing
