from enum import Enum
from random import randint, choice


class Ability(Enum):
    BOOST = 6
    HEAL = 0
    CRITICAL_DAMAGE = 1
    BLOCK_DAMAGE_AND_REVERT = 5
    STUNNED = 0



class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} HEALTH: {self.__health} DAMAGE: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None
        self.__stunned = False

    @property
    def defence(self):
        return self.__defence

    @property
    def stunned(self):
        return self.__stunned

    @stunned.setter
    def stunned(self, value):
        self.__stunned = value

    def choose_defence(self):
        abilities_list = [e for e in Ability]
        self.__defence = choice(abilities_list)

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0 and self.__stunned == False:
                if type(hero) == Berserk:
                    hero.blocked_damage = self.damage // hero.super_ability.value
                    hero.health -= self.damage - hero.blocked_damage
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' DEFENCE: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        if type(super_ability) == Ability:
            self.__super_ability = super_ability
        else:
            raise ValueError('Data type of attribute super_ability must be enum Ability')

    @property
    def super_ability(self):
        return self.__super_ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        # Warrior applies CRIT
        coeff = randint(2, 6)
        boss.health -= coeff * self.damage
        print(f'Warrior {self.name} hits critically {coeff * self.damage}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    def apply_super_power(self, boss, heroes):
        bost_ = randint(0,2)
        if bost_ == 0:
            print(f"Magicn {self.name} failed to cast the spell")
        else:

            print(f"Magican {self.name} bost damege heroes for {bost_}")
        for hero in heroes:
            hero.damage += bost_

class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        # Berserk revert blocked damage
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} blocked and reverted {self.blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        # Medic heals
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.STUNNED)

    def apply_super_power(self, boss, heroes):
        boss_damage =+ boss.damage
        if randint(1, 100) <= 10:  # 10% chance to stun
            boss.stunned = True
            print(f'Thor {self.name} stunned the boss!')
        else:
            boss.damage = boss_damage

class Witcher(Hero):
    def __init__(self, name, health):
        super().__init__(name, health, 0,  Ability.HEAL)
        self.damage -= self.damage
    def apply_super_power(self, boss, heroes):
        # Witcher's ability to revive a fallen hero
        fallen_heroes = [hero for hero in heroes if hero.health <= 0]
        if fallen_heroes:
            chosen_hero = choice(fallen_heroes)
            chosen_hero.health = self.health
            self.health = 0
            print(f'{self.name} revived {chosen_hero.name}!')

class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    def apply_super_power(self, boss, heroes):
        shuriken_type = choice(["Virus", "Vaccine"])
        if shuriken_type == "Virus":
            boss.health -= self.damage
            print(f'Samurai {self.name} threw a virus shuriken for {self.damage} damage!')
        elif shuriken_type == "Vaccine":
            hero = choice(heroes)
            hero.health += self.damage
            print(f'Samurai {self.name} threw a vaccine shuriken to heal the {hero.name} by {self.damage} health!')

class Bomber(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        # When defeated, deal additional damage to the boss
        boss.health -= 100
        print(f'Bomber {self.name} exploded and dealt 100 additional damage to the boss!')

class OnePunchMan(Hero):
    def __init__(self, name, health):
        super().__init__(name, 9999999999999999999999, 0, Ability.BOOST)  # Zero damage

    def apply_super_power(self, boss, heroes):
        # When the last hero standing, deal damage to the boss equal to remaining health
        living_heroes = [hero for hero in heroes if hero.health > 0]
        if len(living_heroes) == 1 and living_heroes[0] == self:
            damage_dealt = self.health
            boss.health -= damage_dealt
            print(f'OnePunchMan {self.name} dealt {damage_dealt} damage to the boss with one punch!')






round_number = 0


def start():
    boss = Boss('Gargarab', 10000, 50)

    warrior_1 = Warrior('Rudolf', 290, 10)
    warrior_2 = Warrior('Guts', 260, 15)
    doc = Medic('Haus', 250, 5, 15)
    magic = Magic('Petr', 270, 20)
    berserk_1 = Berserk('Conan', 260, 10)
    assistant = Medic('Marty', 300, 5, 5)
    thor_1 = Thor("Chicha", 170, 6)
    withr_1 = Witcher("lutiy", 300)
    samurai_1 = Samurai("Zoro", 200, 20)
    bomber_1 = Bomber("BimBom", 100, 10)
    saitama = OnePunchMan("Saitama")
    heroes_list = [warrior_1, warrior_2, doc, magic, berserk_1, assistant, thor_1, withr_1, samurai_1, bomber_1, saitama]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def play_round(boss, heroes):
    print(boss.stunned)
    input("PRESS ENTER TO PLAY ROUND:")
    global round_number
    round_number += 1
    boss.choose_defence()
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.super_ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)


    if not boss.stunned:
        boss.attack(heroes)
    else:
        boss.stunned = False  # Reset boss's stun status
        print('Boss is stunned and skips this round!')
    show_statistics(boss, heroes)



def show_statistics(boss, heroes):
    print(f'ROUND {round_number} -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('Boss won!!!')

    return all_heroes_dead


start()