class Enemy:

    def __init__(self, name, strength, defense, max_health, experience_reward, gold_reward):
        self.name = name

        self.health = max_health

        self.strength = strength
        self.defense = defense
        self.experience_reward = experience_reward
        self.gold_reward = gold_reward
        self.max_health = max_health

    def describe_enemy(self):
        print('== == == == == == == == == ==')
        print('Enemy')

        print('Name: ', self.name)
        print('Exp reward: ', self.experience_reward)
        print('Gold reward: ', self.gold_reward)

        print(f'HP: {self.health} / {self.max_health}')

        print('Strength: ', self.strength)
        print('Defense: ', self.defense)

        print('== == == == == == == == == ==')


    def take_damage(self, amount):
        if amount >= 0:
            self.health -= amount
            if self.health <= 0:
                self.health = 0
        return self.health

    def heal(self, amount):
        if amount >= 0:
            self.health += amount
            if self.health >= self.max_health:
                self.health = self.max_health
        return self.health

    def is_alive(self):
        return self.health > 0