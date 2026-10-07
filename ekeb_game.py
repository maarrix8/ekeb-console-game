class GameStatus:
    def __init__(self):
        self.energy = 6
        self.turns_left = 6
        self.has_clue = False
        self.has_charger = False 
        self.charger_taken = False
        self.errors = {"A": False, "B": False, "C": False}
        self.game_over = False
        self.win = False

def menu():
    print("МИССИЯ ЕКЕБ")
    print("1. Играть")
    print("2. Правила")
    print("3. Выход")

def check_end(state):
    if all(state.errors.values()):
        state.win = True
        state.game_over = True
        return True
    
    no_turns = state.turns_left <= 0
    no_energy = state.energy < 2 and not state.has_charger and state.charger_taken
    
    if no_turns or no_energy:
        state.game_over = True
        state.win = False
        return True
    return False

def main():
    while True:
        menu()
        choice = input("Выберите (1-3): ").strip()
        
        if choice == '1':
            state = GameStatus()
            while not state.game_over:
                print(f"\nЭнергия: {state.energy}/6 | Ходов: {state.turns_left}")
                print("1. Осмотреть стенд")
                print("2. Взять зарядку")
                print("3. Использовать зарядку")
                print("4. Исправить ошибку")
                print("0. В меню")
                
                act = input("Действие (0-4): ").strip()
                
                if act == '0':
                    break
                elif act in ['1', '2', '3', '4']:
                    print(f"Действие {act} сделают другие участники")
                else:
                    print("Неверная команда")
                    continue
                
                if check_end(state):
                    if state.win:
                        print("Победа!")
                    else:
                        print("Поражение!")
                    break
                    
        elif choice == '2':
            print("Правила: исправьте 3 ошибки за 6 ходов.")
        elif choice == '3':
            print("Выход...")
            break
        else:
            print("Введите 1, 2 или 3.")

if __name__ == "__main__":
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
    def check_answer(number, answer, clue):
    answer = answer.strip().lower()

    if number == "A":
        if not clue:
            print("Сначала нужно осмотреть стенд.")
            return False
        return answer == "ekeb"

    if number == "B":
        return answer == "120"

    if number == "C":
        return answer == "almaty"

    return False

    main()
