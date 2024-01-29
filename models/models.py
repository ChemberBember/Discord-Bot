import random
import discord


def generate_objects():
    num_objects = random.randint(2, 8)
    objects = random.choices([0, 1], k=num_objects - 2)
    objects.append(0)
    objects.append(1)
    random.shuffle(objects)
    return objects


class User:
    def __init__(self, dict):
        self.name = dict['name']
        self.uid = dict['uid']
        self.luck = dict['luck']
        self.charisma = dict['charisma']
        self.intelligence = dict['intelligence']
        self.strength = dict['strength']
        self.agility = dict['agility']
        self.inventory = dict['inventory']
        self.dead = dict['dead']
        self.carma = dict['carma']

    def add_item(self, item):
        self.inventory[item] = self.inventory.get(item, 0) + 1

    def remove_item(self, item):
        self.inventory[item] -= 1

        if self.inventory[item] == 0:
            del self.inventory[item]

    def add_luck(self, luck):
        self.luck += luck

    def add_charisma(self, charisma):
        self.charisma += charisma

    def add_intelligence(self, intelligence):
        self.intelligence += intelligence

    def add_strength(self, strength):
        self.strength += strength

    def add_agility(self, agility):
        self.agility += agility

    def set_dead(self):
        self.dead = True


class CreateUser:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid
        self.luck = 0
        self.charisma = 0
        self.intelligence = 0
        self.strength = 0
        self.agility = 0
        self.carma = 0
        self.dead = False

        self.inventory = {}


class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name


"""Roulette game"""


class RouletPlayer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hp = 6
        self.dmg = 1
        self.inventory = []
        self.blocked = False

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def heal(self, hp):
        self.hp += hp

    def take_dmg(self, damage):
        self.hp -= damage

    def block(self):
        self.blocked = True

    def unblock(self):
        self.blocked = False


class RouletShotgun:

    def __init__(self, pool=generate_objects()):
        self.pool = pool
        self.realBullets = self.pool.count(1)
        self.fakeBullets = self.pool.count(0)
        self.bullet = None

    def shoot(self):
        self.bullet = self.pool[0]
        del self.pool[0]
        return self.bullet

    def check_pool(self):
        if len(self.pool) > 0:
            return True
        else:
            return False
