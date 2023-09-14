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

    def __init__(self, vj, bankname, beatname):
        self.bankname = bankname
        self.beatname = beatname
        self.bpm = vj.bpm
        self.note_value = vj.note_value

    def make_videoclip(self):
        """Make a video object."""
        filepath = os.path.join("soundbanks", self.bankname, f"{self.bankname}.mp4")
        return VideoFileClip(filepath)

    def get_subclip(self, videoclip, start=0):
        """Get a subclip from a video object."""
        return videoclip.subclip(start, start + self.note_value)

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

    def concat_drum_subpatterns(self, patterns, drum_subclips, loops_n=1):
        """Concatenate and write each drum sub-pattern separately."""
        soundbank_dir_path = os.path.join("soundbanks", self.bankname)
        key_clips = defaultdict(list)

        for pattern in patterns.values():
            for key, key_pattern in pattern.items():
                for hit in key_pattern:
                    if hit == "x":
                        key_clip = drum_subclips.drums[key].clip
                    else:
                        key_clip = drum_subclips.drums["_"].clip
                    key_clips[key].append(key_clip)

        for key in key_clips:
            final_clip = self.concatenate_subclips(key_clips[key]*loops_n)
            final_clip_path = os.path.join(
                soundbank_dir_path, 'beats', f'{self.beatname}', f'{key}.mp4'
                )
            self.write_concatenated_subclips(final_clip, final_clip_path)

    def composite_vertical_videobeat(self, patterns):
        """Composite a polyphonic vertical video array from concatenated drum subclips."""
        dks = list(patterns["01"].keys()) # drum keys
        soundbank_dir_path = os.path.join("soundbanks", self.bankname)
        beat_path = os.path.join(soundbank_dir_path, "beats", f"{self.beatname}")
        clip1 = VideoFileClip(os.path.join(beat_path, f"{dks[0]}.mp4")).fx(vfx.mirror_x)
        clip2 = VideoFileClip(os.path.join(beat_path, f"{dks[1]}.mp4"))
        clip3 = VideoFileClip(os.path.join(beat_path, f"{dks[2]}.mp4")).fx(vfx.mirror_x)
        video = clips_array([[clip1],
                             [clip2],
                             [clip3]])
        video.resize(width=960).write_videofile(
            os.path.join(beat_path, f"{self.beatname}_array.mp4"))


    def midi_steps_to_pattern(self, midi_steps, vdk):
        """Convert a parsed midi steps dictionary to vjpy pattern."""
        drumkit_note_shs = {}
        for drum in vdk.drums.values():
            drumkit_note_shs[drum.note] = drum.short_hand
        
        # collect unique MIDI notes as shorthands
        shs = set()
        for n, s in enumerate(midi_steps.items()): 
            notes = s[1]
            for note in notes:
                if note != 81:
                    sh = drumkit_note_shs[note]
                    shs.add(sh)
        
        # create empty pattern dictionary with the necessary drum keys
        pattern = defaultdict(list)
        for sh in shs:
            for n in range(len(midi_steps.items())):
                pattern[sh].append("_")
        
        # replace empty slots with corresponding drum hits
        for n, s in enumerate(midi_steps.items()): 
            notes = s[1]
            for note in notes:
                if note != 81:
                    sh = drumkit_note_shs[note]
                    pattern[sh][n] = "x"
        
        patterns = defaultdict(dict)
        patterns["01"] = pattern
        return patterns

    # def midi_steps_to_pattern_triple_array(self, midi_steps, vdk):
    #     """Convert a parsed midi steps dictionary to vjpy pattern for 3-array video beat."""
    #     drumkit_note_shs = {}
    #     for drum in vdk.drums.values():
    #         drumkit_note_shs[drum.note] = drum.short_hand
    #     arrays = ["1", "2", "3"] # Drum groups. 1: cymbals, 2: snare, toms, 3: pedals
    #     array_d = {
    #         "h": "1",
    #         "r": "1",
    #         "x": "1",
    #         "c": "1",
    #         "o": "1",
    #         "t": "2",
    #         "w": "2",
    #         "s": "2",
    #         "z": "2",
    #         "k": "3"
    #         }
    #     # create empty pattern dictionary with the necessary drum group keys
    #     pattern = defaultdict(list)
    #     for a in arrays:
    #         for n in range(len(midi_steps.items())):
    #             pattern[a].append("_")
        
    #     # replace empty slots with corresponding drum hits
    #     for n, s in enumerate(midi_steps.items()): 
    #         notes = s[1]
    #         for note in notes:
    #             sh = drumkit_note_shs[note]
    #             a_ = array_d[sh]
    #             pattern[a_][n] = sh
    #     patterns = defaultdict(dict)
    #     patterns["01"] = pattern
    #     return patterns