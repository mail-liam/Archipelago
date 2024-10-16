from __future__ import annotations

import typing as t

from ..constants import AVItemType
from ..items import item_data

if t.TYPE_CHECKING:
    from ..types import LogicContext


ALL_WEAPONS = tuple(item.name for item in item_data.values() if item.group_name == AVItemType.WEAPON)


if t.TYPE_CHECKING:
    from BaseClasses import CollectionState


def not_implemented(state: CollectionState, context: LogicContext):
    """Sentinel function for unimplemented logic."""
    return True


def always_accessible(state: CollectionState, context: LogicContext):
    return True


def can_angle_shoot(state: CollectionState, context: LogicContext):
    return state.has_any(("Nova",), context.player)


def can_damage_boss(state: CollectionState, context: LogicContext):
    # We need this as Drone cannot be fired during a boss battle
    return state.has_any((*ALL_WEAPONS, "Laser Drill"), context.player) or has_red_coat(state, context)


def can_damage(state: CollectionState, context: LogicContext):
    return can_damage_boss(state, context) or has_drone(state, context)


def can_displacement_warp(state: CollectionState, context: LogicContext):
    return context.displacement_warp_enabled and has_drone(state, context)


def can_drill(state: CollectionState, context: LogicContext):
    return state.has_any(("Laser Drill", "Remote Drone", "Progressive Drone"), context.player) or has_red_coat(state, context)


def can_pierce_wall(state: CollectionState, context: LogicContext):
    return state.has_any(("Kilver", "Reverse Slicer"), context.player)


def has_any_glitch(state: CollectionState, context: LogicContext):
    return state.has_any(("Address Disruptor 1", "Address Disruptor 2", "Address Bomb"), context.player)


def has_any_coat(state: CollectionState, context: LogicContext):
    return state.has_any(("Modified Lab Coat", "Trenchcoat", "Red Coat", "Progressive Coat"), context.player)


def has_drone(state: CollectionState, context: LogicContext):
    return state.has_any(("Remote Drone", "Progressive Drone"), context.player)


def has_drone_tele(state: CollectionState, context: LogicContext):
    return state.has_all(("Remote Drone", "Drone Teleport"), context.player)


def has_glitch_2(state: CollectionState, context: LogicContext):
    return state.has_any(("Address Disruptor 2", "Address Bomb"), context.player)


def has_glitch_bomb(state: CollectionState, context: LogicContext):
    return state.has(("Address Bomb",), context.player) or has_red_coat(state, context)


def has_passcode(state: CollectionState, context: LogicContext):
    return state.has("Passcode Tool", context.player)


def has_red_coat(state: CollectionState, context: LogicContext):
    return state.has("Red Coat", context.player) or state.has("Progressive Coat", context.player, count=3)


def has_trenchcoat(state: CollectionState, context: LogicContext):
    return state.has_any(("Trenchcoat", "Red Coat"), context.player) or state.has("Progressive Coat", context.player, count=2)


# has_grapple
# can_cross_high_jump
# has_key
# has_fatbeam
