class Equipment:
    def __init__(self):
        self.weapon = None
        self.armor = None

    def equip_item(self, item):
        if item.item_type == "Weapon":
            self.weapon = item
            print("Ружбайка экипирована!")
        elif item.item_type == "Armor":
            self.armor = item
            print("Бронька накинута!")
        else:
            print("Ништячок нельзя надеть братан!")

    def show_equipment(self):
        if self.weapon is None:
            print("У тебя нема ружбайки паря:(")
        else:
            self.weapon.describe_item()
        if self.armor is None:
            print("Фу оденься, дрыщ. Броньки нет:(")
        else:
            self.armor.describe_item()

    def unequip_item(self, item):
        if item is self.weapon:
            self.weapon = None
            print("Ты выкинул эту шнягу!")
        elif item is self.armor:
            self.armor = None
            print("Эта фуфайка снята!")
        else:
            print("Ты пытаешься сделать что то не то парняга!")
