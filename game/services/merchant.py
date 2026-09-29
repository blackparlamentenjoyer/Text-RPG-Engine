class Merchant:
    def __init__(self, name):
        self.items = []
        self.name = name

    def add_item(self, item):
        self.items.append(item)
        print(f"У торговца появился предмет: {item.name}")


    def show_items(self):
        if len(self.items) != 0:
            print(f"Торговец {self.name}: ")
            for i in self.items:
                i.describe_item()
        else:
            print("У торговца для тебя ничего нет!")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)


    def buy_item(self, character, item):
        if item in self.items and len(character.inventory.items) < character.inventory.max_capacity:
            if character.spend_gold(item.value):
                character.inventory.add_item(item)
                self.remove_item(item)
                print(f"Ты купил эту шнягу: {item.name} за {item.value} злотых!")
            else:
                print("Ты бедняк!")
        elif len(character.inventory.items) >= character.inventory.max_capacity:
            print("Братан у тебя полные карманы!")
        else:
            print("Ты кажется что то не понял!")

    def sell_item(self, character, item):
        if item in character.inventory.items:
            character.inventory.remove_item(item)
            self.add_item(item)
            sell_price = int(item.value * 0.5)
            character.add_gold(sell_price)
            print(f"Ты продал эту шнягу: {item.name} за {sell_price} злотых!")
        else:
            print("У тебя нет этой шмотки!")








