class Hero():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.health -=self.attack_power
        if enemy.health < 0:
            enemy.health = 0
        print(f"{self.name} атаковал {enemy.name} с силой {self.attack_power}")
        print(f"У {enemy.name} осталось {enemy.health} здоровья")

    def is_alive(self):
        return self.health > 0


class Game:

    def __init__(self, humane, zombie):
       self.hero = Hero(humane, 100, 20)
       self.enemy = Hero(zombie, 100, 15)
    def start(self):
        print(f"Игра началась")

        turn = 0

        while self.hero.is_alive() and self.enemy.is_alive():
            if turn % 2 == 0:
                self.hero.attack(self.enemy)
            else:
                self.enemy.attack(self.hero)

            turn += 1

            if not self.hero.is_alive():
                    print(f"{self.hero.name} Пал в бою")
                    break

            elif not self.enemy.is_alive():
                    print(f"{self.enemy.name} Пал в бою")
                    break



game = Game("Человек", "Зомби")
game.start()





