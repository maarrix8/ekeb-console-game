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

