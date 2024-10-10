from __future__ import annotations

import typing as t
from BaseClasses import Location, MultiWorld, Region

from .constants import AVRegions
from .location_data import location_data
from .logic import conditions

if t.TYPE_CHECKING:
    from BaseClasses import CollectionState


class AVLocation(Location):
    game = "Axiom Verge"


# Start Region, Destination Region, Access Rule, Bidirectional
entrance_data: t.Tuple[t.Tuple[str, str, t.Callable[[CollectionState, int], bool], bool]] = (
    # TODO: Menu region connection to be dynamic with start location rando
    (AVRegions.MENU, AVRegions.WEST_ERIBU, conditions.always_accessible, False),  # True in the purest sense, but it won't ever matter
    (AVRegions.WEST_ERIBU, AVRegions.UPPER_ERIBU, conditions.can_damage, True),
    (AVRegions.UPPER_ERIBU, AVRegions.LOWER_ERIBU, conditions.can_drill, True),
    (AVRegions.LOWER_ERIBU, AVRegions.WEST_ABSU, conditions.always_accessible, True),
    (
        AVRegions.WEST_ABSU,
        AVRegions.LOWER_ABSU,
        lambda s, p: conditions.can_pierce_wall(s, p) or conditions.has_any_coat(s, p),
        False,
    ),
    (
        AVRegions.LOWER_ABSU,
        AVRegions.WEST_ABSU,
        lambda s, p: conditions.can_damage(s, p) or conditions.has_any_coat(s, p),
        False,
    )
)


def create_regions(player: int, multiworld: MultiWorld):
    regions: t.Dict[str, Region] = {}
    for enum_type in AVRegions:
        region_name = enum_type.value
        region = Region(region_name, player, multiworld)
        multiworld.regions.append(region)
        regions[region_name] = region

    for source_name, dest_name, condition_func, bidirectional in entrance_data:
        source, destination = regions[source_name], regions[dest_name]
        access_rule = lambda state, func=condition_func: func(state, player)
        source.connect(destination, rule=access_rule)

        if bidirectional:
            destination.connect(source, rule=access_rule)

    for data in location_data:
        region = regions[data.region_name]
        location = AVLocation(player, data.name, data.id, region)
        location.access_rule = lambda state, data=data: data.access_rule(state, player)
        region.locations.append(location)
