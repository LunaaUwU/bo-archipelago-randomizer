from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BoWorld

def create_and_connect_regions(world: BoWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: BoWorld) -> None:
    forest = Region("forest", world.player, world.multiworld)

    regions: list[Region] = [forest]

    world.multiworld.regions += regions

def connect_regions(world: BoWorld) -> None:
    pass