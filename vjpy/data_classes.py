"""vjpy data classes."""

from pydantic import BaseModel


class Bar(BaseModel):
    """Musical bar (measure of n beats)."""

    num: int
    content: list[str]


class Pattern(BaseModel):
    """Pattern (string using abbreviations of note names. See drumkits.py)."""

    pattern: str


class Drumkit(BaseModel):
    """Object representing a collection of drums."""

    name: str
    drums: dict


class Drum(BaseModel):
    """Object representing a drum (with name, note, shorthand)."""

    name: str
    note: int
    short_hand: str


class NoteValue(BaseModel):
    """Object representing a note value."""

    name: str
    relative_value: float
