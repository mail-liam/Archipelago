from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, PerGameCommonOptions


class Goal(Choice):
    """Victory condition."""
    display_name = "Goal"
    option_athetos = 0
    # option_boss_rush = 1
    # option_gun_hunt = 2
    default = 0


class ProgressiveAddressDisruptor(DefaultOnToggle):
    """
    Combine Address Disruptors into a progressive upgrade.
    Address Bomb remains separate
    """
    display_name = "Progressive Address Disruptor"


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
    progressive_address_disruptor: ProgressiveAddressDisruptor
    progressive_coat: ProgressiveCoat
    progressive_drone: ProgressiveDrone
    secret_world_weapons: ShuffleSecretWorldWeapons
