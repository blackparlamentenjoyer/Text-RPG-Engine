import random
from game.models.enemy import Enemy

enemies = {
    1: {'name': 'Skeleton', 'strength': 5, 'defense': 0, 'max_health' : 50, 'experience_reward': 10, 'gold_reward': 5},
    2: {'name': 'Goblin', 'strength': 10, 'defense': 5, 'max_health': 100, 'experience_reward': 25, 'gold_reward': 15},
    3: {'name': 'Orc', 'strength': 20, 'defense': 0, 'max_health': 200, 'experience_reward': 50, 'gold_reward': 30}
}

def generate_enemy():
    raw_enemy = random.choice(list(enemies.values()))

    generated_enemy = Enemy(raw_enemy['name'], raw_enemy['strength'], raw_enemy['defense'], raw_enemy['max_health'], raw_enemy['experience_reward'], raw_enemy['gold_reward'])

    return generated_enemy

