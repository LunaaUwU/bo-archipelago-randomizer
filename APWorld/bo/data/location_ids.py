from enum import Enum

class LocType(Enum):
    KODAMA = "kodama"
    QUEST = "quest"
    BOSS = "boss" 
    SHOP_ITEM = "shop_item"
    PICKUP_ITEM = "pickup_item"
    SKILL = "skill"

LOCATIONS_BY_REGION: dict[str, dict[str, tuple[int, LocType]]] = {
    # CBF IDS -> 100-199
    "crimson_bamboo_forest": {
        "Crimson Bamboo Forest - Kodama Start": (100, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama On Ledge Left": (101, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama Hidden": (102, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama On Ledge Right": (103, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama Left Dash": (104, LocType.KODAMA),
        "Crimson Bamboo Forest - Asahi Bamboo Staff Quest": (105, LocType.QUEST),
        "Crimson Bamboo Forest - Kira Kira Bozu": (106, LocType.BOSS),
        "Crimson Bamboo Forest - Omamori Confidence": (107, LocType.PICKUP_ITEM),
        "Crimson Bamboo Forest - Bamboo Bat": (108, LocType.SKILL)
    },
    # UC IDS -> 200-299
    "uzumaki_cave": {
        "Uzumaki Cave - Kodama Start": (200, LocType.KODAMA),
        "Uzumaki Cave - Kodama Start South": (201, LocType.KODAMA),
        "Uzumaki Cave - Kodama Hidden West": (202, LocType.KODAMA),
        "Uzumaki Cave - Kodama South East": (203, LocType.KODAMA),
        "Uzumaki Cave - Kodama After Arena Bat": (204, LocType.KODAMA),
        "Uzumaki Cave - Shimeji Quest": (205, LocType.QUEST),
        "Uzumaki Cave - Eye Of The Beast Quest": (206, LocType.QUEST)
    }
}