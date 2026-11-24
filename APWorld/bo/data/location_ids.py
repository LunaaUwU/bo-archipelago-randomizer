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
        "Crimson Bamboo Forest - Kodama: Start": (100, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama: On Ledge Left": (101, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama: Hidden": (102, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama: On Ledge Right": (103, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama: Left Dash": (104, LocType.KODAMA),
        "Crimson Bamboo Forest - Quest: Asahi Bamboo Staff": (105, LocType.QUEST),
        "Crimson Bamboo Forest - Quest: Rozus Requiem": (106, LocType.QUEST),
        "Crimson Bamboo Forest - Boss: Kira Kira Bozu": (107, LocType.BOSS),
        "Crimson Bamboo Forest - Omamori: Confidence": (108, LocType.PICKUP_ITEM),
        "Crimson Bamboo Forest - Omamori: Progress": (109, LocType.PICKUP_ITEM),
        "Crimson Bamboo Forest - Bamboo Bat": (110, LocType.SKILL)
    },
    # UC IDS -> 200-299
    "uzumaki_cave": {
        "Uzumaki Cave - Kodama: Start": (200, LocType.KODAMA),
        "Uzumaki Cave - Kodama: Start South": (201, LocType.KODAMA),
        "Uzumaki Cave - Kodama: Hidden West": (202, LocType.KODAMA),
        "Uzumaki Cave - Kodama: South East": (203, LocType.KODAMA),
        "Uzumaki Cave - Kodama: After Arena Armapillo": (204, LocType.KODAMA),
        "Uzumaki Cave - Quest: Shimeji": (205, LocType.QUEST),
        "Uzumaki Cave - Quest: Eye Of The Beast": (206, LocType.QUEST),
        "Uzumaki Cave - Boss: Particulary Unmanageable Armapillo": (207, LocType.BOSS),
        "Uzumaki Cave - Omamori: Prosperity": (208, LocType.SHOP_ITEM),
        "Uzumaki Cave - Omamori Strap": (209, LocType.SHOP_ITEM),
        "Uzumaki Cave - Daruma: Chomper": (210, LocType.PICKUP_ITEM),
        "Uzumaki Cave - Lotus Dash": (211, LocType.SKILL)
    },
    "sencho_bridge": {
        "Sencho Bridge - Boss: Hashihime": (300, LocType.BOSS),
        "Sencho Bridge - Daruma: Pyro-Kun": (301, LocType.PICKUP_ITEM),
        "Sencho Bridge - Awakening Ink": (302, LocType.PICKUP_ITEM)
    },
    "sakura_city": {
        "Sakura City - Kodama: Start Bush": (400, LocType.KODAMA),
        "Sakura City - Kodama: Top of City Archives": (401, LocType.KODAMA),
        "Sakura City - Quest: Vermillion Stranger": (402, LocType.QUEST),
        "Sakura City - Quest: Daruma": (403, LocType.QUEST),
        "Sakura City - Boss: Gashadokuro": (404, LocType.BOSS),
        "Sakura City - Omamori Strap: Shrine of the Lillies": (405, LocType.SHOP_ITEM),
        "Sakura City - Omamori: Health": (406, LocType.SHOP_ITEM),
        "Sakura City - Omamori: Resilience": (407, LocType.SHOP_ITEM),
        "Sakura City - Omamori: Refinement": (408, LocType.SHOP_ITEM),
        "Sakura City - Omamori: Innovation": (409, LocType.SHOP_ITEM),
        "Sakura City - Omamori Strap: Fox Couple's House": (410, LocType.SHOP_ITEM),
        "Sakura City - Omamori: Stability": (411, LocType.SHOP_ITEM),
        "Sakura City - Omamori: Favor": (412, LocType.SHOP_ITEM),
        "Sakura City - Omamori: Optimism": (413, LocType.SHOP_ITEM),
        "Sakura City - Omamori: Providence": (414, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Jingu": (415, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Ken": (416, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Mamori": (417, LocType.SHOP_ITEM),
        "Sakura City - Awakening Ink: Daruma Shop": (418, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Chomper Two Eyes": (419, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Pyro-Kun Two Eyes": (420, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Ken Two Eyes": (421, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Jingu Two Eyes": (422, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Toge-Chan Two Eyes": (423, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Mamori Two Eyes": (424, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Yuki Two Eyes": (425, LocType.SHOP_ITEM),
        "Sakura City - Daruma: Kaboomaru Two Eyes": (426, LocType.SHOP_ITEM),
        "Sakura City - Kettle Upgrade: Saijo Sip": (427, LocType.SHOP_ITEM),
        "Sakura City - Kettle Upgrade: Fusen Fil": (428, LocType.SHOP_ITEM),
        "Sakura City - Kettle Upgrade: Ocha Oasis": (429, LocType.SHOP_ITEM),
        "Sakura City - Kettle Upgrade: Kanpai Capacity": (430, LocType.SHOP_ITEM),
        "Sakura City - Kettle Upgrade: Surging Tsunami": (431, LocType.SHOP_ITEM),
        "Sakura City - Health Upgrade: Lotus Ramen": (432, LocType.SHOP_ITEM),
        "Sakura City - Health Upgrade: Teal Ramen": (433, LocType.SHOP_ITEM),
        "Sakura City - Health Upgrade: Crystal Ramen": (434, LocType.SHOP_ITEM),
        "Sakura City - Health Upgrade: Silky Smooth Ramen": (435, LocType.SHOP_ITEM),
        "Sakura City - Health Upgrade: Spicy Ramen": (436, LocType.SHOP_ITEM),
        "Sakura City - Staff Upgrade: Staff Upgrade 1": (437, LocType.SHOP_ITEM),
        "Sakura City - Staff Upgrade: Staff Upgrade 2": (438, LocType.SHOP_ITEM),
        "Sakura City - Staff Upgrade: Staff Upgrade 3": (439, LocType.SHOP_ITEM),
        "Sakura City - Lotus Seed: Sumo Pagoda": (440, LocType.PICKUP_ITEM),
        "Sakura City - Awakening Ink: City Archives": (441, LocType.PICKUP_ITEM),
        "Sakura City - Omamori: Intuition": (442, LocType.PICKUP_ITEM),
    }
}