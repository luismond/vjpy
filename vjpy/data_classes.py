"""vjpy data classes."""

from pydantic import BaseModel


class Pattern(BaseModel):
    """Pattern."""

    pattern: str

class Drumkit(BaseModel):
    """Object representing a collection of drums."""

    name: str
    drums: dict

class Drum(BaseModel):
    """Object representing a drum (with name, note, shorthand and emoji)."""

    name: str
    note: int
    short_hand: str
    emoji: str

class NoteValue(BaseModel):
    """Object representing a note value."""

    name: str
    relative_value: float
