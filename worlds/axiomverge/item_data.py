import typing as t
from dataclasses import dataclass

from BaseClasses import ItemClassification

from .constants import AVItemType, AP_ID_BASE


@dataclass
class AVItemData:
    id: int
    name: str
    group_name: str
    ap_classification: ItemClassification


raw_item_data: t.Tuple[int, str, AVItemType, ItemClassification] = (
    (
        0,
        "Axiom Disruptor",
        AVItemType.WEAPON.value,
        ItemClassification.progression_skip_balancing,
    ),
    # (1, "DataGrenade", AVItemType.WEAPON),
    # (2, "FireWall", AVItemType.WEAPON),
    (3, "Inertial Pulse", AVItemType.WEAPON, ItemClassification.progression_skip_balancing),
    # (4, "IonBeam", AVItemType.WEAPON),
    # (5, "LightningGun", AVItemType.WEAPON),
    (
        6,
        "Multi-Disruptor",
        AVItemType.WEAPON,
        ItemClassification.progression_skip_balancing,
    ),
    # (7, "Reflect", AVItemType.WEAPON),
    # (8, "Shards", AVItemType.WEAPON, ItemClassification.progression_skip_balancing),
    # (9, "Swim", AVItemType.WEAPON),
    # (10, "TriCone", AVItemType.WEAPON),
    (
        11,
        "Voranj",
        AVItemType.WEAPON.value,
        ItemClassification.progression_skip_balancing,
    ),
    (12, "Nova", AVItemType.WEAPON, ItemClassification.progression),
    # (13, "TetheredCharge", AVItemType.WEAPON),
    # (14, "VerticalSpread", AVItemType.WEAPON),
    # (15, "WallTrace", AVItemType.WEAPON),
    # (16, "DistortionField", AVItemType.WEAPON),
    # (17, "FlameThrower", AVItemType.WEAPON),
    (18, "Kilver", AVItemType.WEAPON, ItemClassification.progression),
    # (19, "Scythe", AVItemType.WEAPON),
    # (20, "FatBeam", AVItemType.WEAPON),
    # (21, "HeatSeeker", AVItemType.WEAPON),
    # (22, "WebSlicer", AVItemType.WEAPON),
    (23, "Address Disruptor 1", AVItemType.GLITCH, ItemClassification.progression),
    (24, "Address Disruptor 2", AVItemType.GLITCH, ItemClassification.progression),
    # (25, "Progressive Address Disruptor", AVItemType.GLITCH, ItemClassification.progression),
    (26, "Laser Drill", AVItemType.DRILL, ItemClassification.progression),
    (27, "Remote Drone", AVItemType.DRONE, ItemClassification.progression),
    (28, "Address Bomb", AVItemType.GLITCH, ItemClassification.progression),
    # (29, "Grapple", AVItemType.MOVEMENT, True),
    # (30, "HighJump", AVItemType.MOVEMENT, True),
    (31, "Modified Lab Coat", AVItemType.COAT, ItemClassification.progression),
    (32, "Trenchcoat", AVItemType.COAT, ItemClassification.progression),
    (33, "Red Coat", AVItemType.COAT, ItemClassification.progression),
    # (34, "Progressive Coat", AVItemType.COAT, ItemClassification.progression),
    # (35, "BreachSuppressor", AVItemType.KEY, True),
    (36, "Enhanced Drone Launch", AVItemType.DRONE, ItemClassification.progression),
    (37, "Drone Teleport", AVItemType.DRONE, ItemClassification.progression),
    (38, "Passcode Tool", AVItemType.KEY, ItemClassification.progression),
    (39, "TendrilsTop", AVItemType.TENDRILS, ItemClassification.filler),
    (40, "TendrilsBottom", AVItemType.TENDRILS, ItemClassification.filler),
    (41, "HealthNode1", AVItemType.HEALTH_NODE, ItemClassification.useful),
    (42, "HealthNode2", AVItemType.HEALTH_NODE, ItemClassification.useful),
    (43, "HealthNode3", AVItemType.HEALTH_NODE, ItemClassification.useful),
    # (44, "HealthNode4", AVItemType.HEALTH_NODE),
    # (45, "HealthNode5", AVItemType.HEALTH_NODE),
    # (46, "HealthNode6", AVItemType.HEALTH_NODE),
    # (47, "HealthNode7", AVItemType.HEALTH_NODE),
    # (48, "HealthNode8", AVItemType.HEALTH_NODE),
    # (49, "HealthNode9", AVItemType.HEALTH_NODE),
    # (50, "HealthNode10", AVItemType.HEALTH_NODE),
    (51, "PowerNode1", AVItemType.POWER_NODE, ItemClassification.useful),
    (52, "PowerNode2", AVItemType.POWER_NODE, ItemClassification.useful),
    # (53, "PowerNode3", AVItemType.POWER_NODE, ItemClassification.useful),
    # (54, "PowerNode4", AVItemType.POWER_NODE),
    # (55, "PowerNode5", AVItemType.POWER_NODE),
    # (56, "PowerNode6", AVItemType.POWER_NODE),
    # (57, "PowerNode7", AVItemType.POWER_NODE),
    # (58, "PowerNode8", AVItemType.POWER_NODE),
    (59, "HealthNodeFragment1", AVItemType.HEALTH_NODE_FRAGMENT, ItemClassification.useful),
    (60, "HealthNodeFragment2", AVItemType.HEALTH_NODE_FRAGMENT, ItemClassification.useful),
    (61, "HealthNodeFragment3", AVItemType.HEALTH_NODE_FRAGMENT, ItemClassification.useful),
    (62, "HealthNodeFragment4", AVItemType.HEALTH_NODE_FRAGMENT, ItemClassification.useful),
    (63, "HealthNodeFragment5", AVItemType.HEALTH_NODE_FRAGMENT, ItemClassification.useful),
    # (64, "HealthNodeFragment6", AVItemType.HEALTH_NODE_FRAGMENT),
    # (65, "HealthNodeFragment7", AVItemType.HEALTH_NODE_FRAGMENT),
    # (66, "HealthNodeFragment8", AVItemType.HEALTH_NODE_FRAGMENT),
    # (67, "HealthNodeFragment9", AVItemType.HEALTH_NODE_FRAGMENT),
    # (68, "HealthNodeFragment10", AVItemType.HEALTH_NODE_FRAGMENT),
    # (69, "HealthNodeFragment11", AVItemType.HEALTH_NODE_FRAGMENT),
    # (70, "HealthNodeFragment12", AVItemType.HEALTH_NODE_FRAGMENT),
    # (71, "HealthNodeFragment13", AVItemType.HEALTH_NODE_FRAGMENT),
    # (72, "HealthNodeFragment14", AVItemType.HEALTH_NODE_FRAGMENT),
    # (73, "HealthNodeFragment15", AVItemType.HEALTH_NODE_FRAGMENT),
    # (74, "HealthNodeFragment16", AVItemType.HEALTH_NODE_FRAGMENT),
    # (75, "HealthNodeFragment17", AVItemType.HEALTH_NODE_FRAGMENT),
    # (76, "HealthNodeFragment18", AVItemType.HEALTH_NODE_FRAGMENT),
    # (77, "HealthNodeFragment19", AVItemType.HEALTH_NODE_FRAGMENT),
    # (78, "HealthNodeFragment20", AVItemType.HEALTH_NODE_FRAGMENT),
    # (79, "HealthNodeFragment21", AVItemType.HEALTH_NODE_FRAGMENT),
    # (80, "HealthNodeFragment22", AVItemType.HEALTH_NODE_FRAGMENT),
    # (81, "HealthNodeFragment23", AVItemType.HEALTH_NODE_FRAGMENT),
    # (82, "HealthNodeFragment24", AVItemType.HEALTH_NODE_FRAGMENT),
    # (83, "HealthNodeFragment25", AVItemType.HEALTH_NODE_FRAGMENT),
    # (84, "HealthNodeFragment26", AVItemType.HEALTH_NODE_FRAGMENT),
    # (85, "HealthNodeFragment27", AVItemType.HEALTH_NODE_FRAGMENT),
    # (86, "HealthNodeFragment28", AVItemType.HEALTH_NODE_FRAGMENT),
    # (87, "HealthNodeFragment29", AVItemType.HEALTH_NODE_FRAGMENT),
    # (88, "HealthNodeFragment30", AVItemType.HEALTH_NODE_FRAGMENT),
    (89, "PowerNodeFragment1", AVItemType.POWER_NODE_FRAGMENT, ItemClassification.useful),
    (90, "PowerNodeFragment2", AVItemType.POWER_NODE_FRAGMENT, ItemClassification.useful),
    (91, "PowerNodeFragment3", AVItemType.POWER_NODE_FRAGMENT, ItemClassification.useful),
    (92, "PowerNodeFragment4", AVItemType.POWER_NODE_FRAGMENT, ItemClassification.useful),
    (93, "PowerNodeFragment5", AVItemType.POWER_NODE_FRAGMENT, ItemClassification.useful),
    (94, "PowerNodeFragment6", AVItemType.POWER_NODE_FRAGMENT, ItemClassification.useful),
    # (95, "PowerNodeFragment7", AVItemType.POWER_NODE_FRAGMENT),
    # (96, "PowerNodeFragment8", AVItemType.POWER_NODE_FRAGMENT),
    # (97, "PowerNodeFragment9", AVItemType.POWER_NODE_FRAGMENT),
    # (98, "PowerNodeFragment10", AVItemType.POWER_NODE_FRAGMENT),
    # (99, "PowerNodeFragment11", AVItemType.POWER_NODE_FRAGMENT),
    # (100, "PowerNodeFragment12", AVItemType.POWER_NODE_FRAGMENT),
    # (101, "PowerNodeFragment13", AVItemType.POWER_NODE_FRAGMENT),
    # (102, "PowerNodeFragment14", AVItemType.POWER_NODE_FRAGMENT),
    # (103, "PowerNodeFragment15", AVItemType.POWER_NODE_FRAGMENT),
    # (104, "PowerNodeFragment16", AVItemType.POWER_NODE_FRAGMENT),
    # (105, "PowerNodeFragment17", AVItemType.POWER_NODE_FRAGMENT),
    # (106, "PowerNodeFragment18", AVItemType.POWER_NODE_FRAGMENT),
    # (107, "PowerNodeFragment19", AVItemType.POWER_NODE_FRAGMENT),
    # (108, "PowerNodeFragment20", AVItemType.POWER_NODE_FRAGMENT),
    # (109, "PowerNodeFragment21", AVItemType.POWER_NODE_FRAGMENT),
    # (110, "PowerNodeFragment22", AVItemType.POWER_NODE_FRAGMENT),
    # (111, "PowerNodeFragment23", AVItemType.POWER_NODE_FRAGMENT),
    # (112, "PowerNodeFragment24", AVItemType.POWER_NODE_FRAGMENT),
    # (113, "PowerNodeFragment25", AVItemType.POWER_NODE_FRAGMENT),
    # (114, "PowerNodeFragment26", AVItemType.POWER_NODE_FRAGMENT),
    # (115, "PowerNodeFragment27", AVItemType.POWER_NODE_FRAGMENT),
    # (116, "PowerNodeFragment28", AVItemType.POWER_NODE_FRAGMENT),
    # (117, "PowerNodeFragment29", AVItemType.POWER_NODE_FRAGMENT),
    # (118, "PowerNodeFragment30", AVItemType.POWER_NODE_FRAGMENT),
    (119, "RangeNode1", AVItemType.RANGE_NODE, ItemClassification.useful),
    (120, "RangeNode2", AVItemType.RANGE_NODE, ItemClassification.useful),
    # (121, "RangeNode3", AVItemType.RANGE_NODE),
    # (122, "RangeNode4", AVItemType.RANGE_NODE),
    (123, "SizeNode1", AVItemType.SIZE_NODE, ItemClassification.useful),
    (124, "SizeNode2", AVItemType.SIZE_NODE, ItemClassification.useful),
    # (125, "SizeNode3", AVItemType.SIZE_NODE),
    # (126, "SizeNode4", AVItemType.SIZE_NODE),
)

item_data: t.Dict[str, AVItemData] = {
    name: AVItemData(AP_ID_BASE + id, name, group_name, ap_classification)
    for (id, name, group_name, ap_classification) in raw_item_data
}

ITEM_NAME_TO_ID: t.Dict[str, int] = {data.name: data.id for data in item_data.values()}
