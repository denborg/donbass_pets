from item import BasicWeapon
from item import BasicArmor
from item import BasicHelmet
from item import BasicSphere
from item import BasicBoots


class HelmetStasa(BasicHelmet):
    def __init__(self):
        super().__init__()
        self.health = 4
        self.health_regeneration = 0.5
        self.display_name = 'WaBka'


class ArmorTomata(BasicArmor):
    def __init__(self):
        super().__init__()
        self.armor = 1
        self.health = 2
        self.hp_multiplier = 0.06
        self.display_name = 'Помидор'


class TapkiDJ(BasicBoots):
    def __init__(self):
        super().__init__()
        self.health = 4
        self.evasion_chance = 0.05
        self.display_name = 'Тапки Диджея'


class AntiHornyClub(BasicWeapon):
    def __init__(self):
        super().__init__()
        self.attack_damage = 3
        self.display_name = 'Anti-horny дубина'


class RedSphere(BasicSphere):
    def __init__(self):
        super().__init__()
        self.critical_chance = 0.05
        self.display_name = 'Сфера жажды крови'


class GreenSphere(BasicSphere):
    def __init__(self):
        super().__init__()
        self.health = 5
        self.display_name = 'Сфера спокойствия'


class BlueSphere(BasicSphere):
    def __init__(self):
        super().__init__()
        self.armor = 1
        self.display_name = 'Сфера терпения'
