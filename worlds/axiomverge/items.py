from collections import defaultdict
from .item_data import item_data, ItemType


item_groups = defaultdict(set)
for group_name in ItemType:
    item_groups[group_name] = {item.name for item in item_data if item.group_name == group_name}
item_groups["Drill"] |= {"Drone"}
item_groups["Health"] = item_groups[ItemType.HEALTH_NODE] | item_groups[ItemType.HEALTH_NODE_FRAGMENT]
item_groups["Power"] = item_groups[ItemType.POWER_NODE] | item_groups[ItemType.POWER_NODE_FRAGMENT]
item_groups["Nodes"] = item_groups["Health"] | item_groups["Power"]
item_groups["Movement + Coat"] = item_groups[ItemType.MOVEMENT] | item_groups[ItemType.COAT]
item_groups["Abilities"] = item_groups["Movement + Coat"] | item_groups[ItemType.DRONE] | item_groups[ItemType.DRILL] | item_groups[ItemType.GLITCH] | item_groups[ItemType.KEY] | item_groups[ItemType.TENDRILS]
