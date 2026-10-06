def take_charger(charging_taken,inventory,moves):
    if charging_taken:
        print("Вы уже забрали зарядку")
    else:
        charging_taken = True
        inventory.append("Зарядка")
        moves-=1
        print("Вы забрали зарядку.")
    return charging_taken,inventory,moves
def use_charger(inventory,energy,moves):
    if "Зарядка" not in inventory:
        print("У вас нет зарядки.")
        return inventory,energy,moves
    inventory.remove("Зарядка")
    energy+=3
    if energy>6:
        energy=6
    moves-=1
    print("Вы использовали зарядку.")
    print("Энергия восстановлена")
    return inventory,energy,moves
def show_status(energy,moves,errors_fixed,clue):
    print()
    print("----- СТАТУС -----")
    print("Энергия:", energy)
    print("Ходы:", moves)
    if clue:
        print("Улики: Код доступа: EKEB")
    else:
        print("Улик нет.")
    if inventory:
        print("Инвентарь:", inventory)
    else:
        print("Инвентарь пуст.")
    if errors_fixed:
        print("Исправленные ошибки:", errors_fixed)
    else:
        print("Ошибки ещё не исправлены.")
    print("------------------")
