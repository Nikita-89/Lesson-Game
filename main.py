class Hero():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.health -=self.attack_power
        print(f"{self.name} атаковал {enemy.name} с силой {self.attack_power}")
        print(f"У {enemy.name} осталось {enemy.health} здоровья")

    def is_alive(self):
        if self.health > 0:
            print(f"{self.name} Еще жив")
            return True
        else:
            print(f"Умер")
            return False

class Game:

    def __init__(self, humane, zombie):
       self.hero = Hero(humane, 100, 20)
       self.enemy = Hero(zombie, 100, 15)
    def start(self):
        print(f"Игра началась")

        while self.hero.is_alive() and self.enemy.is_alive():
            if self.hero.attack(self.enemy):
                self.enemy.health -= self.attack_power
            else:
                self.enemy.attack(self.hero)

        if not self.hero.is_alive():
            print(f"{self.hero.name} Пал в бою")


        elif not self.enemy.is_alive():
            print(f"{self.enemy.name} Пал в бою")


game = Game("Человек", "Зомби")
game.start()





