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
def check_answer(number,answer,clue,errors_fixed):
    answer=answer.strip().lower()
    if number==1:
        if not clue:
            print("Сначало нужно осмотреть стенд.")
            return False
        if answer=="ekeb":
            print("Правильно! Ошибка А исправлена")
            errors_fixed.append("A")
            return True
    if number==2:
        if answer=="120":
            print("Правильно! Ошибка B исправлена.")
            errors_fixed.append("B")
            return True
        else:
            print("Неверный ответ")
            return False
    if number==3:
        if answer=="almaty":
            print("Правильно! Ошибка С исправлена.")
            errors_fixed.append("C")
            return True
        else:
            print("Неверный ответ")
            return False
    return False