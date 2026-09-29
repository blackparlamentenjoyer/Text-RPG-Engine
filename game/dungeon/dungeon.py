import random

from game.services.boss_generator import generate_boss
from game.services.enemy_generator import generate_enemy
from game.dungeon.room import Room

room_types = ['Enemy', 'Empty', 'Event']
boss_room = 'Boss'

class Dungeon:
    def __init__(self):
        self.rooms = []
        self.current_room_index = 0

    def add_room(self, room):
        self.rooms.append(room)

    def describe_dungeon(self):
        print("=============Dungeon==============")
        for index, room in enumerate(self.rooms, start=1):
            print(f'Комната {index}: {room.room_type}')
        print("==================================")

    def generate_dungeon(self, amount: int) -> None:
        self.rooms = []
        self.current_room_index = 0
        if amount > 0:
            for i in range(amount-1):
                raw_choice = random.choice(room_types)
                if raw_choice == 'Empty':
                    self.add_room(Room('Empty'))
                elif raw_choice == 'Enemy':
                    self.add_room(Room('Enemy', generate_enemy()))
                elif raw_choice == 'Event':
                    self.add_room(Room('Event'))
            self.add_room(Room(boss_room, generate_boss()))

    def get_current_room(self) -> Room | None:
        if self.current_room_index <= len(self.rooms) - 1:
            return self.rooms[self.current_room_index]
        else:
            return None

    def move_to_next_room(self):
        room = self.get_current_room()
        if room is not None and room.is_completed:
            self.current_room_index += 1




    def iter_rooms(self):
        for room in self.rooms:
            yield room

