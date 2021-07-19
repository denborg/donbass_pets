from fundamentals import Entity


class BasicPet(Entity):
    def __init__(self):
        super().__init__()
        self.hp_multiplier = 1
        self.health = 100
        self.health_regeneration = 1
        self.attack_damage = 5
        self.critical_multiplier = 1.6
        self.display_name = 'Basic Pet'

    def armor_effect(self):
        armor_effect = 0
        for n in range(self.armor):
            armor_effect += 9 / (1.1667 * (n+1))
        return armor_effect


class Piggy(BasicPet):
    def __init__(self):
        super().__init__()
        self.display_name = 'Шматок сала'


class Pudge(BasicPet):
    def __init__(self):
        super().__init__()
        self.hp_multiplier = 1.5
        self.health_regeneration = 2
        self.attack_damage = 3
        self.display_name = 'Падж'


class RedPanda(BasicPet):
    def __init__(self):
        super().__init__()
        self.evasion_chance = 0.07
        self.critical_chance = 0.1


class FermerStasyan(BasicPet):
    def __init__(self):
        super().__init__()
        self.armor = 3
        self.attack_damage = 2
        self.health_regeneration = 4
        self.display_name = 'Фермер терпила'


# def get_armor_effects(pet):
#     for i in range(61):
#         pet.armor = i
#         effect = pet.armor_effect()
#         print(f'{i} - {effect}')
