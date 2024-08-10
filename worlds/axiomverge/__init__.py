from worlds.AutoWorld import WebWorld, World


class AxiomVergeWebWorld(WebWorld):
    pass


class AxiomVergeWorld(World):
    """
    Explore and uncover the mystery of a surreal alien world by blasting aliens and glitching your environment
    in this intense retro side-scrolling action/adventure.
    """

    game = "Axiom Verge"
    web = AxiomVergeWebWorld()

    options = None
    options_dataclass = None

    topology_present = True

    item_name_to_id = None
    location_name_to_id = None

    item_names = None
    location_names = None
