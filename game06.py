# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: РАЗБИТЫЙ МОСТ»
# Автор: Абибулаева Алина
# Дата: сентябрь 2026
#
# Пункт 4 — «прислушаться»: герой замирает
# и слушает, что происходит в темноте.
# ================================================

# --- Заголовок -----------------------------------------
title = "ПОДЗЕМЕЛЬЕ: РАЗБИТЫЙ МОСТ"
frame = "=" * 31
print(frame)
print("   " + title + "   ")
print(frame)
print()

# --- Знакомство с героем -------------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в подземелье. Здесь темно и пахнет сыростью.")
print()

# --- Настройка героя -----------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")
while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        endurance = int(input())
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength < 0 or agility < 0 or endurance < 0:
            raise ValueError("Характеристики не могут быть отрицательными")
        if health > 100:
            raise ValueError("Максимальное здоровье 100")
        if strength > 20:
            raise ValueError("Максимальная сила 20")
        break
    except ValueError as e:
        print(f"{e}. Введите все четыре снова:")

# --- Расчёт урона --------------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health // strength

# --- Формуляр героя ------------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health:>7d}")
print(f"Сила: {strength:>9d}")
print(f"Ловкость: {agility:>5d}")
print(f"Выносливость: {endurance}")

print()

print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")
print()


# --- Главный цикл игры ---------------------------------
running = True

actions = 0 #количество действий

outcome = "прерывание"

try:
    while running:

        # --- Меню действий ---------------------------------
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - прислушаться")
        print("5 - перекусить")
        print("6 - тренировка")
        print("0 - выйти из игры")

        print()

        # --- Последний пункт меню --------------------------
        menu_last = 6

        # --- Выбор действия --------------------------------
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню.")
                print()
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи номер пункта из меню.")
            print()

        match choice:
            case "1":
                print("Вы осмотрелись. Доски прогнили, ветер дует через щели.")

            case "2": #stamina -= 3
                cost = 3

                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Доски скрипят под вашими ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")
            
            case "3": #stamina += 2
                stamina = stamina + 2
                print("Вы отдыхаете и набираетесь сил.")
            
            case "4":
                print("Вы замираете и прислушиваетесь. В темноте слышен тихий скрип досок.")
            
            case "5": #stamina += 1
                stamina = stamina + 1
                print("Вы перекусываете и немного восстанавливаете силы.")
            
            case "6": #stamina -= 5
                cost = 5
                
                if stamina >= cost:
                    stamina -= cost
                    print("Вы подходите к тренировочному чучелу.")
                    print("Оно стоит здесь с тех пор, как сюда приходил последний искатель") 
                    print()
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")
                    print("Вы подходите к тренировочному чучелу.")
                    print("Оно стоит здесь с тех пор, как сюда приходил последний искатель") 
                    print()

                strikes = 3
                total_damage = 0.0
                crit_count = 0

                print(f"Наносите {strikes} ударов.")

                for i in range(1, strikes + 1):
                    if i % 3 == 0:
                        total_damage += crit_damage
                        crit_count += 1
                        print(f"Удар {i}: {crit_damage:.1f} - критический!")
                    else:
                        total_damage += damage
                        print(f"Удар {i}: {damage:.1f}")

                avg_damage = total_damage / strikes

                print()
                print(f"Итог: {strikes} ударов (критических: {crit_count})")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {avg_damage:.1f}")

            case "0":
                print("Вы поднимаетесь обратно к свету. Подземелье остаётся позади.")
                outcome = "выход"
                running = False

            case _:
                print("Такого действия нет.")

        print()

        # --- Проверка гибели -------------------------------
        if health <= 0:
            print(f"{hero_name} падает без сил. Подземелье забирает ещё одного искателя.")
            health = 0
            outcome = "гибель"
            running = False 

        # --- Счётчик действий ------------------------------
        if running:
            actions += 1

        # --- Состояние героя -------------------------------
        print(f"Здоровье: {health}   Запас сил: {stamina}")
        print()
except KeyboardInterrupt:
    print()
    print(f"Игрок {hero_name} прервал сеанс.")
finally:
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, игроком {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, игроком {hero_name}. Действий совершено: {actions}.")
    print(frame)