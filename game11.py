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
    "Демон": {"hp": 90, "damage": 35, "loot": 50},
    "Дракон": {"hp": 150, "damage": 60, "loot": 100}
}

log = [] #журнал боя
gold_total = 0
ability_bonus = 0


# --- Главный цикл игры -------------------------------------
running = True

actions = 0 #количество действий

outcome = "прерывание"

inventory = {} #инвентарь

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
        print("9 - магазин")
        print("10 - инвентарь")
        print("11 - использовать зелье исцеления")
        print("0 - выйти из игры")

        print()

        # --- Последний пункт меню --------------------------
        menu_last = 11

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
                print("Вы осторожно идёте вперёд. Доски скрипят под вашими ногами.")
                
                cost = 3
                health, stamina = calculation_hero_stamina(health, stamina, cost)
            
            case "3": #stamina += 2
                stamina = min(stamina + 2, max_stamina)
                print("Вы отдыхаете и набираетесь сил.")
            
            case "4":
                print("Вы замираете и прислушиваетесь. В темноте слышен тихий скрип досок.")
            
            case "5": #health += 2
                health = min(health + 2, max_health)
                print("Вы перекусываете и немного восстанавливаете здоровье.")
            
            case "6": #stamina -= 5
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

                print()
                print(f"Итог: {strikes} ударов (критических: {crit_count})")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {avg_damage:.1f}")
                health, stamina = calculation_hero_stamina(health, stamina, cost)

            case "7":

                if not enemies_stats:
                    print("Подземелье пусто, врагов нет.")
                else:
                    enemy = random.choice(list(enemies_stats.keys()))
                    rounds, won, health, stamina, loot = fight(enemy, health, stamina, ability_bonus)

                    for r in rounds:
                        log.append(r)
                        
                    if won:
                        gold_total += loot
                        del enemies_stats[enemy]
                        print(f"{enemy} побежден! В подземелье осталось {len(enemies_stats)} врагов. У вас {gold_total} золота.")
                    print(f"Всего раундов: {len(rounds)}.")

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

            case "9":
                prices = {"зелье исцеления": 10, "масло для факелов": 15, "боевой эликсир": 40}
                
                print(f"Вы заходите в магазин подземелья. У вас {gold_total} золота.")
                print("Что хотите купить?")
                for name, price in prices.items():
                    print(f"> {name}: {price} золота")
                print("Выберите товар (enter - ничего):")
                name = input()
                
                if name != "":
                    if name in prices:
                        price = prices[name]
                        print("Количество (по умолчанию «1»):")
                        qty_line = input()

                        if qty_line == "":
                            qty = 1
                            gold_total, ok = buy(price, gold_total)
                        else:
                            qty = int(qty_line)
                            gold_total, ok = buy(price, gold_total, quantity=qty)
                        
                        if ok:
                            inventory[name] = inventory.get(name, 0) + qty
                            print(f"Вы купили {qty} {name} за {price * qty} золота.")
                        
                        else:
                            print(f"Недостаточно золота: нужно {price * qty}, есть {gold_total}.")

                    else:
                        print("Такого товара нет в магазине.")

            case "10":
                if not inventory:
                    print("Инвентарь пуст.")
                else:
                    print("Инвентарь:")
                    for name, qty in inventory.items():
                        print(f"> {name}: {qty} шт.")

            case "11":
                if not inventory.get("зелье исцеления", 0) == 0:
                    print("У вас нет зелья исцеления в инвентаре.")
                else:
                    health = min(health + 10, max_health)
                    inventory["зелье исцеления"] -= 1

                    if inventory["зелье исцеления"] == 0:
                        del inventory["зелье исцеления"]

                    print("Вы выпиваете зелье исцеления и восстанавливаете 10 очков здоровья.")
                    print(f"Остаток зелий: {inventory.get('зелье исцеления', 0)}.")

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
    print(frame)