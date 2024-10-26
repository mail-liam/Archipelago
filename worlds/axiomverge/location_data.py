from __future__ import annotations

import typing as t
from dataclasses import dataclass

from . import conditions
from .constants import AVRegions, AP_ID_BASE
from .types import AccessRule


@dataclass
class AVLocationData:
    id: int
    name: str
    region_name: str
    access_rule: AccessRule


# Start Region, Destination Region, Access Rule, Bidirectional
# NOTE: several regions are bidirectional=False if they are dead-ends without spawns to avoid creating an unnecessary entrance
entrance_data: t.Tuple[t.Tuple[str, str, AccessRule, bool]] = (
    (AVRegions.WEST_ERIBU, AVRegions.UPPER_ERIBU, conditions.can_damage, True),
    (AVRegions.WEST_ERIBU, AVRegions.DINGER_GISBAR, conditions.dingergisbar_access, False),
    (AVRegions.WEST_ERIBU, AVRegions.LABORATORY, conditions.can_displacement_warp, False),
    (AVRegions.DINGER_GISBAR, AVRegions.BLURST, conditions.always_accessible, False),
    (AVRegions.UPPER_ERIBU, AVRegions.XEDUR, conditions.xedur_access, False),
    (AVRegions.UPPER_ERIBU, AVRegions.LABORATORY, conditions.laboratory_access, False),
    (AVRegions.UPPER_ERIBU, AVRegions.LOWER_ERIBU, conditions.can_drill, True),
    (AVRegions.UPPER_ERIBU, AVRegions.LOWER_ERIBU, conditions.floor_grapple_clip, False, "Eribu Grapple Clip Exit"),
    (AVRegions.LOWER_ERIBU, AVRegions.WEST_UKKIN_NA, lambda s, c: conditions.has_glitch_2(s, c) or conditions.any_coat(s, c), True),
    (
        AVRegions.LOWER_ERIBU,
        AVRegions.ERIBU_INDI,
        lambda s, c: conditions.has_drone_tele(s, c) or conditions.has_trenchcoat(s, c) or conditions.has_grapple(s, c),
        False,
    ),
    (
        AVRegions.ERIBU_INDI,
        AVRegions.LOWER_ERIBU,
        lambda s, c: conditions.has_drone_tele(s, c) or conditions.has_trenchcoat(s, c) or conditions.has_grapple(s, c) or conditions.has_high_jump(s, c),
        False,
    ),
    (AVRegions.ERIBU_INDI, AVRegions.INDI, conditions.always_accessible, True),
    (AVRegions.LOWER_ERIBU, AVRegions.WEST_ABSU, conditions.always_accessible, True),
    (AVRegions.WEST_ABSU, AVRegions.WEST_ATTIC, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.can_drill(s, c), True),
    (AVRegions.WEST_ABSU, AVRegions.ELSENOVA, conditions.can_drill, True),
    (AVRegions.WEST_ABSU, AVRegions.ELSENOVA, lambda s, c: conditions.has_strict_trenchcoat(s, c) and conditions.roof_grapple_clip(s, c), False, "Elsenova Roof Grapple Entrance"),
    (AVRegions.WEST_ABSU, AVRegions.ABSU_BASEMENT, conditions.basement_regular_access, False),
    (
        AVRegions.WEST_ABSU,
        AVRegions.LOWER_ABSU,
        lambda s, c: conditions.can_pierce_wall(s, c) or conditions.any_coat(s, c),
        False,
    ),
    (
        AVRegions.LOWER_ABSU,
        AVRegions.WEST_ABSU,
        lambda s, c: conditions.can_damage(s, c) or conditions.any_coat(s, c),
        False,
    ),
    (AVRegions.WEST_ATTIC, AVRegions.EAST_ATTIC, conditions.attic_transition_upper, True),
    (AVRegions.WEST_ATTIC, AVRegions.ELSENOVA, conditions.can_drill, True),
    (
        AVRegions.ELSENOVA,
        AVRegions.LOWER_ABSU,
        lambda s, c: conditions.can_pierce_wall(s, c) or conditions.any_coat(s, c),
        False,
    ),
    (AVRegions.EAST_ATTIC, AVRegions.ELSENOVA, conditions.has_glitch_2, False),
    (AVRegions.ELSENOVA, AVRegions.EAST_ATTIC, conditions.elsenova_east_attic_access, False),
    (
        AVRegions.LOWER_ABSU,
        AVRegions.ELSENOVA,
        lambda s, c: conditions.can_damage(s, c) or conditions.any_coat(s, c),
        False,
    ),
    (AVRegions.LOWER_ABSU, AVRegions.ABSU_BASEMENT, conditions.floor_grapple_clip, False, "Basement Floor Grapple Clip"),
    (
        AVRegions.LOWER_ABSU,
        AVRegions.ABSU_BASEMENT,
        lambda s, c: conditions.can_displacement_warp(s, c) and conditions.has_red_coat(s, c),
        False,
        "Basement Displacement Warp",
    ),
    (AVRegions.LOWER_ABSU, AVRegions.TELAL, conditions.can_damage_boss, False),
    (AVRegions.LOWER_ABSU, AVRegions.EAST_ABSU, conditions.not_implemented, False),
    (AVRegions.LOWER_ABSU, AVRegions.EAST_ABSU_LEDGE, conditions.has_drone_launch, False),
    (AVRegions.EAST_ABSU, AVRegions.LOWER_ABSU, conditions.always_accessible, False),
    (AVRegions.EAST_ABSU, AVRegions.TELAL, conditions.any_height, False), # Verify
    (AVRegions.EAST_ABSU, AVRegions.EAST_ABSU_LEDGE, conditions.always_accessible, False),
    (AVRegions.EAST_ABSU, AVRegions.ABSU_ZI_ENTRANCE, conditions.always_accessible, True),
    (AVRegions.ABSU_ZI_ENTRANCE, AVRegions.LOWER_ZI, conditions.always_accessible, False),
    (AVRegions.LOWER_ZI, AVRegions.ABSU_ZI_ENTRANCE, conditions.not_implemented, False),
    (AVRegions.LOWER_ZI, AVRegions.UPPER_ZI, conditions.has_high_jump, False),  # TODO: Update
    (AVRegions.LOWER_ZI, AVRegions.EAST_ZI, conditions.lower_east_zi_access, True),
    (AVRegions.UPPER_ZI, AVRegions.LOWER_ZI, conditions.always_accessible, False),
    (AVRegions.LOWER_ZI, AVRegions.LOWER_KUR, conditions.always_accessible, True),
    (AVRegions.LOWER_KUR, AVRegions.INDI, conditions.not_implemented, False),
    (AVRegions.LOWER_KUR, AVRegions.UPPER_KUR, conditions.any_coat, True),
    (AVRegions.INDI, AVRegions.LOWER_KUR, conditions.not_implemented, False),
    (AVRegions.INDI, AVRegions.LOWER_EDIN, conditions.has_trenchcoat, True),
    (AVRegions.INDI, AVRegions.BLURST, conditions.always_accessible, False),
    (AVRegions.LOWER_EDIN, AVRegions.UPPER_EDIN, lambda s, c: conditions.has_glitch_bomb(s, c) or conditions.has_trenchcoat(s, c), True),
)


raw_location_data: t.Tuple[str, str, AccessRule] = (
    ('Eribu - West of Spawn', AVRegions.WEST_ERIBU, conditions.always_accessible),
    ('Eribu - Wheelchair Room', AVRegions.WEST_ERIBU, lambda s, c: conditions.can_displacement_warp(s, c) or conditions.has_drone_tele(s, c)),
    ('Eribu - West Caves Below Pool', AVRegions.WEST_ERIBU, conditions.west_caves_pool_access),

    ('Eribu - FlameThrower', AVRegions.DINGER_GISBAR, conditions.always_accessible),

    ('Eribu - Upper Right', AVRegions.UPPER_ERIBU, conditions.always_accessible),
    ('Eribu - Upper Eribu Bomb Check', AVRegions.UPPER_ERIBU, conditions.upper_eribu_bomb_access),
    ('Eribu - Bubble Jail', AVRegions.UPPER_ERIBU, conditions.bubble_jail_access),
    ('Eribu - Outside Laboratory', AVRegions.UPPER_ERIBU, conditions.outside_lab_access),

    ('Eribu - Xedur Reward', AVRegions.XEDUR, conditions.can_damage_boss),
    ('Eribu - Below Xedur', AVRegions.XEDUR, conditions.can_drill),

    ('Eribu - Laboratory Gauntlet', AVRegions.LABORATORY, conditions.always_accessible),

    (
        'Eribu - Sentry Bot Tunnel',
        AVRegions.LOWER_ERIBU,
        lambda s, c: conditions.has_drone(s, c) and (c.floor_grapple_clip_enabled or conditions.has_glitch_bomb(s, c)),
    ),
    (
        'Eribu - Outside Passcode Room',
        AVRegions.LOWER_ERIBU,
        lambda s, c: conditions.any_glitch(s, c) and conditions.can_damage(s, c) or conditions.has_drone(s, c) or conditions.has_grapple(s, c) or conditions.has_trenchcoat(s, c),
    ),
    ('Eribu - Passcode Room', AVRegions.LOWER_ERIBU, conditions.dalkhu_subtum_access),
    ('Eribu - Path to Absu', AVRegions.LOWER_ERIBU, conditions.always_accessible),

    (
        'Eribu - Path to Indi Ceiling',
        AVRegions.ERIBU_INDI,
        lambda s, c: (
            conditions.has_red_coat(s, c) and (conditions.has_grapple(s, c) or conditions.has_high_jump(s, c))
            or conditions.has_drone_tele(s, c) and conditions.any_coat(s, c)
        )
    ),

    ('Absu - Main Room Rock Shaft', AVRegions.WEST_ABSU, conditions.can_drill),
    (
        'Absu - Diatom Room',
        AVRegions.WEST_ABSU,
        lambda s, c: conditions.has_red_coat(s, c) or conditions.any_glitch(s, c) and (conditions.any_coat(s, c) or conditions.can_pierce_wall(s, c)),
    ),
    ('Absu - Skeleton Tunnel', AVRegions.WEST_ABSU, conditions.has_drone),
    ('Absu - Below Skeleton Tunnel', AVRegions.WEST_ABSU, lambda s, c: conditions.has_drone_tele(s, c) and conditions.has_trenchcoat(s, c)),
    ('Absu - Behind Glitch Barrier', AVRegions.WEST_ABSU, conditions.not_implemented),

    ('Absu - Switch Cage', AVRegions.WEST_ATTIC, lambda s, c: conditions.can_pierce_wall(s, c) or conditions.any_coat(s, c)),
    ('Absu - Attic Far Left', AVRegions.WEST_ATTIC, conditions.basic_attic_access),
    ('Absu - Attic Middle Left', AVRegions.WEST_ATTIC, conditions.attic_transition_upper),

    ('Absu - Attic Midddle Right', AVRegions.EAST_ATTIC, conditions.basic_attic_access),
    ('Absu - Attic Far Right', AVRegions.EAST_ATTIC, conditions.attic_far_right_access),

    ('Absu - Elsenova', AVRegions.ELSENOVA, conditions.always_accessible),

    ('Absu - Below Zombie Jail', AVRegions.ABSU_BASEMENT, conditions.always_accessible),

    ('Absu - Zombie Jail', AVRegions.LOWER_ABSU, lambda s, c: conditions.any_coat(s, c) or conditions.floor_grapple_clip(s, c)),
    ('Absu - Lowest Point', AVRegions.LOWER_ABSU, lambda s, c: conditions.any_coat(s, c) or conditions.floor_grapple_clip(s, c)),
    ('Absu - Floating Platform', AVRegions.LOWER_ABSU, conditions.floating_platform_access),
    ('Absu - Zombie Tunnel', AVRegions.LOWER_ABSU, conditions.zombie_tunnel_access),

    ('Absu - Telal Reward', AVRegions.TELAL, conditions.always_accessible),

    ('Absu - Trapped Diatoms', AVRegions.EAST_ABSU_LEDGE, lambda s, c: conditions.can_drill(s, c) or conditions.any_glitch(s, c)),

    ('Absu - Vertical Shaft Behind Telal', AVRegions.EAST_ABSU, conditions.always_accessible),
    ('Absu - Wall Alcove', AVRegions.EAST_ABSU, conditions.can_drill),
    ('Absu - Hidden Shrine', AVRegions.EAST_ABSU, lambda s, c: conditions.any_coat(s, c) or conditions.has_drone(s, c) or conditions.easy_grapple_clip(s, c)),
    ('Absu - Chasm Room Tunnel', AVRegions.EAST_ABSU, lambda s, c: conditions.has_red_coat(s, c) or conditions.has_drone(s, c)),
    ('Absu - Gated Alcove', AVRegions.EAST_ABSU, conditions.gated_alcove_access),
    ('Absu - Purple Shrine', AVRegions.EAST_ABSU, lambda s, c: conditions.has_red_coat(s, c) or conditions.has_glitch_2(s, c) and conditions.can_drill(s, c)),
    ('Absu - Zi Entrance', AVRegions.EAST_ABSU, conditions.can_drill),

    ('Zi - Behind False Wall', AVRegions.LOWER_ZI, lambda s, c: conditions.any_coat(s, c) and conditions.any_height(s, c)),
    ('Zi - Disappointment Hill', AVRegions.LOWER_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone_tele(s, c) or conditions.has_high_jump(s, c)),
    (
        'Zi - Secret Room near lower Save',
        AVRegions.LOWER_ZI,
        lambda s, c: conditions.can_drill and (conditions.has_trenchcoat(s, c) or conditions.has_drone_tele(s, c) or conditions.has_high_jump(s, c)),
    ),
    ('Zi - Roof Alcove', AVRegions.LOWER_ZI, conditions.not_implemented),

    ('Zi - Above Veruska', AVRegions.EAST_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone(s, c)),
    ('Zi - Behind Veruska Left', AVRegions.EAST_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone(s, c)),
    ('Zi - Behind Veruska Right', AVRegions.EAST_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone(s, c)),

    ('Zi - Ceiling Alcove Below Uruku', AVRegions.UPPER_ZI, lambda s, c: conditions.has_red_coat(s, c) or conditions.has_drone(s, c) or conditions.can_drill(s, c) and conditions.any_height(s, c)),
    ('Zi - Drone Tunnel Upper', AVRegions.UPPER_ZI, lambda s, c: conditions.has_drone(s, c) and conditions.has_power_nodes(s, c, 2)),
    ('Zi - Drone Tunnel End', AVRegions.UPPER_ZI, lambda s, c: conditions.has_drone(s, c) and conditions.has_power_nodes(s, c, 2)),
    ('Zi - Uruku Room', AVRegions.UPPER_ZI, conditions.any_coat),

    ('Kur - High Jump Shrine', AVRegions.LOWER_KUR, conditions.always_accessible),
    ('Kur - High Jump Shrine False Wall', AVRegions.LOWER_KUR, conditions.not_implemented),

    ('Kur - Near Indi Entrance', AVRegions.UPPER_KUR, conditions.always_accessible),
    ('Kur - Inside Cliff', AVRegions.UPPER_KUR, conditions.has_red_coat),

    ('Indi - Path to Eribu', AVRegions.INDI, conditions.has_drone),
    ('Indi - Outside Save Room', AVRegions.INDI, conditions.has_trenchcoat),

    ('Ukkin-Na - Long Fall Shaft Base', AVRegions.WEST_UKKIN_NA, conditions.not_implemented),
    ('Ukkin-Na - Annihiwaiter Room', AVRegions.WEST_UKKIN_NA, conditions.not_implemented),

    ('Edin - Central Structure Behind Glitch', AVRegions.LOWER_EDIN, conditions.has_glitch_bomb),

    ('Edin - False Wall Shrine', AVRegions.UPPER_EDIN, conditions.always_accessible),
    ('Edin - Upper Drone Tunnel', AVRegions.UPPER_EDIN, lambda s, c: conditions.has_drone_tele(s, c) and conditions.has_trenchcoat(s, c)),

    ('Glitch a Blurst', AVRegions.BLURST, conditions.any_glitch),
)


location_data: t.Tuple[AVLocationData] = tuple(
    AVLocationData(id, name, region_name, access_rule)
    for id, (name, region_name, access_rule) in enumerate(raw_location_data, AP_ID_BASE)
)


LOCATION_NAME_TO_ID: t.Dict[str, int] = {
    data.name: data.id for data in location_data
}
