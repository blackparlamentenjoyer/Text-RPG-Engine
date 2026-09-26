import json
from character import Character
from item import Item
from exceptions import SaveNotFoundError, InvalidSaveDataError

def character_to_dict(character):
    dict_character = {
        "name": character.name,
        "class": character.character_class,

        "health": character.health,
        "mana": character.mana,

        "strength": character.strength,
        "defense": character.defense,
        "level": character.level,
        "experience": character.experience,
        "max_experience": character.max_experience,
        "gold": character.gold,
        "max_health": character.max_health,
        "max_mana": character.max_mana,

        "statistics" : statistics_to_dict(character.statistics),
        "inventory": inventory_to_list(character.inventory)
    }

    return dict_character

def statistics_to_dict(statistics):
    dict_statistics = {
        "enemies_killed" : statistics.enemies_killed,
        "bosses_killed" : statistics.bosses_killed,
        "rooms_completed" : statistics.rooms_completed,
        "gold_earned" : statistics.gold_earned,
        "damage_taken" : statistics.damage_taken
    }
    return dict_statistics

def item_to_dict(item):
    dict_item = {
        "name": item.name,
        "item_type": item.item_type,
        "value" : item.value,
        "effect_value" : item.effect_value,
    }
    return dict_item

def inventory_to_list(inventory):
    list_inventory = []
    for item in inventory.items:
        list_inventory.append(item_to_dict(item))

    return list_inventory






def save_character(character):
    character_data = character_to_dict(character)
    with open("save.json", "w", encoding="utf-8") as file:
        json.dump(character_data, file, indent=4, ensure_ascii=False)


def load_save_data():
    try:
        with open("save.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise SaveNotFoundError
    except json.JSONDecodeError:
        raise InvalidSaveDataError


def restore_statistics(character, statistics_data):
    char_stat = character.statistics
    char_stat.enemies_killed = statistics_data["enemies_killed"]
    char_stat.bosses_killed = statistics_data["bosses_killed"]
    char_stat.rooms_completed = statistics_data["rooms_completed"]
    char_stat.gold_earned = statistics_data["gold_earned"]
    char_stat.damage_taken = statistics_data["damage_taken"]

def dict_to_item(item_data):
    item = Item(item_data["name"], item_data["item_type"], item_data["value"], item_data["effect_value"])
    return item

def restore_inventory(character, inventory_data):
    for item_data in inventory_data:
        item = dict_to_item(item_data)
        character.inventory.add_item(item)



def dict_to_character(data):
    character = Character(data["name"], data["class"], data["strength"], data["defense"], data["max_health"], data["max_mana"])
    character.health = data["health"]
    character.mana = data["mana"]
    character.gold = data["gold"]
    character.level = data["level"]
    character.experience = data["experience"]
    character.max_experience = data["max_experience"]
    restore_statistics(character, data["statistics"])
    restore_inventory(character, data["inventory"])
    return character
