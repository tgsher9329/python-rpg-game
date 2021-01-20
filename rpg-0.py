from hero import Hero
from goblin import Goblin
from zombie import Zombie
from character import Character

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    my_hero = Hero()
    goblin = Goblin()
    zombie = Zombie()

    # while goblin.health > 0 and my_hero.health > 0:
    while goblin.isAlive() and my_hero.isAlive():
        # print("You have %d health and %d power." % (my_hero.health, my_hero.power))
        my_hero.printStatus()
        goblin.printStatus()
        # print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()

        if my_hero.health <= 0:
            print('You are terrible, you got schwacked by a weak garden gnome.')
            break



        if user_input == "1":
            # Hero attacks goblin
            # goblin.health -= my_hero.power
            # print("You do %d damage to the goblin." % my_hero.power)
            # if goblin.health <= 0:
            #     print("The goblin is dead.")
            my_hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
                    goblin.attack(my_hero)

        # if goblin.health > 0:
        #     # Goblin attacks hero
        #     # my_hero.health -= goblin.power
        #     # print("The goblin does %d damage to you." % goblin.power)
        #     # if my_hero.health <= 0:
        #     #     print("You are dead.")
        #     goblin.attack(my_hero)

    while zombie.isAlive() and my_hero.isAlive():
            # fights the zombie after killing the goblin
            print("Zombies are real, the goblin has come back... good luck.")
            while zombie.isAlive() and my_hero.isAlive():
                my_hero.printStatus()
                zombie.printStatus()

                print()
                print("What do you want to do?")
                print(f"1. fight zombie")
                print("2. do nothing")
                print("3. flee")
                print("> ",)
                user_input = input()

                if my_hero.health <= 0:
                    print('I guess doing work one two people seperatly is too much for you.')
                    break

                elif user_input == "1":
                    my_hero.attack(zombie)
                    zombie.regen(my_hero)

                elif user_input == "2":
                    pass

                elif user_input == "3":
                    print("Too much for you?")
                    break

                else:
                    print("Invalid input %r" % user_input)

                if zombie.health > 0:
                    zombie.attack(my_hero)
main()