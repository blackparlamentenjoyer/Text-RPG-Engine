class Item:
    def __init__(self, name, item_type, value, effect_value=None):
        self.name = name
        self.item_type = item_type
        self.value = value
        self.effect_value = effect_value

    def describe_item(self):
        print('         ')
        print('Предмет: ', self.name)
        print('Тип: ', self.item_type)
        print(f'Стоимость: {self.value} золота')
        print('Эффект: ', self.effect_value)
        print('           ')



