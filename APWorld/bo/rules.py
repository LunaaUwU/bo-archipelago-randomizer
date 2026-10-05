from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has

if TYPE_CHECKING:
    from .world import BoWorld

HAS_STAFF = Has("equinox_staff")

def set_all_rules(world: BoWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: BoWorld) -> None:
    pass

def set_all_location_rules(world: BoWorld) -> None:
    if world.options.test:
        world.set_rule(
            world.get_location("kodama_forest_1"), HAS_STAFF
        )

    world.set_rule(
        world.get_location("staff_upgrade"), HAS_STAFF
    )


def set_completion_condition(world: BoWorld) -> None:
    world.set_completion_rule(Has("victory"))
