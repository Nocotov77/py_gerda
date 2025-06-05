def pupil_number(surname):
    global log
    if surname in log:
        print(log.index(surname) + 1)
    else:
        print("Такого ученика нет.")


def add_pupil(surname):
    global log
    if surname in log:
        print("Такой ученик уже есть в журнале.")
    else:
        log.append(surname)
        log.sort()
        print(f"Ученик {surname} добавлен.")


def to_the_blackboard(n):
    global log
    if not hasattr(to_the_blackboard, "called"):
        to_the_blackboard.called = set()
    try:
        pupil = log[n - 1]
    except IndexError:
        print("Такого ученика нет.")
        return
    if pupil in to_the_blackboard.called:
        print("Сан Саныч, Вы меня уже вызывали!")
    else:
        to_the_blackboard.called.add(pupil)
        print(f"{pupil}, к доске!")