from enum import StrEnum


AP_ID_BASE = 2 ** 50


class AVItemType(StrEnum):
    COAT = "Coat"
    DRILL = "Drill"
    DRONE = "Drone"
    GLITCH = "Glitch"
    HEALTH_NODE = "Health Node"
    HEALTH_NODE_FRAGMENT = "Health Node Fragment"
    KEY = "Key"
    MOVEMENT = "Movement"
    NOTE = "Note"
    POWER_NODE = "Power Node"
    POWER_NODE_FRAGMENT = "Power Node Fragment"
    RANGE_NODE = "Range Node"
    SIZE_NODE = "Size Node"
    TENDRILS = "Tendrils"
    WEAPON = "Weapon"


class AVRegions(StrEnum):
    # Eribu
    WEST_ERIBU = "West Eribu"
    DINGER_GISBAR = "Dinger-Gisbar"
    UPPER_ERIBU = "Upper Eribu"
    LABORATORY = "Laboratory"
    XEDUR = "Xedur"
    LOWER_ERIBU = "Lower Eribu"
    ERIBU_UKKIN_NA = "Eribu-Ukkin-Na"
    ERIBU_INDI = "Eribu-Indi"

    # Absu
    WEST_ABSU = "West Absu"
    WEST_ATTIC = "West Attic"
    EAST_ATTIC = "East Attic"
    ELSENOVA = "Elsenova"
    LOWER_ABSU = "Lower Absu"
    ABSU_BASEMENT = "Absu Basement"
    TELAL = "Telal"
    LOWER_CORRIDOR = "Lower Corridor"
    EAST_ABSU = "East Absu"
    EAST_ABSU_DRONE = "East Absu Drone"
    INDI_TUNNEL = "Indi Tunnel"

    # Absu microregions (Thanks Drone)
    EA_LEDGE = "East Absu Ledge"
    EA_BEHIND_TELAL = "Behind Telal"
    EA_ALCOVE = "East Absu Alcove"
    EA_HIDDEN_SHRINE = "Hidden Shrine"
    EA_CHASM_TUNNEL = "Chasm Tunnel"
    EA_ZI_ENTRANCE = "Zi Entrance"

    # Zi
    ABSU_ZI = "Absu-Zi"
    LOWER_ZI = "Lower Zi"
    EAST_ZI = "East Zi"
    UPPER_ZI = "Upper Zi"
    PREVIEW_ROOM = "Preview Room"
    ZI_INDI = "Zi-Indi"
    URUKU = "Uruku"

    # Kur
    LOWER_CAVES = "Lower Caves"
    KUR_INDI = "Kur-Indi"
    GAUNTLET_ROOM = "Gauntlet Room"
    GAUNTLET_REWARD = "Gauntlet Reward"
    UPPER_CAVES = "Upper Caves"
    KUR_EDIN = "Kur-Edin"
    MOUNTAIN_BASE = "Mountain Base"
    LOWER_GIR_TAB = "Lower Gir-Tab"
    UPPER_GIR_TAB = "Upper Gir-Tab"
    BEHIND_GIR_TAB = "Behind Gir-Tab"

    # Indi
    INDI = "Indi"
    WEST_INDI = "West Indi"

    # Ukkin-Na
    WEST_UKKIN_NA_EXIT = "West Ukkin-Na Exit"
    UKKIN_NA_BASE = "Ukkin-Na Base"
    SOUTH_UKKIN_NA_EXIT = "South Ukkin-Na Exit"
    VISION = "Vision"
    OPHELIA = "Ophelia"
    EAST_UKKIN_NA_EXIT = "East Ukkin-Na Exit"

    # Edin
    LOWER_EDIN = "Lower Edin"
    UKHU = "Ukhu"
    CLONE = "Clone"
    HANGAR = "Hangar"
    EAST_EDIN = "East Edin"

    # E-Kur-Mah
    UPPER_E_KUR_MAH = "Upper E-Kur-Mah"
    LOWER_E_KUR_MAH = "Lower E-Kur-Mah"

    # Mar-Uru
    MAR_URU_ENTRANCE = "Mar-Uru Entrance"
    POST_SENTINEL = "Post Sentinel"
    SENTRY_BOT_ROOM = "Sentry Bot Room"
    ATHETOS = "Athetos"

    MENU = "Menu"
    BLURST = "Blurst"
    


START_OPTION_MAP = [
    (AVRegions.WEST_ERIBU, "Area1", "SaveRoom1"),
    (AVRegions.ELSENOVA, "Area2", "SaveRoom2"),
    (AVRegions.EAST_ABSU, "Area2", "SaveRoom4"),
]
