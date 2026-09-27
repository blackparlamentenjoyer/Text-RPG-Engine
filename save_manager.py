import json
import logging

import character
from character import Character
from item import Item
from exceptions import SaveNotFoundError, InvalidSaveDataError


logger = logging.getLogger(__name__)

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
    logger.info(f"Character {character.name} successfully saved")


def load_save_data():
    try:
        with open("save.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.warning(f"Не удалось найти файл save.json: отсутствует JSON")
        raise SaveNotFoundError
    except json.JSONDecodeError:
        logger.exception("Не удалось прочитать save.json: повреждён JSON")
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

def validate_save_data(data):
    required_keys = ["name", "class", "health", "mana", "strength", "defense", "level", "experience", "max_experience", "gold", "max_health", "max_mana", "statistics", "inventory"]
    if not isinstance(data, dict):
        raise InvalidSaveDataError
    for key in required_keys:
        if key not in data:
            raise InvalidSaveDataError
    if not isinstance(data["name"], str) or not isinstance(data["class"], str):
        raise InvalidSaveDataError
    numeric_keys = ["health", "mana", "strength", "defense", "level", "experience", "max_experience", "gold", "max_health", "max_mana"]
    for key in numeric_keys:
        if not isinstance(data[key], int):
            raise InvalidSaveDataError
    for key in numeric_keys:
        if data[key] < 0:
            raise InvalidSaveDataError
    if data["level"] < 1:
        raise InvalidSaveDataError
    if data["max_experience"] <= 0:
        raise InvalidSaveDataError
    validate_statistics_data(data["statistics"])
    validate_inventory_data(data["inventory"])
    if data["name"].strip() == "":
        raise InvalidSaveDataError
    valid_classes = ["Warrior",  "Mage", "Archer"]
    if data["class"] not in valid_classes:
        raise InvalidSaveDataError
    if data["health"] > data["max_health"]:
        raise InvalidSaveDataError
    if data["mana"] > data["max_mana"]:
        raise InvalidSaveDataError

def validate_statistics_data(statistics_data):
    stat_keys = ["enemies_killed", "bosses_killed", "rooms_completed", "gold_earned", "damage_taken"]
    if not isinstance(statistics_data, dict):
        raise InvalidSaveDataError
    for key in stat_keys:
        if key not in statistics_data:
            raise InvalidSaveDataError
        if not isinstance(statistics_data[key], int):
            raise InvalidSaveDataError
        if statistics_data[key] < 0:
            raise InvalidSaveDataError

def validate_item_data(item_data):
    item_keys_str = ["name", "item_type"]
    item_keys = item_keys_str + ["value", "effect_value"]
    if not isinstance(item_data, dict):
        raise InvalidSaveDataError
    for key in item_keys:
        if key not in item_data:
            raise InvalidSaveDataError
    for key_str in item_keys_str:
        if not isinstance(item_data[key_str], str):
            raise InvalidSaveDataError
        if item_data[key_str].strip() == "":
            raise InvalidSaveDataError

    if not isinstance(item_data["value"], int):
        raise InvalidSaveDataError
    if item_data["value"] < 0:
        raise InvalidSaveDataError

    if item_data["effect_value"] is not None:
        if not isinstance(item_data["effect_value"], int) or item_data["effect_value"] < 0:
            raise InvalidSaveDataError

def validate_inventory_data(inventory_data):
    if not isinstance(inventory_data, list):
        raise InvalidSaveDataError
    for item in inventory_data:
        validate_item_data(item)



