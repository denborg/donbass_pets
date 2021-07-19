from enum import Enum
"""
Slots:
helmet - hp hp_regen
armor - low_hp armor hp_multi
boots - hp, evasion
weapon - 1 - 2 - 3 mods (default - uncommon - rare)
sphere1 - 1 mod common (2 very rare)
sphere2 - 1 mod common (2 very rare)
sphere_mods - every mod available
"""


class Rarities(Enum):
    BASIC = 'Basic'
    COMMON = 'Common'
    RARE = 'Rare'
    EPIC = 'Epic'


class BasicItem:
    def __init__(self):
        self.display_name = 'Basic Item'
        self.rarity = Rarities.BASIC


class BasicSphere(BasicItem):
    def __init__(self):
        super().__init__()
        self.hp_multiplier = 0
        self.attack_damage = 0
        self.evasion_chance = 0
        self.health = 0
        self.health_regeneration = 0
        self.armor = 0
        self.critical_multiplier = 0
        self.critical_chance = 0


class BasicHelmet(BasicItem):
    def __init__(self):
        super().__init__()
        self.health = 0
        self.health_regeneration = 0


class BasicArmor(BasicItem):
    def __init__(self):
        super().__init__()
        self.health = 0
        self.armor = 0
        self.hp_multiplier = 0


class BasicBoots(BasicItem):
    def __init__(self):
        super().__init__()
        self.health = 0
        self.evasion_chance = 0


class BasicWeapon(BasicItem):
    def __init__(self):
        super().__init__()
        self.attack_damage = 0
        self.critical_chance = 0
        self.critical_multiplier = 0

