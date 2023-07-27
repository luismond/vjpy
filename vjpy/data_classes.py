#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:48:54 2023

@author: user
"""

from pydantic import BaseModel

# Data Classes

class Pattern(BaseModel):
    bars: str
    beats: str
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
