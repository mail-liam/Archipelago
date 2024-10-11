from __future__ import annotations

import typing as t
from BaseClasses import Location, MultiWorld, Region

from .constants import AVRegions
from .location_data import entrance_data, location_data


class AVLocation(Location):
    game = "Axiom Verge"


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
