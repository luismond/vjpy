"""vjpy video class."""

import os
from collections import defaultdict
from moviepy.editor import (
    VideoFileClip,
    concatenate_videoclips,
    clips_array,
    vfx
    )
from vjpy import Drumkit, Drum


class VideoDevice:
    """vjpy video class."""

    def __init__(self, vj):
        self.note_value = vj.note_value

    def make_videoclip(self, bankname):
        """Make a video object."""
        filepath = os.path.join("soundbanks", bankname, f"{bankname}.mp4")
        return VideoFileClip(filepath)

    def get_vdk(self, videoclip):
        """Video drum kit."""
        vdk = Drumkit(
            name="videokit",
            drums={
                "k": Drum(name="kick", note=36, short_hand="k",
                          clip=self.get_subclip(videoclip, start=24.950)),
                "s": Drum(name="snare", note=38, short_hand="s",
                          clip=self.get_subclip(videoclip, start=27.5128)),
                "z": Drum(name="snare2", note=40, short_hand="z",
                          clip=self.get_subclip(videoclip, start=29.5085)),
                "t": Drum(name="tom1", note=45, short_hand="t",
                          clip=self.get_subclip(videoclip, start=31.4610)),
                "w": Drum(name="tom2", note=43, short_hand="w",
                          clip=self.get_subclip(videoclip, start=38.9788)),
                "r": Drum(name='ride', note=51, short_hand="r",
                          clip=self.get_subclip(videoclip, start=03.7158)),
                "x": Drum(name="china", note=49, short_hand="x",
                          clip=self.get_subclip(videoclip, start=07.1222)),
                "c": Drum(name="crash", note=57, short_hand="c",
                          clip=self.get_subclip(videoclip, start=09.7210)),
                "h": Drum(name="hat", note=42, short_hand="h",
                          clip=self.get_subclip(videoclip, start=21.2910)),
                "o": Drum(name="hat_open", note=46, short_hand="o",
                          clip=self.get_subclip(videoclip, start=23.0869)),
                "_": Drum(name="silence", note=81, short_hand="_",
                          clip=self.get_subclip(videoclip, start=06.005)),
                }
            )
        return vdk

    def get_subclip(self, videoclip, start=0):
        """Get a subclip from a video object."""
        return videoclip.subclip(start, start + self.note_value)

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

    def concat_drum_subpatterns(
            self,
            patterns,
            drum_subclips,
            bankname,
            beatname,
            loops_n=1):
        """Concatenate and write each drum sub-pattern separately."""
        soundbank_dir_path = os.path.join("soundbanks", bankname)
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
                soundbank_dir_path, 'beats', f'{beatname}', f'{key}.mp4'
                )
            self.write_concatenated_subclips(final_clip, final_clip_path)

    def concatenate_subclips(self, subclips):
        """Concatenate an array of subclips."""
        return concatenate_videoclips(subclips)

    def write_concatenated_subclips(self, concatenated_subclips, subclip_name):
        """Write concatenated subclips."""
        concatenated_subclips.write_videofile(subclip_name)

    def composite_vertical_videobeat(self, patterns, bankname, beatname):
        """Composite a polyphonic vertical video array from concatenated drum subclips."""
        dks = list(patterns["01"].keys())
        soundbank_dir_path = os.path.join("soundbanks", bankname)
        beat_path = os.path.join(soundbank_dir_path, "beats", f"{beatname}")
        clip1 = VideoFileClip(os.path.join(beat_path, f"{dks[0]}.mp4")).fx(vfx.mirror_x)
        clip2 = VideoFileClip(os.path.join(beat_path, f"{dks[1]}.mp4"))
        clip3 = VideoFileClip(os.path.join(beat_path, f"{dks[2]}.mp4")).fx(vfx.mirror_x)
        video = clips_array([[clip1],
                             [clip2],
                             [clip3]])
        video.resize(width=960).write_videofile(
            os.path.join(beat_path, f"{beatname}_array.mp4"))

    def render_monophonic_video(self, vdk, videoclip, midi_steps):
        """Monophonic video rendering."""
        midi_steps_ = []
        for x in midi_steps:
            y = midi_steps[x]
            midi_steps_.append(y[0])
        drumkit_note_shs = {}
        for drum in vdk.drums.values():
            drumkit_note_shs[drum.note] = drum.short_hand
        subclips = []
        for note in midi_steps_:
            sh = drumkit_note_shs[note]
            subclip = vdk.drums[sh].clip
            subclips.append(subclip)
        final_clip = self.concatenate_subclips(subclips*4)
        self.write_concatenated_subclips(final_clip, "final_clip.mp4")
