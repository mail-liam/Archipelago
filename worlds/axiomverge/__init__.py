from worlds.AutoWorld import WebWorld, World
from .items import item_groups
from .options import AxiomVergeOptions


class AxiomVergeWebWorld(WebWorld):
    rich_text_options_doc = True


class AxiomVergeWorld(World):
    """
    Explore and uncover the mystery of a surreal alien world by blasting aliens and glitching your environment
    in this intense retro side-scrolling action/adventure.
    """

    game = "Axiom Verge"
    web = AxiomVergeWebWorld()

    options = AxiomVergeOptions
    options_dataclass = AxiomVergeOptions

    topology_present = True

    item_name_to_id = None
    location_name_to_id = None

    item_names = None
    location_names = None

    item_name_groups = item_groups
