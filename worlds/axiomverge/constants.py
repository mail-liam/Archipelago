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
    BLURST = "Blurst"
    DINGER_GISBAR = "Dinger-Gisbar"
    EAST_ABSU = "East Absu"
    # E_KUR_MAH = "E-Kur-Mah"
    INDI = "Indi"
    LABORATORY = "Laboratory"
    LOWER_ABSU = "Lower Absu"
    LOWER_EDIN = "Lower Edin"
    LOWER_ERIBU = "Lower Eribu"
    LOWER_KUR = "Lower Kur"
    LOWER_ZI = "Lower Zi"
    # MAR_URU = "Mar-Uru"
    MENU = "Menu"
    UPPER_EDIN = "Upper Edin"
    UPPER_ERIBU = "Upper Eribu"
    UPPER_KUR = "Upper Kur"
    WEST_ABSU = "West Absu"
    WEST_ERIBU = "West Eribu"
    WEST_UKKIN_NA = "West Ukkin-Na"
    XEDUR = "Xedur"
