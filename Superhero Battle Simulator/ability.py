class Ability:
  def __init__(self, name, max_damage):
      self.name = name
      self.max_damage = max_damage

      return f"{self.name} used with max damage of {self.max_damage}"

# Example usage:
ability1 = Ability("Fireball", 50)
ability2 = Ability("Sword Slash", 30)


class Hero:
    def __init__(self, name, initial_health):
        self.name = name
        self.current_health = initial_health

if __name__ == "__main__":
    my_hero = Hero("Moncho Man", 200)
    print(my_hero.name)
    print(my_hero.current_health)
