"""vjpy backend."""

from vjpy import NoteValue, MidiDevice, WavDevice, drum_kits


class VjPyDevice:
    """vjpy device."""

    def __init__(self, bpm=100, resolution="1/4"):
        self.bpm = bpm
        self.resolution = resolution
        self.drum_kit = drum_kits["TR808EmulationKit"]

        self.midi_device = MidiDevice(
            bpm=self.bpm,
            resolution=self.resolution,
            note_values=self.note_values,
            drumkit_sh_notes=self.drumkit_sh_notes
            )

        self.wav_device = WavDevice()

        # self.video_device = VideoDevice()

    @property
    def note_values(self):
        """Musical definitions of notes' values."""
        note_values = {
            '1': NoteValue(name='whole_note', relative_value=1.0),
            '1/2': NoteValue(name='half_note', relative_value=0.5),
            '1/4': NoteValue(name='quarter_note', relative_value=0.25),
            '1/8': NoteValue(name='eigth_note', relative_value=0.125),
            '1/16': NoteValue(name='sixteenth_note', relative_value=0.0625),
            '1/32': NoteValue(name='thirty-second_note', relative_value=0.0312)
            }
        return note_values

    @property
    def drumkit_sh_names(self):
        """Mapping short-hand-names <-> full-names."""
        drumkit_sh_names = {}
        for drum in self.drum_kit.drums.values():
            drumkit_sh_names[drum.short_hand] = drum.name
        return drumkit_sh_names

    @property
    def drumkit_sh_notes(self):
        """Mapping short-hand-names <-> notes."""
        drumkit_sh_notes = {}
        for drum in self.drum_kit.drums.values():
            drumkit_sh_notes[drum.short_hand] = drum.note
        return drumkit_sh_notes

    @property
    def drumkit_note_names(self):
        """Mapping notes <-> note names."""
        drumkit_note_names = {}
        for drum in self.drum_kit.drums.values():
            drumkit_note_names[drum.note] = drum.name
        return drumkit_note_names

# from moviepy.editor import (
#     VideoFileClip,
#     CompositeVideoClip,
#     concatenate_videoclips,
#     clips_array,
#     vfx
#     )
# from moviepy.audio.fx.all import volumex


# class VideoDevice:
#     def __init__(self):
#         self.soundbanks_path = os.path.join('soundbanks')

#     def get_videoclip(self, video_filename):
#         return VideoFileClip(video_filename)

#     def get_videosubclip(self, video_clip, start=0, duration=.075):
#         return video_clip.subclip(start, start + duration)

#     def concatenate_subclips(self, subclips):
#         return concatenate_videoclips(subclips)

#     def get_bars_subclips(self, bars):
#         subclips = []
#         for bar_ in bars:
#             for patt in bar_:
#                 for subclip in patt:
#                     subclips.append(subclip)
#         return subclips

#     def write_concatenated_subclips(self, concatenated_subclips, subclip_name):
#         concatenated_subclips.write_videofile(subclip_name)

    # todo: implement compositing
