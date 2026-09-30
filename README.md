# Text RPG Engine

## Description: 
Text RPG Engine is a console RPG written in Python. The project was created to practice Python Core, OOP and more advanced Python concepts.

## Features: 
- **Combat** - 1v1 turn-based battles
- **Skills** - unique skills for each character class
- **Dungeon** - simple dungeon system with rooms
- **Enemies/Boss** - random enemies and a final boss 
- **Inventory** - make possible earn loot
- **Loot** - give you some buff
- **Events** - can heal/damage you or give you gold
- **XP/Levels** - increase your stats
- **Statistics** - kills, bosses, completed rooms, earned gold, received damage, etc.
- **JSON-based save and load system** - simple save/load system, save.json in root-directory

## Project Structure:
    Text-RPG-Engine/
    ├── main.py
    ├── game/
    │   ├── models/
    │   │   ├── character.py
    │   │   ├── enemy.py
    │   │   ├── equipment.py
    │   │   ├── inventory.py
    │   │   ├── item.py
    │   │   └── statistics.py 
    │   ├── combat/
    │   │   └── combat.py
    │   ├── dungeon/
    │   │   ├── dungeon.py
    │   │   └── room.py
    │   ├── services/
    │   │   ├── boss_generator.py
    │   │   ├── character_factory.py
    │   │   ├── enemy_generator.py
    │   │   ├── event.py
    │   │   ├── loot.py
    │   │   └── merchant.py
    │   ├── storage/
    │   │   └── save_manager.py
    │   ├── exceptions/
    │   │   └── exceptions.py
    │   ├── utils/
    │   │   └── decorators.py
    │   └── core/
    │       └── game.py
    └── README.md
- models - python classes for game entities
- combat - combat system
- dungeon - dungeon's rooms generation and dungeon complete system
- services - enemies, loot, event generation and character building
- storage - save/load system and validators
- exceptions - custom exceptions
- utils - python decorators
- core - main game logic
- root - entry point and main menu
## Technologies
- Python 3

- Python Standard Library

- Object-Oriented Programming

- JSON serialization and deserialization

- Python logging

- pathlib for file path handling

- Type hints

## Installation
**Requirements: Python3, Git**
```
git clone https://github.com/blackparlamentenjoyer/Text-RPG-Engine
cd Text-RPG-Engine
python main.py
```
## Usage
- After installing and starting game - menu appears.
- Player can choose: New game or Load game.
- If new game - create character(name,class).
- After menu - player starts completing dungeon.
- The game is controlled through console input.

## Save System
The game uses a JSON-based save system.

- Character state is stored in save.json.

- Health, mana, attributes, level, experience, gold, statistics, and inventory are persisted.

- Save data is validated before a Character object is restored.

- Invalid field types and values are rejected.

- Invalid inventory data is detected before restoration.

- Missing or corrupted save files are handled using custom exceptions.

- The save file path is resolved with pathlib, so saving and loading do not depend on the current working directory.
## Logging
The project uses Python's built-in logging module.

Runtime information and important events are written to game.log, including game startup, character creation, save/load operations, combat-related function calls, errors, and other relevant events.

The log file path is resolved independently of the current working directory.

## What I Learned

This project was created as a practical Python Core project. During development, I practiced:

- Object-oriented programming and composition

- Classes and object state management

- Modules and packages

- Project structure and separation of responsibilities

- Dependency direction and avoiding circular imports

- Custom exceptions and error handling

- JSON serialization and deserialization

- Save data validation

- Type hints

- Generators and yield

- Decorators, *args, **kwargs, and functools.wraps

- Context managers

- Logging

- File and path handling with pathlib

- __name__ == "__main__"

- Edge-case handling

- Git and GitHub workflow

The project uses only the Python Standard Library and was built to strengthen Python fundamentals before moving to concurrency, networking, databases, and backend development.
