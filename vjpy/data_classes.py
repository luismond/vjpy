"""vjpy data classes."""

from pydantic import BaseModel, Field
from typing import Optional, Any, List

class Pattern(BaseModel):
    """Pattern."""
    x: str # timeline
    a: List[str] = Field(max_length=8)
    b: List[str] = Field(max_length=8)


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
    clip: Optional[Any] = None

class NoteValue(BaseModel):
    """Object representing a note value."""

    name: str
    relative_value: float

class Bass(BaseModel):
    """Object representing a bass guitar."""

    name: str
    notes: dict

class BassNote(BaseModel):
    """Object representing a bass note."""

    name: str
    note: int
    short_hand: str
    clip: Optional[Any] = None

# todo: develop the pattern model
# patterns = {
#     "01": Pattern(
#         x="  1    2    3    4    5    6    7    8",
#         a= ["x", "_", "_", "_", "_", "_", "_", "_"],
#         b= ["x", "_", "_", "_", "_", "_", "_", "_"]
#         )
#     }