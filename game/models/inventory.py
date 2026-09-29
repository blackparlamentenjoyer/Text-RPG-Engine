class Inventory:
    def __init__(self, max_capacity):
        self.items = []
        self.max_capacity = max_capacity


    def use_item(self, item, character):
        if item in self.items:
            if item.item_type == "Potion":
                if character.health < character.max_health:
                    health_before = character.health
                    character.heal(item.effect_value)
                    health_after = character.health
                    amount_healed = health_after - health_before
                    print(f"Братан ты вылечился на {amount_healed} HP")
                    self.remove_item(item)
                else:
                    print("Пацан ты здоров как бык!")
            else:
                print("Братан ты не можешь это попить!")
        else:
            print("Братан у тебя этой шняги нету!")



    def add_item(self, item):
        if len(self.items) < self.max_capacity:
            self.items.append(item)
            print("Предмет добавлен")
        else:
            print("Инвентарь переполнен!")

    def show_inventory(self):
        if len(self.items) != 0:
            print("Инвентарь: ")
            for i in self.items:
                i.describe_item()
        else:
            print("Инвентарь пуст!")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print("Предмет удален")
        else:
            print("Нет такого предмета!")



