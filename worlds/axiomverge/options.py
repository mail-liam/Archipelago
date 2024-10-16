from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, PerGameCommonOptions, Toggle


class Goal(Choice):
    """Victory condition."""
    display_name = "Goal"
    option_athetos = 0
    # option_boss_rush = 1
    # option_gun_hunt = 2
    default = 0

# Item Options
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


# Logic Options
class AllowDisplacementWarps(Toggle):
    """Allows for displacement warps to be considered in logic."""


class AllowFlight(Toggle):
    """Allows for flying to be considered in logic."""


class AllowGrappleClips(Toggle):
    """Allows for grapple clips to be considered in logic."""


class AllowRocketJumps(Toggle):
    """Allows for rocket jumps to be considered in logic."""


@dataclass
class AxiomVergeOptions(PerGameCommonOptions):
    allow_displacement_warps: AllowDisplacementWarps
    allow_flight: AllowFlight
    allow_grapple_clips: AllowGrappleClips
    allow_rocket_jumps: AllowRocketJumps
    goal: Goal
    progressive_address_disruptor: ProgressiveAddressDisruptor
    progressive_coat: ProgressiveCoat
    progressive_drone: ProgressiveDrone
    secret_world_weapons: ShuffleSecretWorldWeapons
