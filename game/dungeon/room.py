class Room:
    def __init__(self, room_type, enemy=None):
        self.room_type = room_type
        self.enemy = enemy
        self.is_completed = False

    def complete_room(self):
        if self.enemy is None or not self.enemy.is_alive():
            self.is_completed = True

    def describe_room(self):
        print('== == == == == == == == == ==')
        print('           Room              ')

        print('Тип комнаты: ', self.room_type)
        if self.enemy is not None:
            print('Противник: ', self.enemy.name)
        else:
            print('Противника нет')
        print('Пройдена ли комната?: ', self.is_completed)

        print('== == == == == == == == == ==')

