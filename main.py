class Hero():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        enemy.health -=self.attack_power
        print(f"{self.name} атаковал {enemy.name} с силой {self.attack_power}")
        print(f"У {enemy.name} осталось {enemy.health} здоровья")

    def is_alive(self):
        if self.health > 0:
            print(f"Еще жив")
            return True
        else:
            print(f"Умер")
            return False




