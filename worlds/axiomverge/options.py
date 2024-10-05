from dataclasses import dataclass
from Options import Choice, Toggle, PerGameCommonOptions


class Goal(Choice):
    display_name = "Goal"
    option_athetos = 0
    # option_boss_rush = 1
    # option_gun_hunt = 2
    default = 0



class ProgressiveCoat(Toggle):
    """Combine Coat upgrades into a single progressive upgrade. Lab -> Trench -> Red."""
    display_name = "Progressive Coat Upgrades"
    default = True


class ProgressiveDrone(Toggle):
    """Combine Drone upgrades into a single progressive upgrade. Drone -> Teleport."""
    display_name = "Progressive Drone Upgrades"
    default = True


class SecretWorldWeapons(Toggle):
    """Randomize Secret world weapons into the item pool."""
    default = True


@dataclass
class AxiomVergeOptions(PerGameCommonOptions):
    goal: Goal
    progressive_coat: ProgressiveCoat
    progressive_drone: ProgressiveDrone
    secret_world_weapons: SecretWorldWeapons