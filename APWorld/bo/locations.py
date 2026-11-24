from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import ItemClassification, Location

from . import items
from data.location_ids import LOCATIONS_BY_REGION

if TYPE_CHECKING:
    from .world import BoWorld


class BoLocation(Location):
    game = "Bo"


def create_all_locations(world: BoWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: BoWorld) -> None:
    crimson_bamboo_forest = world.get_region("crimson_bamboo_forest")


def create_events(world: BoWorld) -> None:
    pass
    # crimson_bamboo_forest = world.get_region("crimson_bamboo_forest")

    # crimson_bamboo_forest.add_event(
    #     "staff_upgrade", "victory", location_type=BoLocation, item_type=items.BoItem
    # )