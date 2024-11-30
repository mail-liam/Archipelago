from worlds.AutoWorld import WebWorld, World
from .constants import START_OPTION_MAP
from .item_data import item_data, ITEM_NAME_TO_ID
from .items import AVItem
from .location_data import LOCATION_NAME_TO_ID
from .options import AxiomVergeOptions, AllowRocketJumps, AllowWallGrappleClips
from .regions import create_regions
from .types import LogicContext

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


    def generate_early(self):
        options = self.options
        self.context = LogicContext(
            displacement_warp_enabled=bool(options.allow_displacement_warps),
            flight_enabled=bool(options.allow_flight),
            floor_grapple_clip_enabled=bool(options.allow_floor_grapple_clips),
            brown_rocket_jump_enabled=options.allow_rocket_jumps in {AllowRocketJumps.option_brown, AllowRocketJumps.option_both},
            red_rocket_jump_enabled=options.allow_rocket_jumps in {AllowRocketJumps.option_red, AllowRocketJumps.option_both},
            roof_grapple_clip_enabled=bool(options.allow_roof_grapple_clips),
            start_location=options.start_location,
            wall_grapple_clip_difficulty=self.options.allow_wall_grapple_clips,
            player=self.player,
        )


    def create_regions(self):
        create_regions(self.context, self.multiworld)


    def create_item(self, item_name):
        data = item_data[item_name]
        return AVItem(item_name, data.ap_classification, data.id, self.player)


    def create_items(self):
        options = self.options
        av_itempool = [self.create_item(item.name) for item in item_data.values() if item.is_default]

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

        if bool(options.progressive_drone):
            av_itempool.append(self.create_item("Progressive Drone"))
            av_itempool.append(self.create_item("Progressive Drone"))
        else:
            av_itempool.append(self.create_item("Remote Drone"))
            av_itempool.append(self.create_item("Enhanced Drone Launch"))

        av_itempool.extend(self.create_item("Health Node") for _ in range(10))


        self.multiworld.itempool.extend(av_itempool)


    def set_rules(self):
        # Debug wincon
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Voranj", self.player)

        visualize_regions(self.multiworld.get_region("Menu", self.player), "axiomverge.puml")


    def fill_slot_data(self):
        _, area, room = START_OPTION_MAP[self.options.start_location]

        return {"goal": self.options.goal, "start_area": area, "start_room": room}
