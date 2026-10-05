from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BoWorld

ITEM_NAME_TO_ID = {
    "equinox_staff": 1,
    "fox_fire_30": 2
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "equinox_staff": ItemClassification.progression,
    "fox_fire_30": ItemClassification.filler
}

class BoItem(Item):
    game = "Bo"

def get_random_item_filler(world: BoWorld) -> str:
    return "fox_fire_30"

def create_item_with_correct_classification(world: BoWorld, name: str) -> BoItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return BoItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: BoWorld) -> None:
    itempool = [
        world.create_item("equinox_staff")
    ]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool