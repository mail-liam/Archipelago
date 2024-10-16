import typing as t
from collections import defaultdict

from BaseClasses import Item

from .item_data import item_data
from .constants import AVItemType


class AVItem(Item):
    game = "Axiom Verge"


BASE_ITEMPOOL = (
    "Axiom Disruptor", "Inertial Pulse", "Multi-Disruptor", "Shards", "Voranj", "Nova", "Kilver", "Reverse Slicer",
    "Laser Drill", "Remote Drone", "Address Bomb", "Enhanced Drone Launch", "Drone Teleport",
    "Passcode Tool", "TendrilsTop", "TendrilsBottom",
    "HealthNode1", "HealthNode2", "HealthNode3",
    "PowerNode1", "PowerNode2",
    "HealthNodeFragment1", "HealthNodeFragment2", "HealthNodeFragment3", "HealthNodeFragment4", "HealthNodeFragment5",
    "HealthNodeFragment6", "HealthNodeFragment7", "HealthNodeFragment8", "HealthNodeFragment9", "HealthNodeFragment10",
    "PowerNodeFragment1", "PowerNodeFragment2", "PowerNodeFragment3", "PowerNodeFragment4", "PowerNodeFragment5", "PowerNodeFragment6",
    "RangeNode1", "RangeNode2",
    "SizeNode1", "SizeNode2",
)


item_groups = defaultdict(set)
for group_name in AVItemType:
    item_groups[group_name] = {item.name for item in item_data.values() if item.group_name == group_name}
item_groups["Drill"] |= {"Remote Drone"}
item_groups["Health"] = item_groups[AVItemType.HEALTH_NODE] | item_groups[AVItemType.HEALTH_NODE_FRAGMENT]
item_groups["Power"] = item_groups[AVItemType.POWER_NODE] | item_groups[AVItemType.POWER_NODE_FRAGMENT]
item_groups["Powerups"] = item_groups["Health"] | item_groups["Power"]
item_groups["Movement + Coat"] = item_groups[AVItemType.MOVEMENT] | item_groups[AVItemType.COAT]
item_groups["Abilities"] = item_groups["Movement + Coat"] | item_groups[AVItemType.DRONE] | item_groups[AVItemType.DRILL] | item_groups[AVItemType.GLITCH] | item_groups[AVItemType.KEY] | item_groups[AVItemType.TENDRILS]
