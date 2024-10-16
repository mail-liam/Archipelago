import typing as t
from dataclasses import dataclass

from BaseClasses import CollectionState

@dataclass
class LogicContext:
    displacement_warp_enabled: bool
    flight_enabled: bool
    grapple_clip_enabled: bool
    rocket_jump_enabled: bool
    player: int


AccessRule = t.Callable[[CollectionState, LogicContext], bool]
