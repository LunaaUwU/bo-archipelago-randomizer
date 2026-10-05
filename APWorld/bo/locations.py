from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import BoWorld


LOCATION_NAME_TO_ID = {
    "equinox_staff": 1,
    "kodama_forest_1": 2
}

class BoLocation(Location):
    game = "Bo"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: BoWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: BoWorld) -> None:
    forest = world.get_region("forest")

    # === REGION LOCS ===
    forest_locations = get_location_names_with_ids(
        ["equinox_staff"]
    )

    if world.options.test:
        forest_locations.append("kodama_forest_1")

    forest.add_locations(forest_locations, BoLocation)

def create_events(world: BoWorld) -> None:
    forest = world.get_region("forest")

    forest.add_event(
        "staff_upgrade", "victory", location_type=BoLocation, item_type=items.BoItem
    )