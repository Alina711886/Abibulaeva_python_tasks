# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: РАЗБИТЫЙ МОСТ»
# Автор: Абибулаева Алина
# Дата: сентябрь 2026
#
# Пункт 4 — «прислушаться»: герой замирает
# и слушает, что происходит в темноте.
# ================================================


# --- Импорт --------------------------------------------
import random

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
print(f"Добро пожаловать, {hero_name.capitalize()}!")
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
        if strength == 0:
            raise ValueError("Сила не может быть равна нулю")
        if health > 100:
            raise ValueError("Максимальное здоровье 100")
        if strength > 20:
            raise ValueError("Максимальная сила 20")
        
        break

    except ValueError as e:
        print(f"{e}. Введите все четыре характеристики снова:")

# --- Расчёт урона --------------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health // strength

# --- Формуляр героя ------------------------------------
print()

print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Выносливость: {endurance}")

print()

print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")
print()

# --- Список врагов -------------------------------------
enemies = ["Упырь", "Скелет", "Паук", "Летучая мышь", "Гоблин", "Зомби", "Вампир", "Демон", "Дракон"]

log = [] #журнал боя

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
        print("7 - сразиться с врагом")
        print("8 - таблица лидеров")
        print("0 - выйти из игры")

        print()

        # --- Последний пункт меню --------------------------
        menu_last = 8

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
                    print("Сил больше нет — вы идёте на одном упорстве. Доски скрипят под вашими ногами.")
            
            case "3": #stamina += 2
                stamina = stamina + 2
                print("Вы отдыхаете и набираетесь сил.")
            
            case "4":
                print("Вы замираете и прислушиваетесь. В темноте слышен тихий скрип досок.")
            
            case "5": #health += 2
                health = health + 2
                print("Вы перекусываете и немного восстанавливаете здоровье.")
            
            case "6": #stamina -= 5
                cost = 5
                
                if stamina >= cost:
                    stamina -= cost
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

            case "7": #stamina -= 2 (за одну атаку)
                try:
                    enemy = random.choice(enemies)
                except IndexError:
                    print("Подземелье пусто, врагов нет.")
                    print()
                    continue

                enemy_hp = random.randint(10, 100)
                round_n = 0

                print(f"Вы встречаете врага! Из темноты появляется {enemy}!")

                while enemy_hp > 0 and health > 0:
                    round_n += 1
                    print()
                    print('-' * 40)
                    print(f"Раунд {round_n}:")
                    print(f"{hero_name.capitalize()} здоровье: {health}, запас сил: {stamina}")
                    print(f"{enemy} здоровье: {enemy_hp}")

                    # --- Атака героя --------------------------
                    final_damage = 0

                    if round_n % 3 == 0:
                        enemy_hp -= crit_damage
                        final_damage = crit_damage
                    else:
                        enemy_hp -= damage
                        final_damage = damage
                    print(f"{hero_name.capitalize()} атакует врага {enemy} и наносит {final_damage:.1f} урона.")
                    
                    # --- Расход сил на атаку ------------------
                    cost = 2

                    if stamina >= cost:
                        stamina -= cost
                    else:
                        health -= cost - stamina
                        print(f"Вы потратили все силы и дополнительно получаете {cost - stamina} урона.")
                        stamina = 0

                    # --- Атака врага --------------------------
                    if enemy_hp > 0:
                        enemy_attack = random.randint(5, 15)
                        health -= enemy_attack
                        print(f"{enemy} атакует вас и наносит {enemy_attack} урона.")
                        log.append([enemy, round_n, final_damage, enemy_attack])
                    else:
                        print(f"{enemy} повержен!")
                        enemies.remove(enemy)
                        log.append([enemy, round_n, final_damage, 0])
                    
                    print(f"Итоги раунда: {hero_name.capitalize()} наносит {final_damage:.1f} урона, {enemy} наносит {enemy_attack if enemy_hp > 0 else 0} урона.")

                print()
                print(f"В подземелье осталось {len(enemies)} врагов.")

            case "8":
                if not log:
                    print("Таблица лидеров пуста. Сражений ещё не было.")
                else:
                    top = sorted(log, key=lambda r: r[2], reverse=True)[:3]
                    print("*" * 40)
                    print("Топ-3 лучших атак героя:")
                    for i in range(len(top)):
                        print(f"{i + 1}. Враг: {top[i][0]}, Раунд: {top[i][1]}, Урон: {top[i][2]:.1f}")
                    print("*" * 40)

                    print()

                    max_enemies_dmg = max(log, key=lambda r: r[3])
                    print(f"Наибольший урон от врага: {max_enemies_dmg[3]}")
                    max_enemies = [x for x in log if x[3] == max_enemies_dmg[3]]
                    for i in range(len(max_enemies)):
                        print(f"Враг {max_enemies[i][0]} нанес наибольший урон в раунде {max_enemies[i][1]}.")

            case "0":
                print("Вы поднимаетесь обратно к свету. Подземелье остаётся позади.")
                outcome = "выход"
                running = False

            case _:
                print("Такого действия нет.")

        print()

        # --- Проверка гибели -------------------------------
        if health <= 0:
            print(f"{hero_name.capitalize()} падает без сил. Подземелье забирает ещё одного искателя.")
            health = 0
            outcome = "гибель"
            running = False 

        # --- Счётчик действий ------------------------------
        if running:
            actions += 1

        # --- Состояние героя -------------------------------
        print(f"┌────────────────────────────────┐")
        print(f"   Здоровье: {health} | Запас сил: {stamina}")
        print(f"└────────────────────────────────┘")
        print()
except KeyboardInterrupt:
    print()
    print(f"Игрок {hero_name.capitalize()} прервал сеанс.")
finally:
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name.capitalize()}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, игроком {hero_name.capitalize()}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, игроком {hero_name.capitalize()}. Действий совершено: {actions}.")

    total_hero_dmg = sum(r[2] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Урон, нанесенный героем: {total_hero_dmg:.1f}  за {rounds} раундов, средний урон: {total_hero_dmg / rounds:.1f}")
    else:
        print("Сражений не было.")
    print(frame)