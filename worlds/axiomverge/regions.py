from __future__ import annotations

import typing as t
from BaseClasses import Location, MultiWorld, Region

from worlds.axiomverge import conditions
from .constants import AVRegions
from .location_data import location_data

if t.TYPE_CHECKING:
    from BaseClasses import CollectionState


class AVLocation(Location):
    game = "Axiom Verge"


# Start Region, Destination Region, Access Rule
entrance_data: t.Tuple[t.Tuple[str, str, t.Callable[[CollectionState, int], bool]]] = (
    # TODO: Menu region connection to be dynamic with start location rando
    (AVRegions.MENU, AVRegions.WEST_ERIBU, conditions.always_accessible),
    (AVRegions.WEST_ERIBU, AVRegions.UPPER_ERIBU, conditions.can_damage),
    (AVRegions.UPPER_ERIBU, AVRegions.LOWER_ERIBU, conditions.can_drill),
    (AVRegions.LOWER_ERIBU, AVRegions.WEST_ABSU, conditions.always_accessible),
    (AVRegions.WEST_ABSU, AVRegions.LOWER_ABSU, lambda s,
     p: conditions.can_pierce_wall(s, p) or conditions.has_any_coat(s, p)),
)


def create_regions(player: int, multiworld: MultiWorld):
    regions: t.Dict[str, Region] = {region_name: Region(
        region_name, player, multiworld) for region_name in AVRegions}

    for (source_name, dest_name, condition) in entrance_data:
        regions[source_name].connect(
            regions[dest_name], rule=lambda state: condition(state, player))

    for data in location_data:
        location = AVLocation(player, data.name, data.id,
                              regions[data.region_name])
        location.access_rule = lambda state: data.access_rule(state, player)
