from character import Character

class Goblin(Character):
    name ="Goblin"
    def  __init__(self, health = 6, power = 2):
        self.health = health
        self.power = power
        self.winPhrase = "You are terrible, you got schwacked by a weak garden gnome."


# check to see if the goblin is alive
    # def isAlive(self):
    #     if self.health > 0:
    #         return True
        
    #     else:
    #         return False


# goblin attacks the hero
    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print(f"The {self.name} did {self.power} damage to the {enemy.name}.")
    #     print(self.winPhrase)
    # ^^^^^^this comes from character now


# prints status of this character
    # def printStatus(self):
    #     print(f"The goblin has {self.health} health and {self.power} power.")