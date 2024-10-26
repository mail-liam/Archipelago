from __future__ import annotations

import typing as t

from .constants import AVItemType
from .items import item_data
from .options import AllowWallGrappleClips

if t.TYPE_CHECKING:
    from BaseClasses import CollectionState
    from .types import LogicContext


ALL_WEAPONS = tuple(item.name for item in item_data.values() if item.group_name == AVItemType.WEAPON)


# Logic primitives that are used either independently or part of more complex expressions
def not_implemented(state: CollectionState, context: LogicContext):
    """Sentinel function for unimplemented logic."""
    return has_trenchcoat(state, context)


def always_accessible(state: CollectionState, context: LogicContext):
    return True


def any_coat(state: CollectionState, context: LogicContext):
    return state.has_any(("Modified Lab Coat", "Trenchcoat", "Red Coat", "Progressive Coat"), context.player)


def any_glitch(state: CollectionState, context: LogicContext):
    return state.has_any(("Address Disruptor 1", "Address Disruptor 2", "Address Bomb", "Progressive Address Disruptor"), context.player)


def any_height(state: CollectionState, context: LogicContext):
    return has_trenchcoat(state, context) or has_drone_tele(state, context) or has_grapple(state, context) or has_high_jump(state, context)


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


def easy_grapple_clip(state: CollectionState, context: LogicContext):
    return has_grapple(state, context) and context.wall_grapple_clip_difficulty >= AllowWallGrappleClips.option_easy


def extra_brown_height(state: CollectionState, context: LogicContext):
    return has_strict_trenchcoat(state, context) and (
        context.brown_rocket_jump_enabled or has_high_jump(state, context)
    )


def floor_grapple_clip(state: CollectionState, context: LogicContext):
    return has_grapple(state, context) and context.floor_grapple_clip_enabled


def has_drone(state: CollectionState, context: LogicContext):
    return state.has_any(("Remote Drone", "Progressive Drone"), context.player)


def has_drone_launch(state: CollectionState, context: LogicContext):
    return state.has_all(("Remote Drone", "Enhanced Drone Launch"), context.player) or state.has("Progressive Drone", context.player, count=2)


def has_drone_tele(state: CollectionState, context: LogicContext):
    return has_drone(state, context) and state.has("Drone Teleport", context.player)


def has_fat_beam(state: CollectionState, context: LogicContext):
    return state.has("Fat Beam", context.player)


def has_glitch_2(state: CollectionState, context: LogicContext):
    return state.has_any(("Address Disruptor 2", "Address Bomb"), context.player) or state.has("Progressive Address Disruptor", context.player, count=2)


def has_glitch_bomb(state: CollectionState, context: LogicContext):
    return state.has(("Address Bomb",), context.player) or has_red_coat(state, context)


def has_grapple(state: CollectionState, context: LogicContext):
    return state.has("Grapple", context.player)


def has_high_jump(state: CollectionState, context: LogicContext):
    return state.has("Field Disruptor", context.player)


def has_passcode(state: CollectionState, context: LogicContext):
    return state.has("Passcode Tool", context.player)


def has_power_nodes(state: CollectionState, context: LogicContext, count: int):
    return True  # TODO: Implement properly when decided upon
    # if not context.node_requirements_enabled:
    #     return True  # Short-circuit if not enabled
    # NOTE: This doesn't work atm due to specific names for Nodes
    # May need the mod to treat Nodes/Fragments like Progressive Items?
    # return state.has("Power Node", context.player, count=2) or state.has("Power Node Fragment", context.player, count=12)


def has_red_coat(state: CollectionState, context: LogicContext):
    return state.has("Red Coat", context.player) or state.has("Progressive Coat", context.player, count=3)


def has_strict_trenchcoat(state: CollectionState, context: LogicContext):
    return state.has("Trenchcoat", context.player) or state.has("Progressive Coat", context.player, count=2)


def has_trenchcoat(state: CollectionState, context: LogicContext):
    return state.has_any(("Trenchcoat", "Red Coat"), context.player) or state.has("Progressive Coat", context.player, count=2)


def roof_grapple_clip(state: CollectionState, context: LogicContext):
    return has_grapple(state, context) and context.roof_grapple_clip_enabled




# has_key


# Specific location checks, that are here mainly to avoid complexity in the data structure
def west_caves_pool_access(s: CollectionState, c: LogicContext):
    return (
        has_red_coat(s, c)
        or has_drone(s, c) and has_glitch_2(s, c) and (
            s.has_any(("Grapple", "Drone Teleport"), c.player) or has_trenchcoat(s, c)
        )
    )


def dingergisbar_access(s: CollectionState, c: LogicContext):
    return (
        has_passcode(s, c) and (
            has_red_coat(s, c) and (has_grapple(s, c) or has_drone_tele(s, c))
            or has_glitch_2(s, c) and has_drone_tele(s, c) and (
                has_drone_launch(s, c) or c.flight_enabled or (
                    has_strict_trenchcoat(s, c) and (has_grapple(s, c) or c.brown_rocket_jump_enabled and has_high_jump(s, c))
                )
            )
        )
    )


def upper_eribu_bomb_access(s: CollectionState, c: LogicContext):
    return has_glitch_bomb(s, c) and (
        has_trenchcoat(s, c)
        or has_drone_tele(s, c)
        or has_high_jump(s, c) and (has_grapple(s, c) or has_drone(s, c))
    )


def bubble_jail_access(s: CollectionState, c: LogicContext):
    return (
        can_angle_shoot(s, c)
        or can_pierce_wall(s, c)
        or has_red_coat(s, c)
        or has_grapple(s, c)
        or has_drone(s, c)
        or has_strict_trenchcoat(s, c) and can_damage_boss(s, c)
    )


def outside_lab_access(s: CollectionState, c: LogicContext):
    return has_red_coat(s, c) or has_drone(s, c) or (
        can_drill(s, c) and (can_angle_shoot(s, c) or can_pierce_wall(s, c) or has_strict_trenchcoat(s, c) or has_grapple(s, c))
    )


def xedur_access(s: CollectionState, c: LogicContext):
    return can_pierce_wall(s, c) or can_angle_shoot(s, c) or has_trenchcoat(s, c) or has_drone(s, c) or s.has_any(("Grapple", "Field Disruptor"), c.player)


def laboratory_access(s: CollectionState, c: LogicContext):
    return (
        has_red_coat(s, c)
        or can_drill(s, c) and (has_grapple(s, c) or has_strict_trenchcoat(s, c) and (c.brown_rocket_jump_enabled or has_high_jump(s, c)))
    ) and (has_fat_beam(s, c) or has_passcode(s, c)) or has_drone_tele(s, c) and has_passcode(s, c)


def dalkhu_subtum_access(s: CollectionState, c: LogicContext):
    return has_passcode(s, c) and (
        has_grapple(s, c)
        or has_red_coat(s, c)
        or has_drone_tele(s, c)
        or has_drone(s, c) and any_glitch(s, c) and has_high_jump(s, c)
        or has_strict_trenchcoat(s, c) and (has_drone(s, c) or has_high_jump(s, c))
    )


def basic_attic_access(s: CollectionState, c: LogicContext):
    return has_red_coat(s, c) or has_grapple(s, c) or has_drone(s, c) or extra_brown_height(s, c)


def attic_transition_upper(s: CollectionState, c: LogicContext):
    return has_glitch_bomb(s, c) and (
        has_red_coat(s, c) or has_grapple(s, c) or has_drone_tele(s, c) or extra_brown_height(s, c)
    )


def attic_far_right_access(s: CollectionState, c: LogicContext):
    return (
        has_red_coat(s, c)
        or has_drone(s, c) and (
            has_grapple(s, c) or has_drone_tele(s, c) or has_high_jump(s, c) or has_drone_launch(s, c) or has_strict_trenchcoat(s, c)
        )
        or has_strict_trenchcoat(s, c) and (has_grapple(s, c) or has_high_jump(s, c))
    )


def elsenova_east_attic_access(s: CollectionState, c: LogicContext):
    return has_glitch_2(s, c) and (
        has_drone_tele(s, c) or has_trenchcoat(s, c) or has_high_jump(s, c)
    )


def floating_platform_access(s: CollectionState, c: LogicContext):
    return has_drone(s, c) or has_trenchcoat(s, c) or (
        can_drill(s, c) and (has_high_jump(s, c) or has_grapple(s, c) or any_glitch(s, c))
    )


def zombie_tunnel_access(s: CollectionState, c: LogicContext):
    return has_red_coat(s, c) or has_strict_trenchcoat(s, c) and (
        c.brown_rocket_jump_enabled or has_drone_tele(s, c) or has_grapple(s, c) or has_high_jump(s, c)
    )


def basement_regular_access(s: CollectionState, c: LogicContext):
    return has_glitch_2(s, c) and any_coat(s, c) and (has_drone(s, c) or has_red_coat(s, c) and roof_grapple_clip(s, c))


def gated_alcove_access(s: CollectionState, c: LogicContext):
    return can_drill(s, c) and (
        any_glitch(s, c) or easy_grapple_clip(s, c) or any_coat(s, c)
        or s.has_any(("Flamethrower", "Scissor Beam", "Reverse Slicer", "Fat Beam"), c.player)
    )


def lower_east_zi_access(s: CollectionState, c: LogicContext):
    return can_damage(s, c) or has_glitch_2(s, c) or has_trenchcoat(s, c)
