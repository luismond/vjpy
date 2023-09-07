# -*- coding: utf-8 -*-

#%% todo: parse midi file and use it to sequence videobeats
import mido

mid_name = 'vjpy/data/midi/drum_beat.mid'   # midi file
mid = mido.MidiFile(mid_name, clip=True)    # midi object
tracks = mid.tracks                         # midi tracks
transport = tracks[0]                       # transport
inst = tracks[1]                            # instrument 1 (drum machine)

# meta messages
inst_track_name = inst[0].name              # track name ('Hip Hop Kit 03')
inst_name = inst[1].name                    # instrument name ('Hip Hop Kit 03')
inst_port = inst[2]                         # midi port

# messages
messages = [m for m in inst[3:-1]]          # midi messages

# message
m = messages[0]                             # midi message
m_type = m.type                             # midi message type ('note on', 'note off')
m_note = m.note                             # midi message note (int)
m_time = m.time                             # midi message time (int)
m_velo = m.velocity                         # midi message velocity (int)

messages[:20]

notes = set()

for m in messages:
    notes.add(m.note)