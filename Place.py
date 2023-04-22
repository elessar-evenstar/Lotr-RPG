import time
import random

class Place:
    def __init__(self, name, population, location, place_type):
        self.name = name
        self.population = population
        self.location = location
        self.place_type = place_type

##    def talk_to(self, character, words):
##        time.sleep(1)
##        if self.name != character.name:
##            print(self.name, "said to", character.name, ":", words)
##            time.sleep(1)
##            if words == 'How are you?':
##                print(character.name, "said to", self.name, ": I am fine, thank you!")


minas_tirith = Place("Minas Tirith", "men", "south", "city")
rivendell = Place("Rivendell", "elves", "middle", "city")
shire = Place("The Shire", "hobbits", "west", "realm")
mordor = Place("Mordor", "orcs and Nazgul", "southeast", "realm")
mirkwood = Place("Mirkwood", "elves", "east", "forest")
fangorn = Place("Fangorn", "ents", "south", "forest")
rohan = Place("Rohan", "men", "southwest", "kingdom")


  
