from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BoWorld

def create_and_connect_regions(world: BoWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: BoWorld) -> None:
    crimson_bamboo_forest = Region("crimson_bamboo_forest", world.player, world.multiworld)
    uzumaki_cave = Region("uzumaki_cave", world.player, world.multiworld)
    sencho_bridge = Region("sencho_bridge", world.player, world.multiworld)
    sakura_city = Region("sakura_city", world.player, world.multiworld)
    midori_forest = Region("midori_forest", world.player, world.multiworld)
    megumi_mountain = Region("megumi_mountain", world.player, world.multiworld)
    kitsune_burrows = Region("kitsune_burrows", world.player, world.multiworld)
    ice_caverns = Region("ice_caverns", world.player, world.multiworld)
    imperial_castle = Region("imperial_castle", world.player, world.multiworld)

    regions = [crimson_bamboo_forest, uzumaki_cave, sencho_bridge,
               sakura_city, midori_forest, megumi_mountain, kitsune_burrows,
               ice_caverns, imperial_castle]

    world.multiworld.regions += regions

def connect_regions(world: BoWorld) -> None:
    crimson_bamboo_forest = world.get_region("crimson_bamboo_forest")
    uzumaki_cave = world.get_region("uzumaki_cave")
    sencho_bridge = world.get_region("sencho_bridge")
    sakura_city = world.get_region("sakura_city")
    midori_forest = world.get_region("midori_forest")
    megumi_mountain = world.get_region("megumi_mountain")
    kitsune_burrows = world.get_region("kitsune_burrows")
    ice_caverns = world.get_region("ice_caverns")
    imperial_castle = world.get_region("imperial_castle")

    crimson_bamboo_forest.connect(uzumaki_cave, "cbf_to_uc")
    crimson_bamboo_forest.connect(sencho_bridge, "cbf_to_sb")
    sencho_bridge.connect(sakura_city, "sb_to_sc")
    sakura_city.connect(midori_forest, "sc_to_mf")
    sakura_city.connect(megumi_mountain, "sc_to_mm")
    midori_forest.connect(kitsune_burrows, "mf_to_kb")
    megumi_mountain.connect(ice_caverns, "mm_to_ic")
    sakura_city.connect(imperial_castle, "sc_to_ic")