from character import Character

class Hero(Character):
    name = "Hero"
    def __init__(self, health = 10, power = 5):
        self.health = health
        self.power = power
        self.winPhrase = "Good job, you killed the easiest enemy ever."


# checks to see if the hero is alive
    # def isAlive(self):
    #     if self.health > 0:
    #         return True
    #     else:
    #         return False


#  the hero attacks the goblin
    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print(f"The {self.name} did {self.power} damage to the {enemy.name}.")
    # ^^^this comes from character now

# prints status of this character
    # def printStatus(self):
    #     print(f"You have {self.health} health and {self.power} power.")