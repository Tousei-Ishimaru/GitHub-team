import random

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def battle(self, opponent):
        ran = randint(0,1)
        if (ran == 0):
            print(self)
        else if (ran == 1):
            print(opponent)

    if __name__ == "__main__":
        my_hero = Hero("grace hopper", 200)
        print(my_hero.name)
        print(my_hero.current_health)
