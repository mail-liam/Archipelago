from __future__ import annotations

import typing as t

from ..constants import AVItemType
from ..items import item_data


if t.TYPE_CHECKING:
    from BaseClasses import CollectionState


def always_accessible(state: CollectionState, player: int):
    return True


def can_angle_shoot(state: CollectionState, player: int):
    return state.has_any(("Nova",), player)


def can_damage(state: CollectionState, player: int):
    # guns = [item.name for item in item_data.values() if item.group_name == AVItemType.WEAPON]
    # return state.has_any([*guns, "Red Coat"], player) or can_drill(state, player)
    return state.has_any(("DataDisruptor", "Voranj"), player)


def can_drill(state: CollectionState, player: int):
    return state.has_any(("Drill", "Drone", "Progressive Drone"), player)


def can_pierce_wall(state: CollectionState, player: int):
    return state.has_any(("Kilver",), player)


def has_any_coat(state: CollectionState, player: int):
    return state.has_any(("White Coat", "Brown Coat", "Red Coat", "Progressive Coat"), player)


# has_address_1
# has_address_2
# has_address_bomb
# has_trenchcoat
# has_red_coat
# has_grapple
# has_password
# can_cross_high_jump
# has_drone
# has_drone_tele
# has_key
# has_fatbeam
