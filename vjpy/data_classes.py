"""vjpy data classes."""

from typing import Optional
from pydantic import BaseModel, constr


class Bar(BaseModel):
    """Musical measure containing patterns."""

    bar_num: int
    patterns: list[str]


class Pattern(BaseModel):
    """Pattern."""

    pattern: Optional[constr(min_length=8, max_length=8)]


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
