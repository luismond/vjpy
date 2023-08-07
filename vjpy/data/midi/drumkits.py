"""vjpy drumkits."""

from vjpy.data_classes import Drumkit, Drum

TR808EmulationKit = Drumkit(
    name='TR808EmulationKit',
    drums={
        'kick': Drum(name='kick', note=36, short_hand='k'),
        'snare': Drum(name='snare', note=38, short_hand='s'),
        'clap': Drum(name='clap', note=40, short_hand='c'),
        'tom': Drum(name='tom', note=43, short_hand='t'),
        'hat': Drum(name='hat', note=45, short_hand='h'),
        'conga': Drum(name='conga', note=49, short_hand='g'),
        'clave': Drum(name='clave', note=50, short_hand='v'),
        'cowbell': Drum(name='cowbell', note=51, short_hand='w'),
        }
    )


My808kit = Drumkit(
    name='my808kit',
    drums={
        'bongo': Drum(name='bongo', note=36, short_hand='b'),
        'conga': Drum(name='conga', note=38, short_hand='g'),
        'crash': Drum(name='crash', note=40, short_hand='x'),
        'hat': Drum(name='hat', note=43, short_hand='h'),
        'kick': Drum(name='kick', note=45, short_hand='k'),
        'ride': Drum(name='ride', note=49, short_hand='r'),
        'snare': Drum(name='snare', note=50, short_hand='c'),
        'snare2': Drum(name='snare2', note=51, short_hand='z'),
        'tom': Drum(name='tom', note=51, short_hand='t')
        }
    )

MyFunkKit = Drumkit(
    name='MyFunkKit',
    drums={
        'kick': Drum(name='kick', note=43, short_hand='k'),
        'hat': Drum(name='hat', note=38, short_hand='h'),
        'clap': Drum(name='clap', note=40, short_hand='c')
        }
    )


def get_drum_midi_notes_to_names(drumkit):
    """Drum-midi-notes <-> Drum-wav-names map."""
    drum_names = {}
    for drum in drumkit.drums.values():
        drum_names[drum.note] = drum.name
    return drum_names