"""Drumkits."""
from vjpy import Drumkit, Drum

drum_kits = {
    "TR808EmulationKit": Drumkit(
        name="TR808EmulationKit",
        drums={
            "kick1": Drum(name="kick1", note=36, short_hand="k", emoji="🥾"),
            "kick2": Drum(name="kick2", note=37, short_hand="q", emoji="👟"),
            "snare1": Drum(name="snare1", note=38, short_hand="s", emoji="🥁"),
            "clap1": Drum(name="clap1", note=40, short_hand="c", emoji="👏"),
            "tom1": Drum(name="tom1", note=42, short_hand="t", emoji="🪘"),
            "hat1": Drum(name="hat1", note=44, short_hand="h", emoji="🔔"),
            "hato": Drum(name="hato", note=46, short_hand="o", emoji="🐍"),
            "shkr": Drum(name="shaker", note=48, short_hand="r", emoji="🧂"),
            "clve": Drum(name="clave", note=50, short_hand="v", emoji="🪵"),
            "cwbl": Drum(name="cowbell", note=51, short_hand="w", emoji="🐄")
            }
        ),
    "myfunkkit": Drumkit(
        name="myfunkkit",
        drums={
            "kick": Drum(name="kick", note=36, short_hand="k", emoji="🥾"),
            "snare": Drum(name="snare", note=38, short_hand="s", emoji="👏"),
            "hat": Drum(name="hat", note=42, short_hand="h", emoji="🔔"),
            "hat_open": Drum(name="hat_open", note=40, short_hand="o", emoji="🐍"),
            "silence": Drum(name="silence", note=81, short_hand="_")
            }
        ),
    "reasonkit": Drumkit(
        name="reasonkit",
        drums={
            "kick": Drum(name="kick", note=36, short_hand="k", emoji="🥾"),
            "snare": Drum(name="snare", note=38, short_hand="s", emoji="🥁"),
            "rim": Drum(name="rim", note=37, short_hand="c", emoji="👏"),
            "tom_high": Drum(name="tom_high", note=45, short_hand="t", emoji="🪘"),
            "tom_mid": Drum(name="tom_mid", note=43, short_hand="h", emoji="🔔"),
            "tom_low": Drum(name="tom_low", note=41, short_hand="o", emoji="🐍"),
            "hh1": Drum(name="hh1", note=42, short_hand="o", emoji="🐍"),
            "hh2": Drum(name="hh2", note=46, short_hand="o", emoji="🐍"),
            "hh3": Drum(name="hh3", note=44, short_hand="o", emoji="🐍"),
            "crash1": Drum(name="crash1", note=49, short_hand="r", emoji="🧂"),
            "crash2": Drum(name="crash2", note=57, short_hand="r", emoji="🧂"),
            "ride": Drum(name="ride", note=51, short_hand="v", emoji="🪵"),
            "bell": Drum(name="bell", note=81, short_hand="w", emoji="🐄")
            }
        ),
    }
