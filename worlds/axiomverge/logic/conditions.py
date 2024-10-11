from __future__ import annotations

import typing as t

from ..constants import AVItemType
from ..items import item_data


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
    # guns = [item.name for item in item_data.values() if item.group_name == AVItemType.WEAPON]
    # return state.has_any([*guns, "RedCoat"], player) or can_drill(state, player)
    return state.has_any(("DataDisruptor", "Voranj"), player)


def can_drill(state: CollectionState, player: int):
    return state.has_any(("Drill", "Drone", "Progressive Drone"), player)


def can_pierce_wall(state: CollectionState, player: int):
    return state.has_any(("Kilver",), player)


def has_any_glitch(state: CollectionState, player: int):
    return state.has_any(("AddressDisruptor1", "AddressDisruptor2", "GlitchBomb"), player)


def has_any_coat(state: CollectionState, player: int):
    return state.has_any(("White Coat", "Trenchcoat", "RedCoat", "Progressive Coat"), player)


def has_drone(state: CollectionState, player: int):
    return state.has_any(("Drone", "Progressive Drone"), player)


def has_drone_tele(state: CollectionState, player: int):
    return state.has("Drone Teleport", player) or state.has("Progressive Drone", player, count=3)


def has_glitch_2(state: CollectionState, player: int):
    return state.has_any(("AddressDisruptor2", "GlitchBomb"), player)


def has_red_coat(state: CollectionState, player: int):
    return state.has("RedCoat", player) or state.has("Progressive Coat", player, count=3)


def has_trenchcoat(state: CollectionState, player: int):
    return state.has_any(("Trenchcoat", "RedCoat"), player) or state.has("Progressive Coat", player, count=2)


# has_trenchcoat
# has_grapple
# has_password
# can_cross_high_jump
# has_key
# has_fatbeam
