from worlds.AutoWorld import World

from collections.abc import Mapping
from typing import Any

from . import items, locations, regions, rules
from . import options as bo_options

class BoWorld(World):
    """
    Bo: Path of the Teal Lotus is a 2D metroidvania action platformer inspired by Japanese folklore.
    The gameplay includes unlocking new abilities to explore the world while engaging in acrobatic aerial combat.
    """

    game = "Bo"

    options_dataclass = bo_options.BoOptions
    options: bo_options.BoOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "forest"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.BoItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "test"
        )