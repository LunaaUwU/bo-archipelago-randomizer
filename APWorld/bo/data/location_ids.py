from enum import Enum

class LocType(Enum):
    KODAMA = "kodama"
    QUEST = "quest"
    BOSS = "boss" 
    OMAMORI = "omamori"
    OMAMORI_STRAP = "omamori_strap"
    DARUMA = "daruma"
    AWAKENING_INK = "awakening_ink"
    LOTUS_SEED = "lotus_seed"
    KETTLE_UPGRADES = "kettle_upgrades"
    HEALTH_UPGRADES = "health_upgrades"
    STAFF_UPGRADES = "staff_upgrades"
    SKILL = "skill"

LOCATIONS_BY_REGION: dict[str, dict[str, tuple[int, LocType]]] = {
    # CBF IDS -> 100-199
    "crimson_bamboo_forest": {
        "Crimson Bamboo Forest - Kodama: Start": (100, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama: On Ledge Left": (101, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama: Hidden": (102, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama: On Ledge Right": (103, LocType.KODAMA),
        "Crimson Bamboo Forest - Kodama: Left Dash": (104, LocType.KODAMA),
        "Crimson Bamboo Forest - Quest: Bamboo Bulk-Up": (105, LocType.QUEST),
        "Crimson Bamboo Forest - Quest: Rozu's Requiem": (106, LocType.QUEST),
        "Crimson Bamboo Forest - Boss: Kira Kira Bozu": (107, LocType.BOSS),
        "Crimson Bamboo Forest - Omamori: Confidence": (108, LocType.OMAMORI),
        "Crimson Bamboo Forest - Omamori: Progress": (109, LocType.OMAMORI),
        "Crimson Bamboo Forest - Skill: Bamboo Bat": (110, LocType.SKILL)
    },
    # UC IDS -> 200-299
    "uzumaki_cave": {
        "Uzumaki Cave - Kodama: Start": (200, LocType.KODAMA),
        "Uzumaki Cave - Kodama: Start South": (201, LocType.KODAMA),
        "Uzumaki Cave - Kodama: Hidden West": (202, LocType.KODAMA),
        "Uzumaki Cave - Kodama: South East": (203, LocType.KODAMA),
        "Uzumaki Cave - Kodama: After Arena Armapillo": (204, LocType.KODAMA),
        "Uzumaki Cave - Quest: Armapillo Assembly": (205, LocType.QUEST),
        "Uzumaki Cave - Quest: Eye Of The Beast": (206, LocType.QUEST),
        "Uzumaki Cave - Boss: Particulary Unmanageable Armapillo": (207, LocType.BOSS),
        "Uzumaki Cave - Omamori: Prosperity": (208, LocType.OMAMORI),
        "Uzumaki Cave - Omamori Strap: Dodomeki Shop": (209, LocType.OMAMORI_STRAP),
        "Uzumaki Cave - Daruma: Chomper": (210, LocType.DARUMA),
        "Uzumaki Cave - Skill: Lotus Dash": (211, LocType.SKILL)
    },
    # SB IDS -> 300-399
    "sencho_bridge": {
        "Sencho Bridge - Boss: Hashihime": (300, LocType.BOSS),
        "Sencho Bridge - Daruma: Pyro-Kun": (301, LocType.DARUMA),
        "Sencho Bridge - Awakening Ink: Defeat Hashihime": (302, LocType.AWAKENING_INK)
    },
    # SC IDS -> 400-499
    "sakura_city": {
        "Sakura City - Kodama: Start Bush": (400, LocType.KODAMA),
        "Sakura City - Kodama: Top of City Archives": (401, LocType.KODAMA),
        "Sakura City - Quest: Vermillion Stranger": (402, LocType.QUEST),
        "Sakura City - Quest: A Daruma's Destiny": (403, LocType.QUEST),
        "Sakura City - Boss: Gashadokuro": (404, LocType.BOSS),
        "Sakura City - Omamori: Health": (405, LocType.OMAMORI),
        "Sakura City - Omamori: Resilience": (406, LocType.OMAMORI),
        "Sakura City - Omamori: Refinement": (407, LocType.OMAMORI),
        "Sakura City - Omamori: Innovation": (408, LocType.OMAMORI),
        "Sakura City - Omamori: Stability": (409, LocType.OMAMORI),
        "Sakura City - Omamori: Favor": (410, LocType.OMAMORI),
        "Sakura City - Omamori: Optimism": (411, LocType.OMAMORI),
        "Sakura City - Omamori: Providence": (412, LocType.OMAMORI),
        "Sakura City - Omamori: Intuition": (413, LocType.OMAMORI),
        "Sakura City - Omamori Strap: Shrine of the Lillies": (414, LocType.OMAMORI_STRAP),
        "Sakura City - Omamori Strap: Fox Couple's House": (415, LocType.OMAMORI_STRAP),
        "Sakura City - Daruma: Jingu": (416, LocType.DARUMA),
        "Sakura City - Daruma: Ken": (417, LocType.DARUMA),
        "Sakura City - Daruma: Mamori": (418, LocType.DARUMA),
        "Sakura City - Daruma: Chomper Two Eyes": (419, LocType.DARUMA),
        "Sakura City - Daruma: Pyro-Kun Two Eyes": (420, LocType.DARUMA),
        "Sakura City - Daruma: Ken Two Eyes": (421, LocType.DARUMA),
        "Sakura City - Daruma: Jingu Two Eyes": (422, LocType.DARUMA),
        "Sakura City - Daruma: Toge-Chan Two Eyes": (423, LocType.DARUMA),
        "Sakura City - Daruma: Mamori Two Eyes": (424, LocType.DARUMA),
        "Sakura City - Daruma: Yuki Two Eyes": (425, LocType.DARUMA),
        "Sakura City - Daruma: Kaboomaru Two Eyes": (426, LocType.DARUMA),
        "Sakura City - Awakening Ink: City Archives": (427, LocType.AWAKENING_INK),
        "Sakura City - Awakening Ink: Daruma Shop": (428, LocType.AWAKENING_INK),
        "Sakura City - Lotus Seed: Sumo Pagoda": (429, LocType.LOTUS_SEED),
        "Sakura City - Kettle Upgrade: Saijo Sip": (430, LocType.KETTLE_UPGRADES),
        "Sakura City - Kettle Upgrade: Fusen Fil": (431, LocType.KETTLE_UPGRADES),
        "Sakura City - Kettle Upgrade: Ocha Oasis": (432, LocType.KETTLE_UPGRADES),
        "Sakura City - Kettle Upgrade: Kanpai Capacity": (433, LocType.KETTLE_UPGRADES),
        "Sakura City - Kettle Upgrade: Surging Tsunami": (434, LocType.KETTLE_UPGRADES),
        "Sakura City - Health Upgrade: Lotus Ramen": (435, LocType.HEALTH_UPGRADES),
        "Sakura City - Health Upgrade: Teal Ramen": (436, LocType.HEALTH_UPGRADES),
        "Sakura City - Health Upgrade: Crystal Ramen": (437, LocType.HEALTH_UPGRADES),
        "Sakura City - Health Upgrade: Silky Smooth Ramen": (438, LocType.HEALTH_UPGRADES),
        "Sakura City - Health Upgrade: Spicy Ramen": (439, LocType.HEALTH_UPGRADES),
        "Sakura City - Staff Upgrade: Staff Upgrade 1": (440, LocType.STAFF_UPGRADES),
        "Sakura City - Staff Upgrade: Staff Upgrade 2": (441, LocType.STAFF_UPGRADES),
        "Sakura City - Staff Upgrade: Staff Upgrade 3": (442, LocType.STAFF_UPGRADES),
    },
    # MF IDS -> 500-599
    "midori_forest": {
        "Midori Forest - Kodama: Senbiki Okami": (500, LocType.KODAMA),
        "Midori Forest - Kodama: Middle Room Grapple": (501, LocType.KODAMA),
        "Midori Forest - Kodama: Big Room": (502, LocType.KODAMA),
        "Midori Forest - Kodama: Big Room Right": (503, LocType.KODAMA),
        "Midori Forest - Kodama: Start": (504, LocType.KODAMA),
        "Midori Forest - Kodama: Tall Room East": (505, LocType.KODAMA),
        "Midori Forest - Quest: Monk's Melody": (506, LocType.QUEST),
        "Midori Forest - Quest: Bunny Blossom Bouquet": (507, LocType.QUEST),
        "Midori Forest - Quest: The Fox Wedding": (508, LocType.QUEST),
        "Midori Forest - Boss: Kitsura": (509, LocType.BOSS),
        "Midori Forest - Omamori: Vitality": (510, LocType.OMAMORI),
        "Midori Forest - Omamori: Focus": (511, LocType.OMAMORI),
        "Midori Forest - Omamori: Poise": (512, LocType.OMAMORI),
        "Midori Forest - Omamori: Composure": (513, LocType.OMAMORI),
        "Midori Forest - Omamori: Deliberation": (514, LocType.OMAMORI),
        "Midori Forest - Omamori: Ingenuity": (515, LocType.OMAMORI),
        "Midori Forest - Omamori: Potency": (516, LocType.OMAMORI),
        "Midori Forest - Daruma: Toge-Chan": (517, LocType.DARUMA),
        "Midori Forest - Daruma: Kaboomaru": (518, LocType.DARUMA),
        "Midori Forest - Awakening Ink: Defeat Kitsura": (519, LocType.AWAKENING_INK),
        "Midori Forest - Lotus Seed: Fox Wedding Fumie": (520, LocType.LOTUS_SEED),
        "Midori Forest - Skill: Grappling Gun": (521, LocType.SKILL)
    },
    # MM IDS -> 600-699
    "megumi_mountain": {
        "Megumi Mountain - Kodama: Kamaitachi": (600, LocType.KODAMA),
        "Megumi Mountain - Kodama: Wind": (601, LocType.KODAMA),
        "Megumi Mountain - Kodama: Flying Sumo Kabuto Training": (602, LocType.KODAMA),
        "Megumi Mountain - Kodama: Wind North West": (603, LocType.KODAMA),
        "Megumi Mountain - Kodama: Start": (604, LocType.KODAMA),
        "Megumi Mountain - Quest: Finesse Of The Flame": (605, LocType.QUEST),
        "Megumi Mountain - Quest: Gyoji's Gunbai": (606, LocType.QUEST),
        "Megumi Mountain - Quest: Moro's Missing Monkeys": (607, LocType.QUEST),
        "Megumi Mountain - Boss: Yokozuna": (608, LocType.BOSS),
        "Megumi Mountain - Omamori: Vigor": (609, LocType.OMAMORI),
        "Megumi Mountain - Omamori: Abundance": (610, LocType.OMAMORI),
        "Megumi Mountain - Omamori: Finesse": (611, LocType.OMAMORI),
        "Megumi Mountain - Omamori: Proficiency": (612, LocType.OMAMORI),
        "Megumi Mountain - Omamori: Fortitude": (613, LocType.OMAMORI),
        "Megumi Mountain - Omamori: Efficiency": (614, LocType.OMAMORI),
        "Megumi Mountain - Omamori: Ambition": (615, LocType.OMAMORI),
        "Megumi Mountain - Omamori Strap: Shop": (616, LocType.OMAMORI_STRAP),
        "Megumi Mountain - Daruma: Yuki": (617, LocType.DARUMA),
        "Megumi Mountain - Lotus Seed: Flying Sumo Kabuto Training": (618, LocType.LOTUS_SEED),
        "Megumi Mountain - Awakening Ink: Defeat Yokozuna": (619, LocType.AWAKENING_INK),
        "Megumi Mountain - Skill: Kabuto Wings": (620, LocType.SKILL)
    },
    # KB IDS -> 700-799
    "kitsune_burrows": {
        "Kitsune Burrows - Kodama: After Tsuki Dash Behind Rock": (700, LocType.KODAMA),
        "Kitsune Burrows - Kodama: Pest Clearing Quest Room": (701, LocType.KODAMA),
        "Kitsune Burrows - Kodama: Around Mimics East": (702, LocType.KODAMA),
        "Kitsune Burrows - Kodama: Above Tea Set": (703, LocType.KODAMA),
        "Kitsune Burrows - Kodama: Guarded by Spiders North": (704, LocType.KODAMA),
        "Kitsune Burrows - Kodama: Mochi Mallet Drop West": (705, LocType.KODAMA),
        "Kitsune Burrows - Kodama: South East": (706, LocType.KODAMA),
        "Kitsune Burrows - Quest: Into the Breach of the Burrows": (707, LocType.QUEST),
        "Kitsune Burrows - Quest: Kitane's Crystals": (708, LocType.QUEST),
        "Kitsune Burrows - Boss: Jorogumo": (709, LocType.BOSS),
        "Kitsune Burrows - Omamori: Punctuality": (710, LocType.OMAMORI),
        "Kitsune Burrows - Omamori: Perseverance": (711, LocType.OMAMORI),
        "Kitsune Burrows - Omamori: Gravitas": (712, LocType.OMAMORI),
        "Kitsune Burrows - Omamori Strap: After Jorogumo": (713, LocType.OMAMORI_STRAP),
        "Kitsune Burrows - Awakening Ink: After Jorogumo": (714, LocType.AWAKENING_INK),
        "Kitsune Burrows - Lotus Seed: North East Hidden Room": (715, LocType.LOTUS_SEED),
        "Kitsune Burrows - Skill: Tsuki Dash": (716, LocType.SKILL),
        "Kitsune Burrows - Skill: Mochi Mallet": (717, LocType.SKILL)
    },
    # ICS IDS -> 800-899
    "ice_caverns": {
        "Ice Caverns - Kodama: Start West Climb": (800, LocType.KODAMA),
        "Ice Caverns - Kodama: East Climb Middle": (801, LocType.KODAMA),
        "Ice Caverns - Kodama: East Climb Hidden Vermillion Stranger": (802, LocType.KODAMA),
        "Ice Caverns - Kodama: East Climb Top": (803, LocType.KODAMA),
        "Ice Caverns - Quest: Trial of the Tengu": (804, LocType.QUEST),
        "Ice Caverns - Quest: The Kitsune Kifuda": (805, LocType.QUEST),
        "Ice Caverns - Quest: Fragile Egg": (806, LocType.QUEST),
        "Ice Caverns - Boss: Tengu Solo": (807, LocType.BOSS),
        "Ice Caverns - Boss: Tengu Duo": (808, LocType.BOSS),
        "Ice Caverns - Boss: Tengu Trio": (809, LocType.BOSS),
        "Ice Caverns - Omamori: Serenity": (810, LocType.OMAMORI),
        "Ice Caverns - Omamori: Elegance": (811, LocType.OMAMORI),
        "Ice Caverns - Omamori Strap: After Tengu Duo": (812, LocType.OMAMORI_STRAP),
        "Ice Caverns - Awakening Ink: After Tengu Duo": (813, LocType.AWAKENING_INK),
        "Ice Caverns - Lotus Seed: After Tengu Solo": (814, LocType.LOTUS_SEED),
        "Ice Caverns - Skill: Ice Picks": (815, LocType.SKILL)
    },
    # IC IDS -> 900-999
    "imperial_castle": {
        "Imperial Castle - Boss: Sakura Shogun": (900, LocType.BOSS)
    }
}