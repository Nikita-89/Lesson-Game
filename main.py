class Game:
   def __init__(self, humane, zombie):
    self.player = Hero(humane, 100, 20)
    self.computer = Hero(zombie, 100, 15)  
