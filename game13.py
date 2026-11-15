# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: РАЗБИТЫЙ МОСТ»
# Автор: Абибулаева Алина
# Дата: сентябрь 2026
# ================================================


# --- Импорт ------------------------------------------------
import random

# --- Заголовок ---------------------------------------------
title = "ПОДЗЕМЕЛЬЕ: РАЗБИТЫЙ МОСТ"
frame = "=" * 31
print(frame)
print("   " + title + "   ")
print(frame)
print()

# --- Знакомство с героем -----------------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name.capitalize()}!")
print("Ты входишь в подземелье. Здесь темно и пахнет сыростью.")
print()

# --- Настройка героя ---------------------------------------
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

# --- Расчёт урона ------------------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health // strength

max_health = health
max_stamina = stamina

# --- Формуляр героя ----------------------------------------
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

# --- Список врагов -----------------------------------------
enemies_stats = {
    "Упырь": {"hp": 20, "damage": 5, "loot": 10},
    "Скелет": {"hp": 40, "damage": 15, "loot": 20},
    "Паук": {"hp": 30, "damage": 12, "loot": 15},
    "Летучая мышь": {"hp": 25, "damage": 10, "loot": 12},
    "Гоблин": {"hp": 35, "damage": 18, "loot": 25},
    "Зомби": {"hp": 45, "damage": 20, "loot": 30},
    "Вампир": {"hp": 60, "damage": 20, "loot": 40},
    "Демон": {"hp": 90, "damage": 20, "loot": 50},
    "Дракон": {"hp": 100, "damage": 30, "loot": 100}
}

log = [] #журнал боя
gold_total = 0
ability_bonus = 0


# --- Данные командного меню --------------------------------
prices = {
    "зелье исцеления": 10,
    "зелье восстановления": 15,
    "зелье силы": 40
}

commands = [
    "осмотреться", "идти [вперед/назад/влево/вправо]", "отдохнуть", "прислушаться", "перекусить",
    "тренировка", "сразиться", "лидеры", "магазин", "инвентарь",
    "выпить [название зелья]", "карта", "разведка", "помощь", "выход"
]

MENU = [
    "Что делаешь? (номер или команда; помощь — «помощь»)",
    "1 - осмотреться (осмотреться)",
    "2 - идти (идти вперед, назад, влево или вправо)",
    "3 - отдохнуть (отдохнуть)",
    "4 - прислушаться (прислушаться)",
    "5 - перекусить (перекусить)",
    "6 - тренировка (тренировка)",
    "7 - сразиться с врагом (сразиться)",
    "8 - таблица лидеров (лидеры)",
    "9 - магазин (магазин)",
    "10 - инвентарь (инвентарь)",
    "11 - использовать зелье исцеления (выпить)",
    "карта - показать карту подземелья",
    "разведка - посчитать доступные комнаты",
    "0 - выйти из игры (выход)"
]

num_to_verb = {
    "1": "осмотреться",
    "2": "идти",
    "3": "отдохнуть",
    "4": "прислушаться",
    "5": "перекусить",
    "6": "тренировка",
    "7": "сразиться",
    "8": "лидеры",
    "9": "магазин",
    "10": "инвентарь",
    "11": "выпить",
    "0": "выход"
}

# --- Главный цикл игры -------------------------------------
running = True

actions = 0 #количество действий

outcome = "прерывание"

inventory = {} #инвентарь

# --- Карта подземелья ---------------------------------------
MAP = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "#", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "S", ".", "#"]
]

hero_r, hero_c = 4, 2
visited = {(4, 2)}

LOOT = {
    (1, 1): "старая монета",
    (2, 3): "пыльное зелье",
    (3, 3): "самоцвет стража"
}

found_loot = set()

DIRECTIONS = {
    "вперед": (-1, 0), "назад": (1, 0),
    "влево": (0, -1), "вправо": (0, 1)
}

# --- Функция запаса сил ----------------------------
def calculation_hero_stamina(hero_health, hero_stamina, cost_stammina):
    """
    Расчет стамины. 
    Убавление hero_health, если стамины не хватает.
    
    Возвращает (hero_health, hero_stamina).
    Глобальные переменные не меняет: здоровье приходит параметром
    и возвращается новым значением.
    """
    if hero_stamina >= cost_stammina:
        hero_stamina -= cost_stammina
    else:
        hero_health -= cost_stammina - hero_stamina
        print(f"❗️Вы потратили все силы и дополнительно получаете {cost_stammina - hero_stamina} урона.")
        hero_stamina = 0
    return hero_health, hero_stamina

# --- Функция урона героя ---------------------------
def hero_hit(strike_n):
    """
    Урон героя в удар номер strike_n.

    Возвращает пару (hit, crit): урон и признак критического удара.
    Читает глобальные правила damage и crit_damage, не меняет ничего.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False

# --- Функция боя с врагом --------------------------
def fight(enemy, hero_health, hero_stamina, bonus):
    """Бой с enemy до гибели одного из двоих.

    bonus — надбавка к урону героя, по умолчанию 0: без эликсира бой идёт как прежде. 
    Печатает строки раундов.
    Возвращает (rounds, won, hero_health, hero_stamina, loot):
    таблицу раундов, признак победы героя, здоровье после боя, запас сил после боя и добычу.
    Глобальные переменные не меняет: враг, здоровье, запас сил и бонус к урону приходят параметром
    и возвращаются новым значением.
    """
    stats = enemies_stats[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0
    cost = 2
    final_hero_dmg = 0
    final_enemy_dmg = 0

    print(f"Вы встречаете врага! Из темноты появляется {enemy}!")
    print()

    while enemy_hp > 0 and hero_health > 0:
        round_n += 1

        hit, crit = hero_hit(round_n)
        hit += bonus

        final_hero_dmg += hit

        frame = '-' * 40
        line = (
            f"🦸 {hero_name.capitalize()} (здоровье: {hero_health}, запас сил: {hero_stamina})\n"
            f"🦹 {enemy} (здоровье: {enemy_hp:.1f})\n"
            f"{hero_name.capitalize()} атакует врага {enemy} и наносит {hit:.1f} урона"
        )

        if crit:
            line += " — критический!"

        if hit >= enemy_hp:
            enemy_hp = 0
            rounds.append([enemy, round_n, hit, 0])

        else:
            enemy_hp -= hit  # атака героя

            blow = float(stats["damage"])
            hero_health -= blow # атака врага
            final_enemy_dmg += blow

            line += f"\n{enemy} атакует Вас и наносит {blow} урона"
            rounds.append([enemy, round_n, hit, blow])

        print(frame)
        print(f"Раунд {round_n}:")
        print(line)
        hero_health, hero_stamina = calculation_hero_stamina(hero_health, hero_stamina, cost)
        print()
    
    print(f"Итоги боя: {hero_name.capitalize()} наносит {final_hero_dmg:.1f} урона, {enemy} наносит {final_enemy_dmg} урона.")

    won = enemy_hp <= 0
    loot = stats["loot"] if won else 0

    return rounds, won, hero_health, hero_stamina, loot

# --- Функция покупки в магазине ----------------------------
def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.
    
    quantity по умолчанию 1. Возвращает (gold_left, ok): остаток
    золота и признак успешной покупки. Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False

def scout(r, c, seen):
    """Рекурсивно считает доступные комнаты, начиная с указанной клетки."""
    if (
        (r, c) in seen
        or not (0 <= r < len(MAP) and 0 <= c < len(MAP[r]))
        or MAP[r][c] == "#"
    ):
        return 0

    seen.add((r, c))
    total = 1

    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)

    return total


try:
    while running:

        # --- Меню действий ---------------------------------
        print("\n".join(MENU))
        print()

        # --- Ввод и разбор команды -------------------------
        line = input()
        cmd = line.strip().lower()

        while cmd == "":
            print("Пустая команда. Введи команду или номер пункта.")
            line = input()
            cmd = line.strip().lower()

        words = cmd.split()
        verb = words[0]

        if cmd in num_to_verb:
            verb = num_to_verb[cmd]

        if verb == "купить":
            verb = "магазин"
            words = ["магазин"] + words[1:]

        match verb:
            case "осмотреться":
                print("Вы осмотрелись. Доски прогнили, ветер дует через щели.")

            case "идти":
                if len(words) > 1 and words[1] in DIRECTIONS:
                    dr, dc = DIRECTIONS[words[1]]
                    nr, nc = hero_r + dr, hero_c + dc

                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))

                        cost = 3
                        health, stamina = calculation_hero_stamina(health, stamina, cost)

                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                inventory[item] = inventory.get(item, 0) + 1
                                print(f"Вы нашли предмет «{item}»! Уникальных находок: {len(found_loot)}.")

                        print(f"Вы идёте в направлении «{words[1]}». Комната ({hero_r}, {hero_c}).")
                    else:
                        print(f"Нельзя идти в направлении «{words[1]}»: там стена или край карты.")
                else:
                    print("Неизвестное направление. Используй: вперед, назад, влево или вправо.")

            case "отдохнуть":
                stamina = min(stamina + 2, max_stamina)
                print("Вы отдыхаете и набираетесь сил.")

            case "прислушаться":
                print("Вы замираете и прислушиваетесь. В темноте слышен тихий скрип досок.")

            case "перекусить":
                health = min(health + 2, max_health)
                print("Вы перекусываете и немного восстанавливаете здоровье.")

            case "тренировка":
                cost = 5
                print("Вы подходите к тренировочному чучелу.")
                print("Оно стоит здесь с тех пор, как сюда приходил последний искатель")
                print()

                strikes = 3
                total_damage = 0.0
                crit_count = 0

                print(f"Наносите {strikes} ударов.")

                for i in range(1, strikes + 1):
                    hit_damage, crit = hero_hit(i)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")
                    total_damage += hit_damage

                avg_damage = total_damage / strikes

                damage += 1
                crit_damage = damage * 2

                print()
                print(f"Итог: {strikes} ударов (критических: {crit_count})")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {avg_damage:.1f}")
                health, stamina = calculation_hero_stamina(health, stamina, cost)

            case "сразиться":
                if not enemies_stats:
                    print("Подземелье пусто, врагов нет.")
                else:
                    enemy = random.choice(list(enemies_stats.keys()))
                    rounds, won, health, stamina, loot = fight(
                        enemy, health, stamina, ability_bonus
                    )

                    for r in rounds:
                        log.append(r)

                    if won:
                        gold_total += loot
                        del enemies_stats[enemy]
                        print(
                            f"{enemy} побежден! В подземелье осталось "
                            f"{len(enemies_stats)} врагов. У вас {gold_total} золота."
                        )
                    print(f"Всего раундов: {len(rounds)}.")

            case "лидеры":
                if not log:
                    print("Таблица лидеров пуста. Сражений ещё не было.")
                else:
                    top = sorted(log, key=lambda r: r[2], reverse=True)[:3]
                    print("*" * 40)
                    print("Топ-3 лучших атак героя:")
                    for i in range(len(top)):
                        print(
                            f"{i + 1}. Враг: {top[i][0]}, Раунд: {top[i][1]}, "
                            f"Урон: {top[i][2]:.1f}"
                        )
                    print("*" * 40)

                    print()
                    max_enemies_dmg = max(log, key=lambda r: r[3])
                    print(f"Наибольший урон от врага: {max_enemies_dmg[3]}")
                    max_enemies = [
                        x for x in log if x[3] == max_enemies_dmg[3]
                    ]
                    for i in range(len(max_enemies)):
                        print(
                            f"Враг {max_enemies[i][0]} нанес наибольший "
                            f"урон в раунде {max_enemies[i][1]}."
                        )

            case "магазин":
                print(f"Вы заходите в магазин подземелья. У вас {gold_total} золота.")
                print("Товары в магазине:")
                for name, price in prices.items():
                    print(f"> {name}: {price} золота за штуку")
                purchase_words = words[1:]
                if purchase_words and purchase_words[0] == "купить":
                    purchase_words = purchase_words[1:]
                if not purchase_words:
                    purchase_line = input("Что Вы хотите купить? Введи название товара и количество или «отмена»: ").strip().lower()
                    if purchase_line in ("отмена", "отменить", "назад"):
                        print("Покупка отменена.")
                        print()
                        continue
                    purchase_words = purchase_line.split()

                if not purchase_words:
                    print("Название товара не указано. Покупка отменена.")
                    print()
                    continue

                if purchase_words[-1].isdigit():
                    qty = int(purchase_words[-1])
                    item = " ".join(purchase_words[:-1])
                else:
                    qty = 1
                    item = " ".join(purchase_words)

                if not item:
                    print("Название товара не указано. Покупка отменена.")
                    print()
                    continue
                if qty <= 0:
                    print("Количество должно быть больше нуля.")
                    print()
                    continue
                if item not in prices:
                    print(f"Товара «{item}» нет в магазине.")
                    print()
                    continue

                price = prices[item]
                gold_total, ok = buy(price, gold_total, quantity=qty)
                if not ok:
                    print(f"Недостаточно золота: нужно {price * qty}, есть {gold_total}.")
                    print()
                    continue

                inventory[item] = inventory.get(item, 0) + qty
                print(f"Вы купили {qty} шт. товара «{item}» за {price * qty} золота.")
                print(f"Осталось золота: {gold_total}.")
                print()

            case "инвентарь":
                if not inventory:
                    print("Инвентарь пуст.")
                else:
                    print("Инвентарь:")
                    for name, qty in inventory.items():
                        print(f"> {name}: {qty} шт.")

            case "выпить" | "пить":
                item = " ".join(words[1:]) or "зелье исцеления"

                if inventory.get(item, 0) == 0:
                    print(f"У вас нет предмета «{item}» в инвентаре.")
                elif item != "зелье исцеления":
                    print(f"Предмет «{item}» нельзя использовать таким способом.")
                else:
                    health = min(health + 10, max_health)
                    inventory[item] -= 1

                    if inventory[item] == 0:
                        del inventory[item]

                    print(
                        "Вы выпиваете зелье исцеления и восстанавливаете "
                        "10 очков здоровья."
                    )
                    print(f"Остаток зелий: {inventory.get(item, 0)}.")


            case "карта" | "map":
                print("Карта подземелья:")
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        cell = "🦸" if (i, j) == (hero_r, hero_c) else MAP[i][j]
                        cells.append(cell)
                    print(" ".join(cells))

            case "разведка" | "scout":
                seen = set()
                print(f"Разведка: доступно комнат — {scout(hero_r, hero_c, seen)}.")

            case "помощь" | "помоги":
                print("Доступные команды:")
                print("\n".join(f"- {command}" for command in commands))
                print("\nНомера от 0 до 11 по-прежнему работают.")

            case "выход":
                print("Вы поднимаетесь обратно к свету. Подземелье остаётся позади.")
                outcome = "выход"
                running = False

            case _:
                print(f"Не понимаю команду: «{line.strip()}». Введи «помощь», чтобы увидеть список команд.")
                print()
                continue

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
        hero_status = f"Здоровье: {health} | Запас сил: {stamina} | Золото: {gold_total}"
        frame_status_top = "┌" + "─" * len(hero_status) + "┐"
        frame_status_bottom = "└" + "─" * len(hero_status) + "┘"
        print(frame_status_top)
        print(f" {hero_status}")
        print(frame_status_bottom)
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
        print(f"Урон, нанесенный героем: {total_hero_dmg:.1f} за {rounds} раундов, средний урон: {total_hero_dmg / rounds:.1f}")
    else:
        print("Сражений не было.")

    if inventory:
        print("Остатки в инвентаре:")
        for name, qty in inventory.items():
            print(f"> {name}: {qty} шт.")
    else:
        print("Инвентарь пуст.")

    if found_loot:
        print("Найденные уникальные предметы:")
        for item in sorted(found_loot):
            print(f"> {item}")
    else:
        print("Уникальные предметы не найдены.")

    print(frame)