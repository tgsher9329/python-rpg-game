class Character:
    name = "character"
    # checks to see is the charcter is alive
    def isAlive(self):
        if self.health > 0:
            return True
        
        else:
            return False


# prints status of this character
    def printStatus(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")


# the self attacks the enemy, or the other player
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"The {self.name} did {self.power} damage to the {enemy.name}.")
        if enemy.health <= 0:
            print(self.winPhrase)

# gives characters the ability to regen the health of whatever power their enemy has
    def regen(self, enemy):
        self.health += enemy.power