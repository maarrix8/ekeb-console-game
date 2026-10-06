# -*- coding: utf-8 -*-

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
        print("\n[Логическая ошибка]: Сначала нужно осмотреть стенд, чтобы получить КОД доступа! Ресурсы НЕ были потрачены.")
        return None
        
    return target_error
