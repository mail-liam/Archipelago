from __future__ import annotations

import typing as t
from dataclasses import dataclass

from .logic import conditions
from .constants import AVRegions, AP_ID_BASE

if t.TYPE_CHECKING:
    from BaseClasses import CollectionState


@dataclass
class AVLocationData:
    id: int
    name: str
    region_name: str
    access_rule: t.Callable[[CollectionState, int], bool]


# Start Region, Destination Region, Access Rule, Bidirectional
entrance_data: t.Tuple[t.Tuple[str, str, t.Callable[[CollectionState, int], bool], bool]] = (
    # TODO: Menu region connection to be dynamic with start location rando
    (AVRegions.MENU, AVRegions.WEST_ERIBU, conditions.always_accessible, False),  # True in the purest sense, but it won't ever matter
    (AVRegions.WEST_ERIBU, AVRegions.UPPER_ERIBU, conditions.can_damage, True),
    (AVRegions.UPPER_ERIBU, AVRegions.XEDUR, conditions.can_angle_shoot, False),  # REQUIRES_UPDATE
    (AVRegions.UPPER_ERIBU, AVRegions.LOWER_ERIBU, conditions.can_drill, True),
    (AVRegions.LOWER_ABSU, AVRegions.WEST_UKKIN_NA, lambda s, c: conditions.has_glitch_2(s, c) or conditions.has_any_coat(s, c), True),
    (AVRegions.LOWER_ERIBU, AVRegions.WEST_ABSU, conditions.always_accessible, True),
    (
        AVRegions.WEST_ABSU,
        AVRegions.LOWER_ABSU,
        lambda s, c: conditions.can_pierce_wall(s, c) or conditions.has_any_coat(s, c),
        False,
    ),
    (
        AVRegions.LOWER_ABSU,
        AVRegions.WEST_ABSU,
        lambda s, c: conditions.can_damage(s, c) or conditions.has_any_coat(s, c),
        False,
    ),
    (AVRegions.LOWER_ABSU, AVRegions.EAST_ABSU, conditions.not_implemented, True),
    (AVRegions.EAST_ABSU, AVRegions.LOWER_ZI, conditions.always_accessible, True),
    (AVRegions.LOWER_ZI, AVRegions.LOWER_KUR, conditions.always_accessible, True),
    (AVRegions.LOWER_KUR, AVRegions.INDI, conditions.not_implemented, False),
    (AVRegions.LOWER_KUR, AVRegions.UPPER_KUR, conditions.has_any_coat, True),
    (AVRegions.INDI, AVRegions.LOWER_KUR, conditions.not_implemented, False),
    (AVRegions.INDI, AVRegions.LOWER_EDIN, conditions.has_trenchcoat, True),
    (AVRegions.LOWER_EDIN, AVRegions.UPPER_EDIN, lambda s, c: conditions.has_glitch_bomb(s, c) or conditions.has_trenchcoat(s, c), True),
)


raw_location_data = (
    ('Eribu - West of Spawn', AVRegions.WEST_ERIBU, conditions.always_accessible),
    ('Eribu - Wheelchair Room', AVRegions.WEST_ERIBU, lambda s, c: conditions.can_displacement_warp(s, c) or conditions.has_drone_tele(s, c)),

    ('Eribu - Upper Right', AVRegions.UPPER_ERIBU, conditions.always_accessible),
    (
        'Eribu - Bubble Jail',
        AVRegions.UPPER_ERIBU,
        lambda s, c: conditions.can_angle_shoot(s, c) or conditions.can_pierce_wall(s, c),
    ),
    (
        'Eribu - Outside Lab',
        AVRegions.UPPER_ERIBU,
        lambda s, c: conditions.can_drill and (conditions.can_angle_shoot(s, c) or conditions.can_pierce_wall(s, c))
    ),

    ('Eribu - Xedur Reward', AVRegions.XEDUR, conditions.always_accessible),
    ('Eribu - Below Xedur', AVRegions.XEDUR, conditions.can_drill),

    ('Eribu - Passcode Room', AVRegions.LOWER_ERIBU, conditions.not_implemented),
    ('Eribu - Path to Absu', AVRegions.LOWER_ERIBU, conditions.always_accessible),

    ('Absu - Main Room Side', AVRegions.WEST_ABSU, conditions.can_drill),
    ('Absu - Diatom Room', AVRegions.WEST_ABSU, conditions.not_implemented),
    ('Absu - Skeleton Tunnel', AVRegions.WEST_ABSU, conditions.has_drone),
    ('Absu - Below Skeleton Tunnel', AVRegions.WEST_ABSU, conditions.not_implemented),
    ('Absu - Behind Glitch Barrier', AVRegions.WEST_ABSU, conditions.not_implemented),
    ('Absu - Elsenova', AVRegions.WEST_ABSU, conditions.always_accessible),
    ('Absu - Switch Cage', AVRegions.WEST_ABSU, conditions.can_pierce_wall),

    ('Absu - Zombie Jail', AVRegions.LOWER_ABSU, conditions.not_implemented),
    ('Absu - Telal Reward', AVRegions.LOWER_ABSU, conditions.always_accessible),

    ('Absu - Trapped Diatoms', AVRegions.EAST_ABSU, conditions.can_drill),
    ('Absu - Wall Alcove', AVRegions.EAST_ABSU, conditions.can_drill),
    ('Absu - Hidden Shrine', AVRegions.EAST_ABSU, lambda s, c: conditions.has_any_coat(s, c) or conditions.has_drone(s, c)),
    ('Absu - Chasm Room Tunnel', AVRegions.EAST_ABSU, lambda s, c: conditions.has_red_coat(s, c) or conditions.has_drone(s, c)),
    ('Absu - Purple Shrine', AVRegions.EAST_ABSU, lambda s, c: conditions.has_red_coat(s, c) or conditions.has_glitch_2(s, c) and conditions.can_drill(s, c)),
    ('Absu - Zi Entrance', AVRegions.EAST_ABSU, conditions.can_drill),

    ('Zi - Behind False Wall', AVRegions.LOWER_ZI, conditions.not_implemented),
    ('Zi - Disappointment Hill', AVRegions.LOWER_ZI, conditions.not_implemented),
    ('Zi - Roof Alcove', AVRegions.LOWER_ZI, conditions.not_implemented),
    ('Zi - Above Veruska', AVRegions.LOWER_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone(s, c)),
    ('Zi - Behind Veruska Left', AVRegions.LOWER_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone(s, c)),
    ('Zi - Behind Veruska Right', AVRegions.LOWER_ZI, lambda s, c: conditions.has_trenchcoat(s, c) or conditions.has_drone(s, c)),

    ('Kur - High Jump Shrine', AVRegions.LOWER_KUR, conditions.always_accessible),
    ('Kur - High Jump Shrine - False Wall', AVRegions.LOWER_KUR, conditions.not_implemented),

    ('Kur - Inside Cliff', AVRegions.UPPER_KUR, conditions.has_red_coat),

    ('Indi - Path to Eribu', AVRegions.INDI, conditions.has_drone),
    ('Indi - Outside Save Room', AVRegions.INDI, conditions.has_trenchcoat),

    ('Ukkin-Na - Long Fall Shaft Base', AVRegions.WEST_UKKIN_NA, conditions.not_implemented),
    ('Ukkin-Na - Annihiwaiter Room', AVRegions.WEST_UKKIN_NA, conditions.not_implemented),

    ('Edin - Central Structure Behind Glitch', AVRegions.LOWER_EDIN, conditions.has_glitch_bomb),

    ('Edin - False Wall Shrine', AVRegions.UPPER_EDIN, conditions.always_accessible),
    ('Edin - Upper Drone Tunnel', AVRegions.UPPER_EDIN, lambda s, c: conditions.has_drone_tele(s, c) and conditions.has_trenchcoat(s, c))
)


location_data: t.Tuple[AVLocationData] = tuple(
    AVLocationData(id, name, region_name, access_rule)
    for id, (name, region_name, access_rule) in enumerate(raw_location_data, AP_ID_BASE)
)


LOCATION_NAME_TO_ID: t.Dict[str, int] = {
    data.name: data.id for data in location_data
}
