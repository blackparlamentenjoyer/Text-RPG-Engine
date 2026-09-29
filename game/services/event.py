import random

events = {"Healing Fountain" : 30, "Gold Stash" : 25, "Trap" : 20}

def random_event(character):
    event = random.choice(list(events))
    event_value = events[event]
    match event:
        case "Healing Fountain":
            character.heal(event_value)
            print("Healing Fountain тебя подлечил")
        case "Gold Stash":
            character.add_gold(event_value)
            print("Gold Stash отсыпал тебе монет")
        case "Trap":
            character.take_damage(event_value)
            print("Trap пизданул тебя")

