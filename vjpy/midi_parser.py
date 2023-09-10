"""midi file parser."""

import os
from vjpy import VjPyDevice
import mido
# from collections import defaultdict

VJPD = VjPyDevice(bpm=120)                  # vjpy device

# Hydrogen MIDI file (modus SMF0)
                                            # MIDI
MD = VJPD.midi_device                           # device
MID_NAME = os.path.join(                        # file
    MD.midi_data_dir, "drum_beat_2.mid")
mid = mido.MidiFile(MID_NAME, clip=True)        # object
track = mid.tracks[0]                           # track

meta_messages = [msg for msg in track[:4]]          # meta messages
copyright_ = meta_messages[0]                           # copyright
track_name = meta_messages[1]                           # name
tempo = meta_messages[2]                                # tempo
time_signature = meta_messages[3]                       # signature
dur = 60000/(114*tempo.tempo)                           # duration in ms?

messages = [msg for msg in track[4:-1]]             # messages
m = messages[0]
m_type = m.type                                         # type ('note on', 'note off')
m_note = m.note                                         # note (int)
m_time = m.time                                         # time (int)
m_velo = m.velocity                                     # velocity (int)


# # times = defaultdict(list)
# # for m in messages:
# #     if m.type == "note_on":
# #         times[m.time].append(m)

# # for k, v in times.items():
# #     print(f"{k}\t{v}")
# messages#[:20]
