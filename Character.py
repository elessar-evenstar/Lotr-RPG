import time
import random

class Character:
    def __init__(self, name, species, power, weapon, skill, personality):
        self.name = name
        self.species = species
        self.power = power
        self.weapon = weapon
        self.skill = skill
        self.personality = personality

    def describe(self):
        time.sleep(1)
        print("Your character is", self.name, ", he/she is a", self.species, ", his/her weapon is", self.weapon, ", his/her skill is", self.skill, "and his/her personality is", self.personality, ".")

    def talk_to(self, character, words):
        time.sleep(1)
        if self.name != character.name:
            print(self.name, "said to", character.name, ":", words)
        time.sleep(1)

    def smoke(self):
        time.sleep(1)
        print(self.name, "gets a pipe.")
        time.sleep(1)
        if self.species == "elf" or self.species == "Maia":
            print(self.name, "said: What is this thing!!")
        else:
            print(self.name, "said: This is so good!")

    def fight(self, enemy):
        time.sleep(1)
        if self.name != enemy.name:
            fight_random_list = ["yes", "no"]
            fight_random = random.choice(fight_random_list)
            if fight_random == "yes":
                your_health = self.power
                enemy_health = enemy.power
                enemy_powerup = 0
                powerup = 0
                while your_health > 0 and enemy_health > 0:
                    print("Your health is", your_health, "and", enemy.name, "'s health is", enemy_health)
                    fight_action_1 = input("What do you want to do? (Attack, Defend, Power up. You cannot attack unless you power up.")
                    fight_action = fight_action_1.lower().strip()
                    enemy_action = random.choice(["attack", "defend", "powerup"])
                    if fight_action == "attack" and enemy_action == "attack":
                        if powerup == 0:
                            print("You cannot attack because you did not power up.")
                        if enemy_powerup == 0:
                            print(enemy.name, "cannot attack because he did not power up.")
                        else:
                            print("You attacked and", enemy.name, "attacked.")
                            print("You both lose a point.")
                            your_health = int(your_health) - 1
                            enemy_health = int(enemy_health) - 1
                            enemy_powerup = int(enemy_powerup) - 1
                            powerup = int(powerup) - 1
                    if fight_action == "attack" and enemy_action == "defend":
                        if powerup == 0:
                            print("You cannot attack because you did not power up.")
                        else:
                            print("You attacked and", enemy.name, "defended.")
                            print("No one loses a point.")
                            powerup = int(powerup) - 1
                    if fight_action == "attack" and enemy_action == "powerup":
                        if powerup == 0:
                            print("You cannot attack because you did not power up.")
                        else:
                            print("You attacked and", enemy.name, "powered up.")
                            print(enemy.name, "loses a point.")
                            enemy_health = int(enemy_health) - 1
                            powerup = int(powerup) - 1
                            enemy_powerup = int(enemy_powerup) + 1
                    if fight_action == "defend" and enemy_action == "attack":
                        if enemy_powerup == 0:
                            print(enemy.name , "cannot attack because he did not power up.")
                        else:
                            print("You defended and", enemy.name, "attacked.")
                            print("No one loses a point.")
                            enemy_powerup = int(enemy_powerup) - 1
                    if fight_action == "defend" and enemy_action == "defend":
                        print("You defended and", enemy.name, "defended.")
                        print("No one loses a point.")
                    if fight_action == "defend" and enemy_action == "powerup":
                        print("You defended and", enemy.name, "powered up.")
                        print("No one loses a point.")
                        enemy_powerup = int(enemy_powerup) + 1
                    if fight_action == "power up" and enemy_action == "attack":
                        if enemy_powerup == 0:
                            print(enemy.name, "could not attack because he did not power up.")
                        else:
                            print("You powered up and", enemy.name, "attacked.")
                            print("You lost a point.")
                            powerup = int(powerup) + 1
                            enemy_powerup = int(enemy_powerup) - 1
                            your_health = int(your_health) - 1
                    if fight_action == "power up" and enemy_action == "defend":
                        print("You powered up and", enemy.name, "defended.")
                        print("No one lost a point.")
                        powerup = int(powerup) + 1
                    if fight_action == "power up" and enemy_action == "powerup":
                        print("You powered up and", enemy.name, "powered up.")
                        print("No one lost a point.")
                        powerup = int(powerup) + 1
                        enemy_powerup = int(enemy_powerup) + 1
                if your_health == 0:
                    print(enemy.name, "won!")
                if enemy_health == 0:
                    print("You won!")
                if your_health == 0 and enemy_health == 0:
                    print("There was a tie.")

            if fight_random == "no":
                print(enemy.name, "did not want to fight you.")

    def go_to(self, place):
        print("You are entering", place.name, "...")
        time.sleep(1)
        print("You have entered", place.name, ", a", place.place_type , "populated by", place.population, ". It is in the", place.location, "part of Middle Earth.")

frodo = Character("Frodo", "hobbit", 5, "Sting", "resistance", "nice")
sam = Character("Sam", "hobbit", 4, "frying pan", "cooking", "loyal")
legolas = Character("Legolas", "elf", 8, "bow and arrows", "archery", "brave")
gandalf = Character("Gandalf", "wizard", 10, "staff", "magic", "wise")
aragorn = Character("Aragorn", "human", 8, "Anduril", "fighting", "brave")
boromir = Character("Boromir", "human", 7, "sword", "fighting", "determined")
sauron = Character("Sauron", "Maia", 11, "mace", "killing", "evil")
orc = Character("Orc", "orc", random.randint(1, 6), "sword", "killing", "evil")
gollum = Character("Gollum", "hobbit", 2, "nothing", "catching fish", "creepy")
balrog = Character("Balrog", "balrog", 10, "fire whip", "killing", "evil")
goblin = Character("Goblin", "goblin", random.randint(1, 4), "sword", "killing", "evil")
shelob = Character("Shelob", "spider", 5, "stinger", "catching prey", "evil")
thranduil = Character("Thranduil", "elf", 9, "sword", "being king", "smug")
galadriel = Character("Galadriel", "elf", 10, "nothing", "telling the future", "mysterious")
haldir = Character("Haldir", "elf", 8, "bow and arrows", "fighting", "brave")
arwen = Character("Arwen", "elf", 6, "sword", "healing", "kind")
merry = Character("Merry", "hobbit", 5, "small sword", "smoking", "funny")
pippin = Character("Pippin", "hobbit", 4, "small sword", "smoking", "foolish")
gimli = Character("Gimli", "dwarf", 7, "axe", "fighting", "gruff")
