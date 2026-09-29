import logging

from game.storage import save_manager
from game.dungeon.dungeon import Dungeon
from game.combat.combat import combat
from game.services.loot import generate_loot
from game.services.event import random_event
from game.exceptions.exceptions import SaveNotFoundError, InvalidSaveDataError
from game.models.character import Character
from game.services.character_factory import create_character

logger = logging.getLogger(__name__)
dungeon_rooms_value = 5

def play_game(character : Character) -> Character:
    dungeon = Dungeon()
    dungeon.generate_dungeon(dungeon_rooms_value)
    while True:
        current_room = dungeon.get_current_room()
        if current_room is None:
            print("Поземелье кончилось")
            break
        print(f"Ты вошел в комнату {dungeon.current_room_index + 1}")
        current_room.describe_room()
        if current_room.room_type == "Enemy":
            combat(character, current_room.enemy)
            if not character.is_alive():
                print("Проиграл")
                logger.warning(f"Персонаж {character.name} погиб в подземелье")
                break
            else:
                character.statistics.add_enemy_kills()
                loot = generate_loot()
                if loot is not None:
                    character.inventory.add_item(loot)
                    print(f"Вам выпал предмет: {loot.name}")

                else:
                    print("Вам ничего не выпало:(")

        elif current_room.room_type == "Boss":
            combat(character, current_room.enemy)
            if not character.is_alive():
                print("Проиграл")
                logger.warning(f"Персонаж {character.name} погиб в подземелье")
                break
            else:
                character.statistics.add_boss_kills()

        elif current_room.room_type == "Event":
            random_event(character)
            if not character.is_alive():
                print("Проиграл")
                logger.warning(f"Персонаж {character.name} погиб в подземелье")
                break

        current_room.complete_room()
        character.statistics.add_room_completes()
        dungeon.move_to_next_room()

    character.statistics.show_statistics()
    save_manager.save_character(character)
    return character

def new_game(character_name, character_class) -> None:
    character = create_character(character_name, character_class)
    character.describe_character()
    play_game(character)

def load_game() -> None:
    try:
        character_data = save_manager.load_save_data()
        save_manager.validate_save_data(character_data)
    except SaveNotFoundError:
        print("Файл сохранения не найден!")
        return
    except InvalidSaveDataError:
        print("Файл сохранения поврежден!")
        return
    loaded_character = save_manager.dict_to_character(character_data)
    logger.info(f"Загружен персонаж {loaded_character.name}")
    play_game(loaded_character)