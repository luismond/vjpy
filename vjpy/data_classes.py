"""vjpy data classes."""

from pydantic import BaseModel
from typing import Optional, Any


class Drumkit(BaseModel):
    """Object representing a collection of drums."""

    name: str
    drums: dict


class Drum(BaseModel):
    """Object representing a drum (with name, note, shorthand and emoji)."""

    name: str
    note: int
    short_hand: str
    emoji: Optional[str] = None
    start: Optional[float] = None


class VideoDrumkit(BaseModel):
    """Object representing a collection of video drums."""

    name: str
    drums: dict


class VideoDrum(BaseModel):
    """Object representing a drum (with name, note, shorthand and emoji)."""

    name: str
    note: int
    short_hand: str
    clip: Optional[Any] = None
    start: float

class NoteValue(BaseModel):
    """Object representing a note value."""

    name: str
    relative_value: float
