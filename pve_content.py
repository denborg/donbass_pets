from fundamentals import Entity


class BasicBoss(Entity):
    def __init__(self):
        super().__init__()
        self.health = 200
        self.max_pets = 1
        self.health_regeneration = 2
        self.attack_damage = (5, 10)
        self.critical_multiplier = 1.6
        self.display_name = 'Basic Boss'


class AncientToad(BasicBoss):
    def __init__(self):
        super().__init__()
        self.max_pets = 3
        self.health = 250
        self.attack_damage = (10, 15)


class BasicRaid:
    def __init__(self):
        pass


