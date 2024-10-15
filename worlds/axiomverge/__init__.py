from worlds.AutoWorld import WebWorld, World
from .item_data import item_data, ITEM_NAME_TO_ID
from .items import AVItem, BASE_ITEMPOOL
from .location_data import LOCATION_NAME_TO_ID
from .options import AxiomVergeOptions
from .regions import create_regions

from Utils import visualize_regions


class AxiomVergeWebWorld(WebWorld):
    rich_text_options_doc = True


class AxiomVergeWorld(World):
    """
    Explore and uncover the mystery of a surreal alien world by blasting aliens and glitching your environment
    in this intense retro side-scrolling action/adventure.
    """ # Source: Steam Store Page

    game = "Axiom Verge"
    web = AxiomVergeWebWorld()

    options: AxiomVergeOptions
    options_dataclass = AxiomVergeOptions

    topology_present = True

    item_name_to_id = ITEM_NAME_TO_ID
    location_name_to_id = LOCATION_NAME_TO_ID

    item_names = set(ITEM_NAME_TO_ID)
    location_names = set(LOCATION_NAME_TO_ID)

    # item_name_groups = item_groups


    def create_regions(self):
        create_regions(self.player, self.multiworld)


    def create_item(self, item_name):
        data = item_data[item_name]
        return AVItem(item_name, data.ap_classification, data.id, self.player)


    def create_items(self):
        options = self.options
        av_itempool = [self.create_item(name) for name in BASE_ITEMPOOL]

        if bool(options.progressive_address_disruptor):
            av_itempool.append(self.create_item("Progressive Address Disruptor"))
            av_itempool.append(self.create_item("Progressive Address Disruptor"))
        else:
            av_itempool.append(self.create_item("Address Disruptor 1"))
            av_itempool.append(self.create_item("Address Disruptor 2"))

        if bool(options.progressive_coat):
            av_itempool.append(self.create_item("Progressive Coat"))
            av_itempool.append(self.create_item("Progressive Coat"))
            av_itempool.append(self.create_item("Progressive Coat"))
        else:
            av_itempool.append(self.create_item("Modified Lab Coat"))
            av_itempool.append(self.create_item("Trenchcoat"))
            av_itempool.append(self.create_item("Red Coat"))

        self.multiworld.itempool.extend(av_itempool)


    def set_rules(self):
        # Debug wincon
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Voranj", self.player)

        visualize_regions(self.multiworld.get_region("Menu", self.player), "axiomverge.puml")
