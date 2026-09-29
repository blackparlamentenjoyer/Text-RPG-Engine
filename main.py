import logging

from pathlib import Path
from game.core.game import new_game, load_game

path = Path(__file__).resolve().parent
log_path = path / "game.log"

logging.basicConfig(level=logging.DEBUG, filename=log_path, filemode='a', encoding='utf-8', format='%(asctime)s | %(name)s | %(levelname)s | %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


def menu() -> None:
    print("======================")
    print("      TEXT RPG        ")
    print("======================")

    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

def choice_menu_option() -> bool:
    option = input("Выберите опцию: ")
    if option == "1":
        new_game(character_name_choice(), character_class_choice())
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

def character_name_choice() -> str:
    while True:
        raw_character_name = input("Назовите персонажа: ")
        character_name = raw_character_name.strip()
        if character_name == "":
            continue
        else:
            break
    return character_name

def character_class_choice() -> str:
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

def main():
    logger.info("Игра началась")
    while True:
        menu()
        should_exit = choice_menu_option()
        if should_exit:
            break

if __name__ == "__main__":
    main()






