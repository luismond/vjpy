from pydantic import BaseModel

class Bar(BaseModel):
    num: int
    content: list[str]

class Pattern(BaseModel):
    pattern: str

class Drumkit(BaseModel):
    name: str
    drums: dict


class Drum(BaseModel):
    name: str
    note: int
    short_hand: str


class NoteValue(BaseModel):
    name: str
    relative_value: float


