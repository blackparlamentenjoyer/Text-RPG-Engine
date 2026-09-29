class Statistics:
    def __init__(self):
        self.enemies_killed = 0
        self.bosses_killed = 0
        self.rooms_completed = 0
        self.gold_earned = 0
        self.damage_taken = 0

    def add_enemy_kills(self):
        self.enemies_killed += 1

    def add_boss_kills(self):
        self.bosses_killed += 1

    def add_room_completes(self):
        self.rooms_completed += 1

    def add_gold_earned(self, amount):
        if amount >= 0:
            self.gold_earned += amount

    def add_damage_taken(self, amount):
        if amount >= 0:
            self.damage_taken += amount

    def show_statistics(self):
        print("==========Statistics============")
        print(f"Enemies killed: {self.enemies_killed}")
        print(f"Bosses killed: {self.bosses_killed}")
        print(f"Rooms completed: {self.rooms_completed}")
        print(f"Gold earned: {self.gold_earned}")
        print(f"Damage taken: {self.damage_taken}")
        print("================================")