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
        'kick': Drum(name='kick', note=36, short_hand='k'),
        'snare': Drum(name='snare', note=38, short_hand='s'),
        'tom': Drum(name='tom', note=43, short_hand='t'),
        'hat': Drum(name='hat', note=45, short_hand='h'),
        }
    )


my808kit_drum_paths = {}
MY808_KIT_PATH = "wavs/my808kit"
for drum_ in my808kit.drums.values():
    my808kit_drum_paths[drum_.note] = f"{MY808_KIT_PATH}/{drum_.name}.wav"
