from character import Character

class Zombie(Character):
    name = "Zombie"
    def __init__(self, health = 10, power = 1):
        self.health = health
        self.power = power
        self.winPhrase = "Gotta work on them headshots son."

    
    # zombie regenerates health that was done to it
    # def regen(self, enemy):
    #     self.health += enemy.power
# ^^^^^moved to character file
