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
    def take_charger(charging_taken, inventory, moves):
        if charging_taken:
            print("Вы уже забрали зарядку")
        else:
            charging_taken = True
            inventory.append("Зарядка")
            moves -= 1
            print("Вы забрали зарядку.")
        return charging_taken, inventory, moves


def use_charger(inventory, energy, moves):
    if "Зарядка" not in inventory:
        print("У вас нет зарядки.")
        return inventory, energy, moves
    inventory.remove("Зарядка")
    energy += 3
    if energy > 6:
        energy = 6
    moves -= 1
    print("Вы использовали зарядку.")
    print("Энергия восстановлена")
    return inventory, energy, moves


def show_status(energy, moves, errors_fixed, inventory, clue):
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


def handle_user_input(prompt_text="Выберите действие: "):
    """Очищает ввод от пробелов и проверяет на пустую строку."""
    user_input = input(prompt_text)
    cleaned = user_input.strip()
    if not cleaned:
        print("\n[Ошибка ввода]: Вы ничего не ввели. Ресурсы НЕ были потрачены.")
        return ""
    return cleaned


def check_menu_choice(choice, available_options):
    """Проверяет, входит ли выбранная команда в список доступных."""
    if choice not in available_options:
        print(f"\n[Ошибка ввода]: Другая команда '{choice}'. Ресурсы НЕ были потрачены.")
        return False
    return True


def check_error_selection(choice, state):
    """
    Проверяет корректность выбора ошибки (A, B или C).
    Защищает ресурсы игрока от траты при неверных действиях.
    """
    upper_choice = choice.upper()

    # Словарь сопоставления (поддерживает английские и русские буквы)
    mapping = {'A': 'A', 'B': 'B', 'C': 'C', 'А': 'A', 'Б': 'B', 'В': 'C'}

    # 1. Проверка на существование такой ошибки
    if upper_choice not in mapping:
        print(f"\n[Ошибка ввода]: Другое имя ошибки '{choice}'. Ресурсы НЕ были потрачены.")
        return None

    target_error = mapping[upper_choice]

    # 2. Проверка уровня энергии (нужно минимум 2)
    if state.energy < 2:
        print("\n[Нехватка ресурсов]: Недостаточно энергии для исправления ошибки! Ресурсы НЕ были потрачены.")
        return None

    # 3. Проверка, не исправлена ли ошибка ранее
    if state.fixed_errors[target_error]:
        print(f"\n[Логическая ошибка]: Ошибка {target_error} УЖЕ исправлена. Ресурсы НЕ были потрачены.")
        return None

    # 4. Проверка обязательного осмотра стенда перед ошибкой А
    if target_error == 'A' and not state.has_clue:
        print(
            "\n[Логическая ошибка]: Сначала нужно осмотреть стенд, чтобы получить КОД доступа! Ресурсы НЕ были потрачены.")
        return None

    return target_error
main()