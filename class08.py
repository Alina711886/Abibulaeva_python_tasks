# Class8. Класс Hero: name, health, damage; методы to_dict() и from_dict(data); сохранить объект в словарь, создать из словаря новый объект и вывести его health.

class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def to_dict(self):
        return {
            'name': self.name,
            'health': self.health,
            'damage': self.damage
        }

    def from_dict(self, data):
        return Hero(data['name'], data['health'], data['damage'])

name = input()
health = int(input())
damage = int(input())

hero = Hero(name, health, damage)
data = hero.to_dict()

new_hero = Hero.from_dict(data)
print(new_hero.health)