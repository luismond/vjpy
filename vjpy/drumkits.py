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


# define a local drumkit
my808kit = Drumkit(
    name='my808kit',
    drums={
        'bongo': Drum(name='bongo', note=36, short_hand='b'),
        'conga': Drum(name='conga', note=38, short_hand='c'),
        'crash': Drum(name='crash', note=40, short_hand='x'),
        'hat': Drum(name='hat', note=43, short_hand='h'),
        'kick': Drum(name='kick', note=45, short_hand='k'),
        'ride': Drum(name='ride', note=49, short_hand='r'),
        'snare': Drum(name='snare', note=50, short_hand='s'),
        'snare2': Drum(name='snare2', note=51, short_hand='z'),
        'tom': Drum(name='tom', note=51, short_hand='t')
        }
    )


def get_my808kit_paths():
    """Get my drumkit drum paths."""
    my808kit_drum_paths = {}
    MY808_KIT_PATH = "wavs/my808kit"
    for drum_ in my808kit.drums.values():
        my808kit_drum_paths[drum_.note] = f"{MY808_KIT_PATH}/{drum_.name}.wav"
    return my808kit_drum_paths
