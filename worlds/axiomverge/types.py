from dataclasses import dataclass

@dataclass
class LogicContext:
    displacement_warp_enabled: bool
    flight_enabled: bool
    grapple_clip_enabled: bool
    player: int