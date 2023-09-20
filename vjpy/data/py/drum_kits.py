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
        )
    }
