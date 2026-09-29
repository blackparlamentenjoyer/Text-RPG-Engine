from game.models.inventory import Inventory
from game.models.statistics import Statistics

class Character:

    def __init__(self, name, character_class, strength, defense, max_health, max_mana):
        self.name = name
        self.character_class = character_class

        self.health = max_health
        self.mana = max_mana

        self.strength = strength
        self.defense = defense
        self.level = 1
        self.experience = 0
        self.max_experience = 100
        self.gold = 0
        self.max_health = max_health
        self.max_mana = max_mana

        self.inventory = Inventory(10)
        self.statistics = Statistics()
    def describe_character(self):  #решил сделать так как удобнее
        print('== == == == == == == == == ==')
        print('CHARACTER')

        print('Name: ', self.name)
        print('Class: ', self.character_class)
        print('Level: ', self.level)
        print('Exp: ', self.experience)

        print(f'HP: {self.health} / {self.max_health}')
        print(f'Mana: {self.mana} / {self.max_mana}')

        print('Strength: ', self.strength)
        print('Defense: ', self.defense)

        print('Gold: ', self.gold)
        print('== == == == == == == == == ==')

    def take_damage(self, amount_damage):
        health_before = self.health
        if amount_damage >= 0:
            self.health -= amount_damage
            if self.health <= 0:
                self.health = 0

        health_after = self.health
        stats_health = health_before - health_after
        self.statistics.add_damage_taken(stats_health)
        return self.health

    def heal(self, amount_heal):
        if amount_heal >= 0:
            self.health += amount_heal
            if self.health >= self.max_health:
                self.health = self.max_health
        return self.health

    def spend_mana(self, amount_mana):
        if amount_mana >= 0:
            if self.mana >= amount_mana:
                self.mana -= amount_mana
                return True
            else:
                return False
        else:
            return False

    def restore_mana(self, amount_mana):
        if amount_mana >= 0:
            self.mana += amount_mana
            if self.mana >= self.max_mana:
                self.mana = self.max_mana
        return self.mana

    def add_gold(self, amount_gold):
        if amount_gold >= 0:
            self.gold += amount_gold
            self.statistics.add_gold_earned(amount_gold)
            print(f"Шекелей: {self.gold}")
        return self.gold


    def level_up(self):
        self.level += 1
        match self.character_class:
            case 'Warrior':
                self.max_health += 50
                self.strength += 10
                self.defense += 20
            case 'Mage':
                self.max_health += 10
                self.strength += 30
                self.defense += 1
                self.max_mana += 100
            case 'Archer':
                self.max_health += 25
                self.strength += 15
                self.defense += 5
                self.max_mana += 25
        self.health = self.max_health
        self.mana = self.max_mana
        print(f"Братюнь ты достиг нового левела! Здоровье и мана восстановлены, статы улучшились")
        self.describe_character()


    def add_experience(self, amount_experience):
        if amount_experience >= 0:
            self.experience += amount_experience
            if self.experience <= self.max_experience:
                print(f"Exp: {self.experience} / {self.max_experience}")
            while self.experience >= self.max_experience:
                self.experience -= self.max_experience
                self.level_up()



    def spend_gold(self, amount_gold):
        if amount_gold >= 0:
            if self.gold >= amount_gold:
                self.gold -= amount_gold
                return True
            else:
                return False
        else:
            return False

    def is_alive(self):
        return self.health > 0

    def use_skill(self):
        match self.character_class:
            case 'Warrior':
                print(f"{self.name} использует способность Power Strike")
                skill_damage = [self.strength * 2]
                return skill_damage
            case 'Mage':
                if self.spend_mana(30):
                    print(f"{self.name} использует способность Fireball")
                    skill_damage = [self.strength * 3]
                    return skill_damage
                else:
                    return None
            case 'Archer':
                if self.spend_mana(15):
                    print(f"{self.name} использует способность Double Shot")
                    skill_damage = [self.strength, self.strength]
                    return skill_damage
                else:
                    return None



