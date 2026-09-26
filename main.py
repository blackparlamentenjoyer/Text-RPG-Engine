from exceptions import SaveNotFoundError, InvalidSaveDataError
from character import Character
from dungeon import Dungeon
from combat import combat
from loot import generate_loot
from event import random_event
import save_manager

dungeon_rooms_value = 5 #для удобства вынес жесть

def menu():
    print("======================")
    print("      TEXT RPG        ")
    print("======================")

    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

def choice_menu_option():
    option = input("Выберите опцию: ")
    if option == "1":
        new_game()
        return False
    elif option == "2":
        load_game()
        return False
    elif option == "3":
        print("Goodbye")
        return True
    else:
        print("Please enter a valid option")
        return False

def character_name_choice():
    while True:
        raw_character_name = input("Назовите персонажа: ")
        character_name = raw_character_name.strip()
        if character_name == "":
            continue
        else:
            break
    return character_name

def character_class_choice():
    print("Выберите класс персонажа")
    print("1. Warrior  2. Mage  3. Archer")
    while True:
        choice = input()
        match choice:
            case "1":
                character_class = "Warrior"
                break
            case "2":
                character_class = "Mage"
                break
            case "3":
                character_class = "Archer"
                break
            case _:
                print("Please enter a valid option")
                continue
    return character_class

def create_character(character_name, character_class):
    match character_class:
        case "Warrior":
            character = Character(character_name, character_class, 100, 5, 200, 0)
        case "Mage":
            character = Character(character_name, character_class, 30, 10, 50, 500)
        case "Archer":
            character = Character(character_name, character_class, 15, 15, 100, 50)
    return character


def new_game():
    character_name = character_name_choice()
    character_class = character_class_choice()
    character = create_character(character_name, character_class)
    character.describe_character()
    play_game(character)

def load_game():
    try:
        character_data = save_manager.load_save_data()
    except SaveNotFoundError:
        print("Файл сохранения не найден!")
        return
    except InvalidSaveDataError:
        print("Файл сохранения поврежден!")
        return
    loaded_character = save_manager.dict_to_character(character_data)
    play_game(loaded_character)



def play_game(character):
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
                break
            else:
                character.statistics.add_boss_kills()

        elif current_room.room_type == "Event":
            random_event(character)
            if not character.is_alive():
                print("Проиграл")
                break

        current_room.complete_room()
        character.statistics.add_room_completes()
        dungeon.move_to_next_room()

    character.statistics.show_statistics()
    save_manager.save_character(character)
    return character


while True:
    menu()
    should_exit = choice_menu_option()
    if should_exit:
        break






