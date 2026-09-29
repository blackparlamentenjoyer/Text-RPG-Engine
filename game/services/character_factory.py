import logging

from game.models.character import Character


logger = logging.getLogger(__name__)


def create_character(character_name: str, character_class: str) -> Character:
    match character_class:
        case "Warrior":
            character = Character(character_name, character_class, 100, 5, 200, 0)
        case "Mage":
            character = Character(character_name, character_class, 30, 10, 50, 500)
        case "Archer":
            character = Character(character_name, character_class, 15, 15, 100, 50)
    logger.info(f"Создан персонаж {character_name} класса {character_class}")
    return character