from __future__ import annotations

import typing as t

from ..constants import AVItemType
from ..items import item_data


ALL_WEAPONS = tuple(item.name for item in item_data.values() if item.group_name == AVItemType.WEAPON)


if t.TYPE_CHECKING:
    from BaseClasses import CollectionState


def not_implemented(state: CollectionState, player: int):
    """Sentinel function for unimplemented logic."""
    return True


def always_accessible(state: CollectionState, player: int):
    return True


def can_angle_shoot(state: CollectionState, player: int):
    return state.has_any(("Nova",), player)


def can_damage(state: CollectionState, player: int):
    return state.has_any(ALL_WEAPONS, player) or can_drill(state, player)


def can_drill(state: CollectionState, player: int):
    return state.has_any(("Laser Drill", "Remote Drone", "Progressive Drone"), player) or has_red_coat(state, player)


def has_glitch_bomb(state: CollectionState, player: int):
    return state.has(("Address Bomb"), player) or has_red_coat(state, player)


def can_pierce_wall(state: CollectionState, player: int):
    return state.has_any(("Kilver",), player)


def has_any_glitch(state: CollectionState, player: int):
    return state.has_any(("Address Disruptor 1", "Address Disruptor 2", "Address Bomb"), player)


def has_any_coat(state: CollectionState, player: int):
    return state.has_any(("Modified Lab Coat", "Trenchcoat", "Red Coat", "Progressive Coat"), player)


def has_drone(state: CollectionState, player: int):
    return state.has_any(("Remote Drone", "Progressive Drone"), player)


def has_drone_tele(state: CollectionState, player: int):
    return state.has_all(("Remote Drone", "Drone Teleport"), player)


def has_glitch_2(state: CollectionState, player: int):
    return state.has_any(("Address Disruptor 2", "Address Bomb"), player)


def has_red_coat(state: CollectionState, player: int):
    return state.has("Red Coat", player) or state.has("Progressive Coat", player, count=3)


def has_trenchcoat(state: CollectionState, player: int):
    return state.has_any(("Trenchcoat", "Red Coat"), player) or state.has("Progressive Coat", player, count=2)


# has_trenchcoat
# has_grapple
# has_password
# can_cross_high_jump
# has_key
# has_fatbeam
