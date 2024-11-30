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

    def __post_init__(self):
        self.id += AP_ID_BASE


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
    (AVRegions.LOWER_ERIBU, AVRegions.WEST_UKKIN_NA, lambda s, c: conditions.has_glitch_2(s, c) or conditions.any_coat(s, c), True),  # TODO Revisit
    (
        AVRegions.LOWER_ERIBU,
        AVRegions.ERIBU_INDI,
        lambda s, c: conditions.has_drone_tele(s, c) or conditions.has_trenchcoat(s, c) or conditions.has_grapple(s, c),
        False,
    ),
    (AVRegions.ERIBU_INDI, AVRegions.LOWER_ERIBU, conditions.any_height, False),
    (AVRegions.ERIBU_INDI, AVRegions.WEST_INDI, conditions.always_accessible, True),
    (AVRegions.LOWER_ERIBU, AVRegions.WEST_ABSU, conditions.always_accessible, True),
    (AVRegions.WEST_ABSU, AVRegions.WEST_ATTIC, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.can_drill(s, c), True),
    (AVRegions.WEST_ABSU, AVRegions.ELSENOVA, conditions.can_drill, True),
    (AVRegions.WEST_ABSU, AVRegions.ELSENOVA, lambda s, c: conditions.has_strict_trenchcoat(s, c) and conditions.roof_grapple_clip(s, c), False, "Elsenova Roof Grapple Entrance"),
    (AVRegions.WEST_ABSU, AVRegions.ABSU_BASEMENT, conditions.basement_regular_access, False),
    (
        AVRegions.WEST_ABSU,
        AVRegions.LOWER_ABSU,
        lambda s, c: conditions.can_pierce_wall(s, c) or conditions.any_coat(s, c) or conditions.easy_grapple_clip(s, c),
        False,
    ),
    (
        AVRegions.LOWER_ABSU,
        AVRegions.WEST_ABSU,
        lambda s, c: conditions.can_damage(s, c) or conditions.any_coat(s, c),
        False,
    ),
    (AVRegions.WEST_ATTIC, AVRegions.EAST_ATTIC, conditions.attic_transition_upper, True),
    (AVRegions.WEST_ATTIC, AVRegions.EAST_ATTIC, lambda s, c: conditions.can_drill(s, c) and conditions.has_glitch_2(s, c), False, "West to East Attic Default"),
    (AVRegions.EAST_ATTIC, AVRegions.WEST_ATTIC, lambda s, c: conditions.can_drill(s, c) and conditions.has_glitch_2(s, c), False, "East to West Attic Default"),
    (AVRegions.WEST_ATTIC, AVRegions.ELSENOVA, conditions.can_drill, False),
    (AVRegions.ELSENOVA, AVRegions.WEST_ATTIC, conditions.elsenova_west_attic_access, False),
    (AVRegions.EAST_ATTIC, AVRegions.ELSENOVA, conditions.has_glitch_2, True),
    (
        AVRegions.ELSENOVA,
        AVRegions.LOWER_ABSU,
        lambda s, c: conditions.can_pierce_wall(s, c) or conditions.any_coat(s, c) or conditions.easy_grapple_clip(s, c),
        False,
    ),
    (
        AVRegions.LOWER_ABSU,
        AVRegions.ELSENOVA,
        lambda s, c: conditions.can_damage(s, c) or conditions.any_coat(s, c),
        False,
    ),
    (
        AVRegions.LOWER_ABSU,
        AVRegions.ABSU_BASEMENT,
        lambda s, c: conditions.can_displacement_warp(s, c) and conditions.has_red_coat(s, c) or conditions.floor_grapple_clip,
        False,
    ),
    (AVRegions.LOWER_ABSU, AVRegions.TELAL, lambda s, c: conditions.can_damage_boss(s, c) or conditions.any_coat(s, c), False),
    (AVRegions.LOWER_ABSU, AVRegions.LOWER_CORRIDOR, lambda s, c: conditions.can_drill(s, c) or conditions.has_trenchcoat(s, c), True),
    (AVRegions.LOWER_CORRIDOR, AVRegions.EAST_ABSU, conditions.lower_east_absu_access, False),
    (AVRegions.LOWER_CORRIDOR, AVRegions.EAST_ABSU_DRONE, conditions.has_drone_launch, False),
    (AVRegions.TELAL, AVRegions.EAST_ABSU, conditions.telal_east_absu_access, False),
    (AVRegions.TELAL, AVRegions.EAST_ABSU_DRONE, conditions.has_drone_launch, False),
    (AVRegions.EAST_ABSU, AVRegions.EAST_ABSU_DRONE, conditions.has_drone, False),
    (AVRegions.EAST_ABSU, AVRegions.LOWER_CORRIDOR, lambda s, c: conditions.can_drill(s, c) or conditions.has_trenchcoat(s, c) or conditions.any_glitch(s, c), False),
    (AVRegions.EAST_ABSU, AVRegions.TELAL, conditions.any_height, False),
    (AVRegions.EAST_ABSU, AVRegions.INDI_TUNNEL, conditions.east_absu_indi_tunnel_access, False),
    (AVRegions.INDI_TUNNEL, AVRegions.EAST_ABSU, lambda s, c: conditions.hard_grapple_clip(s, c) or conditions.any_coat(s, c), False),
    (AVRegions.INDI_TUNNEL, AVRegions.INDI, conditions.non_grapple_height, False),
    (AVRegions.EAST_ABSU, AVRegions.ABSU_ZI, conditions.always_accessible, True),

    (AVRegions.ABSU_ZI, AVRegions.LOWER_ZI, conditions.always_accessible, False),
    (AVRegions.LOWER_ZI, AVRegions.ABSU_ZI, conditions.zi_vanilla_exit, False),
    (AVRegions.LOWER_ZI, AVRegions.UPPER_ZI, conditions.non_grapple_height, False),
    (AVRegions.UPPER_ZI, AVRegions.LOWER_ZI, conditions.always_accessible, False),
    (AVRegions.LOWER_ZI, AVRegions.EAST_ZI, conditions.lower_east_zi_access, True),
    (AVRegions.UPPER_ZI, AVRegions.EAST_ZI, conditions.always_accessible, False),
    (AVRegions.EAST_ZI, AVRegions.UPPER_ZI, conditions.any_height, False),
    (AVRegions.EAST_ZI, AVRegions.PREVIEW_ROOM, lambda s, c: conditions.any_coat(s, c) and conditions.any_height(s, c), False),
    (AVRegions.EAST_ZI, AVRegions.LOWER_CAVES, conditions.always_accessible, True),
    (AVRegions.UPPER_ZI, AVRegions.PREVIEW_ROOM, conditions.floor_grapple_clip, False),
    (AVRegions.UPPER_ZI, AVRegions.URUKU, conditions.non_grapple_height, False),
    (AVRegions.UPPER_ZI, AVRegions.ZI_INDI, conditions.non_jump_height, False),
    (AVRegions.ZI_INDI, AVRegions.UPPER_ZI, conditions.any_height, False),
    (AVRegions.ZI_INDI, AVRegions.URUKU, conditions.any_height, False),
    (AVRegions.ZI_INDI, AVRegions.INDI, conditions.always_accessible, True),

    (AVRegions.LOWER_CAVES, AVRegions.GAUNTLET_ROOM, conditions.kur_gauntlet_access, False),
    (AVRegions.GAUNTLET_ROOM, AVRegions.GAUNTLET_REWARD, conditions.not_implemented, False),
    (AVRegions.LOWER_CAVES, AVRegions.GAUNTLET_REWARD, lambda s, c: conditions.has_fat_beam(s, c) and conditions.has_trenchcoat(s, c), False),
    (AVRegions.LOWER_CAVES, AVRegions.KUR_INDI, lambda s, c: conditions.any_coat(s, c) or conditions.easy_grapple_clip(s, c), False),
    (AVRegions.KUR_INDI, AVRegions.LOWER_CAVES, lambda s, c: conditions.any_coat(s, c) or conditions.floor_grapple_clip(s, c), False),
    (AVRegions.UPPER_CAVES, AVRegions.KUR_INDI, lambda s, c: conditions.any_coat(s, c) or conditions.floor_grapple_clip(s, c), False),
    (AVRegions.KUR_INDI, AVRegions.UPPER_CAVES, conditions.indi_upper_caves_access, False),
    (AVRegions.UPPER_CAVES, AVRegions.KUR_EDIN, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_glitch_2(s, c), True),
    (AVRegions.KUR_EDIN, AVRegions.EAST_EDIN, conditions.always_accessible, True),
    (AVRegions.UPPER_CAVES, AVRegions.MOUNTAIN_BASE, conditions.caves_to_base_access, False),
    (AVRegions.MOUNTAIN_BASE, AVRegions.UPPER_CAVES, conditions.always_accessible, False),
    (AVRegions.MOUNTAIN_BASE, AVRegions.LOWER_GIR_TAB, conditions.lower_gir_tab_access, False),
    (AVRegions.LOWER_GIR_TAB, AVRegions.MOUNTAIN_BASE, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_glitch_2(s, c), False),
    # KUR_INDI to EAST_INDI
    (AVRegions.WEST_INDI, AVRegions.INDI, conditions.any_height, False),
    (AVRegions.INDI, AVRegions.WEST_INDI, conditions.always_accessible, False),
    (AVRegions.INDI, AVRegions.INDI_TUNNEL, conditions.always_accessible, False),
    # (AVRegions.INDI, AVRegions.LOWER_KUR, conditions.any_coat, False),
    (AVRegions.INDI, AVRegions.LOWER_EDIN, conditions.has_trenchcoat, True),
    (AVRegions.INDI, AVRegions.BLURST, conditions.always_accessible, False),

    # Microregions (Separated for sanity)
    (AVRegions.EAST_ABSU, AVRegions.EA_LEDGE, lambda s, c: conditions.can_drill(s, c) or conditions.any_glitch(s, c), False),
    (AVRegions.EAST_ABSU_DRONE, AVRegions.EA_LEDGE, conditions.always_accessible, False),
    (AVRegions.EAST_ABSU, AVRegions.EA_BEHIND_TELAL, conditions.always_accessible, False),
    (AVRegions.EAST_ABSU_DRONE, AVRegions.EA_BEHIND_TELAL, conditions.always_accessible, False),
    (AVRegions.EAST_ABSU, AVRegions.EA_ALCOVE, conditions.can_drill, False),
    (AVRegions.EAST_ABSU_DRONE, AVRegions.EA_ALCOVE, conditions.always_accessible, False),
    (AVRegions.EAST_ABSU, AVRegions.EA_HIDDEN_SHRINE, lambda s, c: conditions.easy_grapple_clip(s, c) or conditions.any_coat(s, c) and conditions.any_height(s, c), False),
    (AVRegions.EAST_ABSU_DRONE, AVRegions.EA_HIDDEN_SHRINE, conditions.always_accessible, False),
    (AVRegions.EAST_ABSU, AVRegions.EA_CHASM_TUNNEL, conditions.has_red_coat, False),
    (AVRegions.EAST_ABSU_DRONE, AVRegions.EA_CHASM_TUNNEL, conditions.always_accessible, False),
    (AVRegions.EAST_ABSU, AVRegions.EA_ZI_ENTRANCE, conditions.can_drill, False),
    (AVRegions.EAST_ABSU_DRONE, AVRegions.EA_ZI_ENTRANCE, conditions.always_accessible, False),

    # WIP
    (AVRegions.LOWER_GIR_TAB, AVRegions.BEHIND_GIR_TAB, conditions.not_implemented, False),
    (AVRegions.BEHIND_GIR_TAB, AVRegions.UPPER_GIR_TAB, conditions.not_implemented, False),
    (AVRegions.WEST_UKKIN_NA, AVRegions.EAST_UKKIN_NA, conditions.not_implemented, True),
    (AVRegions.EAST_UKKIN_NA, AVRegions.UKKIN_NA_EAST_EXIT, conditions.has_trenchcoat, False),
    (AVRegions.EAST_UKKIN_NA, AVRegions.BLURST, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.easy_grapple_clip(s, c), False),
    (AVRegions.UKKIN_NA_EAST_EXIT, AVRegions.EAST_UKKIN_NA, conditions.any_coat, False),
    (AVRegions.UKKIN_NA_EAST_EXIT, AVRegions.LOWER_EDIN, conditions.always_accessible, True),
    (AVRegions.LOWER_EDIN, AVRegions.UPPER_EDIN, lambda s, c: conditions.has_glitch_bomb(s, c) or conditions.has_trenchcoat(s, c), True),
    (AVRegions.LOWER_EDIN, AVRegions.EAST_EDIN, conditions.not_implemented, True),
    (AVRegions.EAST_EDIN, AVRegions.UPPER_CAVES, conditions.not_implemented, True),

    (AVRegions.UPPER_CAVES, AVRegions.UPPER_E_KUR_MAH, conditions.not_implemented, True),
    (AVRegions.LOWER_E_KUR_MAH, AVRegions.UPPER_E_KUR_MAH, conditions.not_implemented, True),

    (AVRegions.UPPER_E_KUR_MAH, AVRegions.MAR_URU, conditions.mar_uru_access, True),
)


location_data: t.Tuple[AVLocationData] = (
    AVLocationData(0, 'Eribu - West of Spawn', AVRegions.WEST_ERIBU, conditions.always_accessible),
    AVLocationData(1, 'Eribu - Wheelchair Room', AVRegions.WEST_ERIBU, lambda s, c: conditions.can_displacement_warp(s, c) or conditions.has_drone_tele(s, c)),
    AVLocationData(2, 'Eribu - West Caves Below Pool', AVRegions.WEST_ERIBU, conditions.west_caves_pool_access),

    AVLocationData(3, 'Eribu - FlameThrower', AVRegions.DINGER_GISBAR, conditions.always_accessible),

    AVLocationData(4, 'Eribu - Upper Right', AVRegions.UPPER_ERIBU, conditions.always_accessible),
    AVLocationData(5, 'Eribu - Upper Eribu Bomb Check', AVRegions.UPPER_ERIBU, conditions.upper_eribu_bomb_access),
    AVLocationData(6, 'Eribu - Bubble Jail', AVRegions.UPPER_ERIBU, conditions.bubble_jail_access),
    AVLocationData(7, 'Eribu - Outside Laboratory', AVRegions.UPPER_ERIBU, conditions.outside_lab_access),

    AVLocationData(8, 'Eribu - Xedur Reward', AVRegions.XEDUR, conditions.can_damage_boss),
    AVLocationData(9, 'Eribu - Below Xedur', AVRegions.XEDUR, conditions.can_drill),

    AVLocationData(10, 'Eribu - Laboratory Gauntlet', AVRegions.LABORATORY, conditions.always_accessible),

    AVLocationData(
        11,
        'Eribu - Sentry Bot Tunnel',
        AVRegions.LOWER_ERIBU,
        lambda s, c: conditions.has_drone(s, c) and (c.floor_grapple_clip_enabled or conditions.has_glitch_bomb(s, c)),
    ),
    AVLocationData(
        12,
        'Eribu - Outside Passcode Room',
        AVRegions.LOWER_ERIBU,
        lambda s, c: conditions.any_glitch(s, c) and conditions.can_damage(s, c) or conditions.has_drone(s, c) or conditions.has_grapple(s, c) or conditions.has_trenchcoat(s, c),
    ),
    AVLocationData(13, 'Eribu - Passcode Room', AVRegions.LOWER_ERIBU, conditions.dalkhu_subtum_access),
    AVLocationData(14, 'Eribu - Path to Absu', AVRegions.LOWER_ERIBU, conditions.always_accessible),

    AVLocationData(
        15,
        'Eribu - Path to Indi Ceiling',
        AVRegions.ERIBU_INDI,
        lambda s, c: (
            conditions.has_red_coat(s, c) and (conditions.has_grapple(s, c) or conditions.has_high_jump(s, c))
            or conditions.has_drone_tele(s, c) and conditions.any_coat(s, c)
        )
    ),

    AVLocationData(16, 'Absu - Main Room Rock Shaft', AVRegions.WEST_ABSU, conditions.can_drill),
    AVLocationData(
        17,
        'Absu - Diatom Room',
        AVRegions.WEST_ABSU,
        lambda s, c: conditions.has_red_coat(s, c) or conditions.any_glitch(s, c) and (conditions.any_coat(s, c) or conditions.can_pierce_wall(s, c)),
    ),
    AVLocationData(18, 'Absu - Skeleton Tunnel', AVRegions.WEST_ABSU, conditions.has_drone),
    AVLocationData(19, 'Absu - Below Skeleton Tunnel', AVRegions.WEST_ABSU, lambda s, c: conditions.has_drone_tele(s, c) and conditions.has_trenchcoat(s, c)),

    AVLocationData(20, 'Absu - Switch Cage', AVRegions.WEST_ATTIC, lambda s, c: conditions.can_pierce_wall(s, c) or conditions.any_coat(s, c)),
    AVLocationData(21, 'Absu - Attic Far Left', AVRegions.WEST_ATTIC, conditions.basic_attic_access),
    AVLocationData(22, 'Absu - Attic Middle Left', AVRegions.WEST_ATTIC, conditions.attic_transition_upper),

    AVLocationData(23, 'Absu - Attic Midddle Right', AVRegions.EAST_ATTIC, conditions.basic_attic_access),
    AVLocationData(24, 'Absu - Attic Far Right', AVRegions.EAST_ATTIC, conditions.attic_far_right_access),

    AVLocationData(25, 'Absu - Elsenova', AVRegions.ELSENOVA, conditions.always_accessible),

    AVLocationData(26, 'Absu - Behind Glitch Barrier', AVRegions.ABSU_BASEMENT, conditions.always_accessible),

    AVLocationData(27, 'Absu - Zombie Jail', AVRegions.LOWER_ABSU, lambda s, c: conditions.any_coat(s, c) or conditions.floor_grapple_clip(s, c)),
    AVLocationData(28, 'Absu - Lowest Point', AVRegions.LOWER_ABSU, lambda s, c: conditions.any_coat(s, c) or conditions.floor_grapple_clip(s, c)),

    AVLocationData(29, 'Absu - Floating Platform', AVRegions.LOWER_CORRIDOR, conditions.floating_platform_access),

    AVLocationData(31, 'Absu - Telal Reward', AVRegions.TELAL, conditions.always_accessible),

    AVLocationData(32, 'Absu - Indi Tunnel Side Room', AVRegions.INDI_TUNNEL, conditions.any_height),

    AVLocationData(33, 'Absu - Trapped Diatoms', AVRegions.EA_LEDGE, conditions.always_accessible),
    AVLocationData(30, 'Absu - Zombie Tunnel', AVRegions.EAST_ABSU, conditions.zombie_tunnel_access),
    AVLocationData(34, 'Absu - Vertical Shaft Behind Telal', AVRegions.EA_BEHIND_TELAL, conditions.always_accessible),
    AVLocationData(35, 'Absu - Wall Alcove', AVRegions.EA_ALCOVE, conditions.always_accessible),
    AVLocationData(36, 'Absu - Hidden Shrine', AVRegions.EA_HIDDEN_SHRINE, conditions.always_accessible),
    AVLocationData(37, 'Absu - Chasm Room Tunnel', AVRegions.EA_CHASM_TUNNEL, conditions.always_accessible),
    AVLocationData(38, 'Absu - Gated Alcove', AVRegions.EAST_ABSU, conditions.gated_alcove_access),
    AVLocationData(39, 'Absu - Purple Shrine', AVRegions.EAST_ABSU, lambda s, c: conditions.has_red_coat(s, c) or conditions.has_glitch_2(s, c) and conditions.can_drill(s, c)),
    AVLocationData(40, 'Absu - Zi Entrance', AVRegions.EA_ZI_ENTRANCE, conditions.always_accessible),

    AVLocationData(41, 'Zi - Behind False Wall', AVRegions.LOWER_ZI, lambda s, c: conditions.any_coat(s, c) and conditions.any_height(s, c)),
    AVLocationData(42, 'Zi - Disappointment Hill', AVRegions.LOWER_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone_tele(s, c) or conditions.has_high_jump(s, c)),
    AVLocationData(
        43,
        'Zi - Secret Room near lower Save',
        AVRegions.LOWER_ZI,
        lambda s, c: conditions.can_drill(s, c) and (conditions.has_trenchcoat(s, c) or conditions.has_drone_tele(s, c) or conditions.has_high_jump(s, c)),
    ),
    AVLocationData(44, 'Zi - Furglot Tunnel', AVRegions.LOWER_ZI, conditions.furglot_tunnel_access),
    AVLocationData(45, 'Zi - False Roof Alcove', AVRegions.LOWER_ZI, conditions.zi_false_roof_access),

    AVLocationData(46, 'Zi - Above Veruska', AVRegions.EAST_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone(s, c)),
    AVLocationData(47, 'Zi - Behind Veruska Left', AVRegions.EAST_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone(s, c)),
    AVLocationData(48, 'Zi - Behind Veruska Right', AVRegions.EAST_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone(s, c)),

    AVLocationData(49, 'Zi - Ceiling Alcove Below Uruku', AVRegions.UPPER_ZI, lambda s, c: conditions.has_red_coat(s, c) or conditions.has_drone(s, c) or conditions.can_drill(s, c) and conditions.any_height(s, c)),
    AVLocationData(50, 'Zi - Drone Tunnel Upper', AVRegions.UPPER_ZI, lambda s, c: conditions.has_drone(s, c) and conditions.has_power_nodes(s, c, 2)),
    AVLocationData(51, 'Zi - Drone Tunnel End', AVRegions.UPPER_ZI, lambda s, c: conditions.has_drone(s, c) and conditions.has_power_nodes(s, c, 2)),

    AVLocationData(52, 'Zi - Preview Room', AVRegions.PREVIEW_ROOM, conditions.always_accessible),

    #TODO: Proper Implement Uruku
    AVLocationData(53, 'Zi - Uruku Reward', AVRegions.URUKU, conditions.has_trenchcoat),
    AVLocationData(54, 'Zi - Uruku Cage', AVRegions.URUKU, conditions.any_coat),
    AVLocationData(55, 'Zi - Behind Uruku Rooftop Ledge', AVRegions.URUKU, conditions.has_grapple),

    AVLocationData(56, 'Kur - Drone Tunnel Before Gauntlet', AVRegions.LOWER_CAVES, conditions.has_drone),
    AVLocationData(57, 'Kur - High Jump Shrine', AVRegions.LOWER_CAVES, conditions.always_accessible),
    AVLocationData(58, 'Kur - High Jump Shrine False Wall', AVRegions.LOWER_CAVES, lambda s, c: conditions.has_drone(s, c) or conditions.any_height(s, c)),
    AVLocationData(59, 'Kur - Above Lower Save Room', AVRegions.LOWER_CAVES, conditions.above_lower_kur_save_access),

    AVLocationData(60, 'Kur - Gauntlet Reward', AVRegions.GAUNTLET_REWARD, conditions.always_accessible),

    AVLocationData(61, 'Kur - Near Indi Entrance', AVRegions.UPPER_CAVES, conditions.always_accessible),

    AVLocationData(62, 'Kur - Cliffside Cave Shrine', AVRegions.MOUNTAIN_BASE, lambda s, c: conditions.has_red_coat(s, c) or conditions.has_drone(s, c)),

    AVLocationData(63, 'Kur - Above Twin Save Rooms', AVRegions.UPPER_CAVES, conditions.not_implemented),
    AVLocationData(64, 'Kur - Floating Ledge', AVRegions.UPPER_CAVES, conditions.has_drone),
    AVLocationData(65, 'Kur - Inside Cliff', AVRegions.UPPER_CAVES, conditions.has_red_coat),
    AVLocationData(66, 'Kur - Upper Cliffs Shrine', AVRegions.UPPER_CAVES, conditions.has_drone),
    AVLocationData(67, 'Kur - Drone Odyssey Behind Wall', AVRegions.UPPER_CAVES, conditions.has_drone),
    AVLocationData(68, 'Kur - Drone Odyssey Reward', AVRegions.UPPER_CAVES, conditions.has_drone),
    AVLocationData(69, 'Kur - Snowy Cliffs Ledge Upper', AVRegions.UPPER_CAVES, conditions.not_implemented),
    AVLocationData(70, 'Kur - Snowy Cliffs Ledge Lower', AVRegions.UPPER_CAVES, conditions.has_red_coat),
    AVLocationData(71, 'Kur - Loop Room', AVRegions.UPPER_CAVES, conditions.not_implemented),
    AVLocationData(72, 'Kur - Peak Cliff Ledge', AVRegions.UPPER_CAVES, conditions.not_implemented),

    AVLocationData(73, 'Kur - Gir-Tab Lower Entrance Drone Tunnel', AVRegions.LOWER_GIR_TAB, conditions.has_drone),

    AVLocationData(74, 'Kur - Gir-Tab Upper Entrance', AVRegions.UPPER_GIR_TAB, conditions.always_accessible),

    AVLocationData(75, 'Kur - Internal Cliffs near False Floor', AVRegions.BEHIND_GIR_TAB, conditions.not_implemented),
    AVLocationData(76, 'Kur - Internal Cliffs Shrine', AVRegions.BEHIND_GIR_TAB, conditions.not_implemented),
    AVLocationData(77, 'Kur - Internal Cliffs Above Shrine', AVRegions.BEHIND_GIR_TAB, conditions.not_implemented),

    AVLocationData(78, 'Indi - Path to Eribu', AVRegions.WEST_INDI, conditions.has_drone),

    AVLocationData(79, 'Indi - Outside Save Room', AVRegions.INDI, conditions.has_trenchcoat),

    AVLocationData(80, 'Ukkin-Na - Long Fall Shaft Base', AVRegions.WEST_UKKIN_NA, conditions.any_height),
    AVLocationData(81, 'Ukkin-Na - Annihiwaiter Room', AVRegions.WEST_UKKIN_NA, conditions.not_implemented),

    AVLocationData(82, 'Ukkin-Na - Secret Room Below Floor', AVRegions.EAST_UKKIN_NA, conditions.has_trenchcoat),
    AVLocationData(83, 'Ukkin-Na - Blurst Room', AVRegions.EAST_UKKIN_NA, lambda s, c: conditions.has_trenchcoat(s, c) and conditions.has_drone(s, c)),
    AVLocationData(84, 'Ukkin-Na - Midway Shaft Lower', AVRegions.EAST_UKKIN_NA, conditions.has_trenchcoat),
    AVLocationData(85, 'Ukkin-Na - Midway Shaft Upper', AVRegions.EAST_UKKIN_NA, conditions.not_implemented),
    AVLocationData(86, 'Ukkin-Na - Hidden Shrine', AVRegions.EAST_UKKIN_NA, conditions.ukkin_na_shrine_access),
    AVLocationData(87, 'Ukkin-Na - Chamber Above Vision Room', AVRegions.EAST_UKKIN_NA, conditions.not_implemented),
    AVLocationData(88, 'Ukkin-Na - Tunnel Below Vision Room', AVRegions.EAST_UKKIN_NA, lambda s, c: conditions.has_trenchcoat(s, c) and conditions.has_drone(s, c)),
    AVLocationData(89, 'Ukkin-Na - Outside Ophelia', AVRegions.EAST_UKKIN_NA, conditions.not_implemented),
    AVLocationData(90, 'Ukkin-Na - Above Ophelia Ledge', AVRegions.EAST_UKKIN_NA, conditions.not_implemented),

    AVLocationData(91, 'Edin - Roof Ledge Near Ukkin-Na', AVRegions.LOWER_EDIN, conditions.not_implemented),
    AVLocationData(92, 'Edin - Roof Cage', AVRegions.LOWER_EDIN, conditions.not_implemented),
    AVLocationData(93, 'Edin - Central Structure Behind Glitch', AVRegions.LOWER_EDIN, conditions.has_glitch_bomb),
    AVLocationData(94, 'Edin - Secret Tunnel Below Zombies', AVRegions.LOWER_EDIN, conditions.not_implemented),
    AVLocationData(95, 'Edin - Above Indi Entrace', AVRegions.LOWER_EDIN, conditions.not_implemented),
    AVLocationData(96, 'Edin - Clone Path Inside Blocks', AVRegions.LOWER_EDIN, conditions.not_implemented),
    AVLocationData(97, 'Edin - Clone Path Rooftop Ledge', AVRegions.LOWER_EDIN, conditions.not_implemented),
    AVLocationData(98, 'Edin - Clone Path Roof Before Save', AVRegions.LOWER_EDIN, conditions.not_implemented),

    AVLocationData(99, 'Edin - False Wall Shrine', AVRegions.UPPER_EDIN, conditions.always_accessible),
    AVLocationData(100, 'Edin - Ukhu Path Drone Tunnel', AVRegions.UPPER_EDIN, lambda s, c: conditions.has_drone_tele(s, c) and conditions.has_trenchcoat(s, c)),
    AVLocationData(101, 'Edin - Ukhu Path Side Room', AVRegions.UPPER_EDIN, conditions.not_implemented),
    AVLocationData(102, 'Edin - In Structure Ruins', AVRegions.UPPER_EDIN, conditions.not_implemented),
    AVLocationData(103, 'Edin - Ukhu Reward', AVRegions.UPPER_EDIN, conditions.not_implemented),

    AVLocationData(104, 'Edin - Clone Reward', AVRegions.EAST_EDIN, conditions.not_implemented),
    AVLocationData(105, 'Edin - Double Check Tunnel Left', AVRegions.EAST_EDIN, conditions.not_implemented),
    AVLocationData(106, 'Edin - Double Check Tunnel Right', AVRegions.EAST_EDIN, conditions.not_implemented),

    AVLocationData(107, 'E-Kur-Mah - Entry Chamber Breakable Wall', AVRegions.UPPER_E_KUR_MAH, conditions.not_implemented),
    AVLocationData(108, 'E-Kur-Mah - Key Door on Key Chamber Path', AVRegions.UPPER_E_KUR_MAH, lambda s, c: conditions.has_red_coat(s, c) or conditions.has_sudran_key(s, c)),
    AVLocationData(109, 'E-Kur-Mah - Key Chamber Upper', AVRegions.UPPER_E_KUR_MAH, conditions.not_implemented),
    AVLocationData(110, 'E-Kur-Mah - Key Chamber Lower', AVRegions.UPPER_E_KUR_MAH, conditions.not_implemented),

    AVLocationData(111, 'E-Kur-Mah - Midway Down East Shaft', AVRegions.LOWER_E_KUR_MAH, conditions.has_red_coat),
    AVLocationData(112, 'E-Kur-Mah - Passcode Check', AVRegions.LOWER_E_KUR_MAH, conditions.not_implemented),
    AVLocationData(113, 'E-Kur-Mah - Hidden Drone Tunnel', AVRegions.LOWER_E_KUR_MAH, conditions.not_implemented),
    AVLocationData(114, 'E-Kur-Mah - Area Reward', AVRegions.LOWER_E_KUR_MAH, conditions.not_implemented),
    AVLocationData(115, 'E-Kur-Mah - Lowest Area Inside Wall', AVRegions.LOWER_E_KUR_MAH, conditions.not_implemented),

    AVLocationData(116, 'Mar-Uru - Alcove After Sentinel', AVRegions.MAR_URU, conditions.not_implemented),
    AVLocationData(117, 'Mar-Uru - Sentry Bot Puzzle', AVRegions.MAR_URU, conditions.not_implemented),
    AVLocationData(118, 'Mar-Uru - Below Sentry Bot Puzzle', AVRegions.MAR_URU, conditions.not_implemented),
    AVLocationData(119, 'Mar-Uru - Below Sentry Bot Puzzle In Wall', AVRegions.MAR_URU, conditions.not_implemented),
    AVLocationData(120, 'Mar-Uru - Inside Corridor Block', AVRegions.MAR_URU, conditions.not_implemented),
    AVLocationData(121, 'Mar-Uru - Behind Wall Before Athetos Ascent', AVRegions.MAR_URU, conditions.not_implemented),
    AVLocationData(122, 'Mar-Uru - Tie-Flighter Puzzle', AVRegions.MAR_URU, conditions.has_glitch_2),
    AVLocationData(123, 'Mar-Uru - Athethos Ascent Drone Tunnel', AVRegions.MAR_URU, conditions.has_drone),

    AVLocationData(124, 'Glitch a Blurst', AVRegions.BLURST, conditions.any_glitch),
)


LOCATION_NAME_TO_ID: t.Dict[str, int] = {
    data.name: data.id for data in location_data
}
