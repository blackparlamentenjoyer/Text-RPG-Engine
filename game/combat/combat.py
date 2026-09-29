from game.utils.decorators import log_call

def damage_calculator(amount_strength, amount_defense):
    amount_damage = amount_strength
    if amount_damage > amount_defense:
        amount_damage -= amount_defense
        return amount_damage
    else:
        amount_damage = 1
    return amount_damage
@log_call
def combat(character, enemy):
    character_damage = damage_calculator(character.strength, enemy.defense)
    enemy_damage = damage_calculator(enemy.strength, character.defense)
    warrior_skill_flag = False
    print("================COMBAT================")
    print(f"{character.name} VS {enemy.name}")
    print("======================================")
    while character.is_alive() and enemy.is_alive():
        while True:
            print("Выберите действие: ")
            print("1. Атаковать")
            print("2. Использовать способность")
            player_choice = input()
            match player_choice:
                case '1':
                    enemy.take_damage(character_damage)
                    print(f"{character.name} атакует {enemy.name}, нанося {character_damage} урона!")
                    print(f"{enemy.name} HP: {enemy.health}/{enemy.max_health}")
                    break
                case '2':
                    if character.character_class == "Warrior" and warrior_skill_flag:
                        print("Ты не можешь использовать эту способность больше 1 раза за бой!")
                        continue
                    else:
                        character_skill_damage = character.use_skill()
                        if character_skill_damage is not None:
                            for i in character_skill_damage:
                                skill_damage = damage_calculator(i, enemy.defense)
                                enemy.take_damage(skill_damage)
                                print(f"{character.name} атакует {enemy.name}, нанося {skill_damage} урона!")
                                print(f"{enemy.name} HP: {enemy.health}/{enemy.max_health}")
                                if not enemy.is_alive():
                                    break
                            if character.character_class == "Warrior":
                                warrior_skill_flag = True
                            break
                        else:
                            print("Недостаточно маны!")
                            continue
                case _:
                    print("Неправильный ввод")
                    continue

        if enemy.is_alive():
            character.take_damage(enemy_damage)
            print(f"{enemy.name} атакует {character.name}, нанося {enemy_damage} урона!")
            print(f"{character.name} HP: {character.health}/{character.max_health}")
            if character.is_alive():
                continue
            else:
                print(f"{character.name} погиб! Вы проиграли:(")
                break
        else:
            print(f"{enemy.name} повержен!")
            character.add_experience(enemy.experience_reward)
            character.add_gold(enemy.gold_reward)
            break



