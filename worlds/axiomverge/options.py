from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, PerGameCommonOptions


class Goal(Choice):
    """Victory condition."""
    display_name = "Goal"
    option_athetos = 0
    # option_boss_rush = 1
    # option_gun_hunt = 2
    default = 0


class ProgressiveCoat(DefaultOnToggle):
    """Combine Coat upgrades into a single progressive upgrade. Lab -> Trench -> Red."""
    display_name = "Progressive Coat Upgrades"


class ProgressiveDrone(DefaultOnToggle):
    """Combine Drone upgrades into a single progressive upgrade. Drone -> Launcher -> Teleport."""
    display_name = "Progressive Drone Upgrades"


class ShuffleSecretWorldWeapons(DefaultOnToggle):
    """Randomize Secret world weapons into the item pool."""


@dataclass
class AxiomVergeOptions(PerGameCommonOptions):
    goal: Goal
    progressive_coat: ProgressiveCoat
    progressive_drone: ProgressiveDrone
    secret_world_weapons: ShuffleSecretWorldWeapons
