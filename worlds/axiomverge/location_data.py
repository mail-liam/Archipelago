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


raw_location_data = (
    ('West of Spawn', AVRegions.WEST_ERIBU, conditions.always_accessible),
    ('Upper Right', AVRegions.UPPER_ERIBU, conditions.always_accessible),
    (
        'Bubble Jail',
        AVRegions.UPPER_ERIBU,
        lambda s, p: conditions.can_angle_shoot(s, p) or conditions.can_pierce_wall(s, p),
    ),
    ('Xedur Reward', AVRegions.UPPER_ERIBU, conditions.can_angle_shoot),
    ('Below Xedur', AVRegions.UPPER_ERIBU, conditions.can_angle_shoot),
    (
        'Outside Lab',
        AVRegions.UPPER_ERIBU,
        lambda s, p: conditions.can_drill and (conditions.can_angle_shoot(s, p) or conditions.can_pierce_wall(s, p))
    ),
    ('Path to Absu', AVRegions.LOWER_ERIBU, conditions.always_accessible),
    ('Main Room Side', AVRegions.WEST_ABSU, conditions.can_drill),
    ('Elsenova', AVRegions.WEST_ABSU, conditions.always_accessible),
    ('Switch Cage', AVRegions.WEST_ABSU, conditions.can_pierce_wall),

    ('Zombie Jail', AVRegions.LOWER_ABSU, conditions.always_accessible),


    # (11, 'Absu - Telal Reward', 'Kilver + Drill/Labcoat+Drill/Trenchcoat + Drill/Drone Tele/Red Coat'),
)


location_data: t.Tuple[AVLocationData] = tuple(
    AVLocationData(id, name, region_name, access_rule)
    for id, (name, region_name, access_rule) in enumerate(raw_location_data, AP_ID_BASE)
)


LOCATION_NAME_TO_ID: t.Dict[str, int] = {
    data.name: data.id for data in location_data
}
