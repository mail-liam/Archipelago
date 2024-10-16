from __future__ import annotations

import typing as t
from BaseClasses import Location, MultiWorld, Region

from .constants import AVRegions
from .location_data import entrance_data, location_data

if t.TYPE_CHECKING:
    from .types import LogicContext


class AVLocation(Location):
    game = "Axiom Verge"


def create_regions(context: LogicContext, multiworld: MultiWorld):
    regions: t.Dict[str, Region] = {}
    for enum_type in AVRegions:
        region_name = enum_type.value
        region = Region(region_name, context.player, multiworld)
        multiworld.regions.append(region)
        regions[region_name] = region

    for source_name, dest_name, condition_func, bidirectional in entrance_data:
        source, destination = regions[source_name], regions[dest_name]
        access_rule = lambda state, func=condition_func: func(state, context)
        source.connect(destination, rule=access_rule)

        if bidirectional:
            destination.connect(source, rule=access_rule)

    for data in location_data:
        region = regions[data.region_name]
        location = AVLocation(context.player, data.name, data.id, region)
        location.access_rule = lambda state, data=data: data.access_rule(state, context)
        region.locations.append(location)
