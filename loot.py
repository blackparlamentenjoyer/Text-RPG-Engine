import random
from item import Item

items = {
    1: {'name': 'Ножик', 'item_type': "Weapon", 'value': 50, 'effect_value' : 0},
    2: {'name': 'Найк худак', 'item_type': "Armor", 'value': 50, 'effect_value' : 0},
    3: {'name': 'Эсса 0.5', 'item_type': 'Potion', 'value': 25, 'effect_value' : 50}
}

def generate_loot() -> Item | None:
    raw_item = random.choice(list(items.values()))

    generated_item = Item(raw_item['name'], raw_item['item_type'], raw_item['value'], raw_item['effect_value'])

    drop_chance = random.randint(1,2)

    if drop_chance == 1:
        return generated_item
    else:
        return None