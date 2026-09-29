import random
from game.models.enemy import Enemy

bosses = {
    1: {'name': 'Dungeon Lord', 'strength': 35, 'defense': 25, 'max_health' : 300, 'experience_reward': 500, 'gold_reward': 200},
}

def generate_boss():
    raw_boss = random.choice(list(bosses.values()))

    generated_enemy = Enemy(raw_boss['name'], raw_boss['strength'], raw_boss['defense'], raw_boss['max_health'], raw_boss['experience_reward'], raw_boss['gold_reward'])

    return generated_enemy
