from Options import Choice, Toggle


class Goal(Choice):
    display_name = "Goal"
    option_athetos = 0
    # option_boss_rush = 1
    # option_gun_hunt = 2
    default = 0



class ProgressiveCoat(Toggle):
    """Combine Coat upgrades into a single progressive upgrade. White -> Brown -> Red."""
    display_name = "Progressive Coat Upgrades"
    default = False


class ProgressiveDrone(Toggle):
    """Combine Drone upgrades into a single progressive upgrade. Drone -> Teleport."""
    display_name = "Progressive Drone Upgrades"
    default = True
    