from test.bases import WorldTestBase

from ..world import BoWorld

class BoTestBase(WorldTestBase):
    game = "Bo"
    world: BoWorld