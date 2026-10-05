from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

def Test(Toggle):
    """
    Test toggle option.
    """
    display_name = "Test"

@dataclass
class BoOptions(PerGameCommonOptions):
    test: Test

option_groups = [
    OptionGroup(
        "Test Group",
        [Test]
    )
]