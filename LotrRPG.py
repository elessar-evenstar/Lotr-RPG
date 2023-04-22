import time
import random
from Character import frodo, sam, legolas, gandalf, aragorn, boromir, sauron, orc, gollum, balrog, goblin, shelob, thranduil, galadriel, haldir, arwen, merry, pippin, gimli
from Character import Character
from Place import minas_tirith, rivendell, shire, mordor, mirkwood, fangorn, rohan

characters = {'frodo': frodo, 'sam': sam, 'legolas': legolas, 'gandalf': gandalf, 'aragorn': aragorn, 'boromir': boromir, 'thranduil': thranduil, 'galadriel': galadriel, 'haldir': haldir, 'arwen': arwen,
              'sauron': sauron, 'orc': orc, 'gollum': gollum, 'balrog': balrog, 'goblin': goblin, 'shelob': shelob, 'merry': merry, 'pippin': pippin, 'gimli': gimli}
inventory = list()
your_character_upper = input("Choose a character: Frodo, Sam, Merry, Pippin, Gimli, Legolas, Gandalf, Aragorn, Boromir, Arwen, Sauron, or create your own character by typing create.")
if your_character_upper.lower().strip() != "create":
    your_character_name = your_character_upper.lower().strip()
    your_character = characters[your_character_name]
    your_character.describe()
else:
    custom_character_name = input("Type your name").lower().strip()
    custom_character_species = input("Type your species").lower().strip()
    custom_character_power = int(input("How powerful are you from 1 to 10?"))
    custom_character_weapon = input("What is your weapon?").lower().strip()
    custom_character_skill = input("What is your skill?").lower().strip()
    custom_character_personality = input("What is your personality?").lower().strip()
    custom_character = Character(custom_character_name.capitalize(), custom_character_species, custom_character_power, custom_character_weapon, custom_character_skill, custom_character_personality)
    custom_character.describe()
    your_character = custom_character

if your_character == frodo:
    inventory = ["Sting", "pipe", "Lembas bread", "Light of Earendil"]
if your_character == sam:
    inventory = ["frying pan", "pipe", "Lembas bread", "elven rope"]
if your_character == legolas:
    inventory = ["bow", "arrows"]
if your_character == gandalf:
    inventory = ["Staff", "pipe"]
if your_character == aragorn:
    inventory = ["Anduril", "pipe", "Evenstar necklace"]
if your_character == boromir:
    inventory = ["shield", "Horn of Gondor", "sword"]
if your_character == arwen:
    inventory = ["Evenstar necklace", "elven sword"]
if your_character == sauron:
    inventory = ["mace", "One Ring"]
if your_character == merry:
    inventory = ["pipe", "pipeweed", "small sword"]
if your_character == pippin:
    inventory = ["pipe", "pipeweed", "second breakfast"]
if your_character == gimli:
    inventory = ["axe"]



# Plot below
talk_list = ["Hello!", "How are you?", "Good day!", "Hello there!", "Greetings."]
bad_talk_list = ["I will destroy you.", "Get ready to die.", "This will be your last moment alive."]
how_are_you = ["I am great!", "I am fine.", "I am good!", "I am okay."]
frodo_quote = ["All right then, keep you secrets.", "I will take the Ring to Mordor, though I do not know the way.", "You're late."]
sam_quote = ["Po-tay-toes. Boil em, mash em, stick em in a stew.", "There's some good in this world, Mister Frodo, and it's worth fighting for.", "I can't carry it for you, but I can carry you!"]
legolas_quote = ["They're taking the Hobbits to Isengard!", "You have my bow.", "Lembas bread. One small bite is enough to fill the stomach of a grown man."]
gandalf_quote = ["A wizard is never late, nor is he early. He arrives precisely when he means to.", "You shall not pass!!!", "When in doubt, always follow your nose." "Fool of a Took!"]
aragorn_quote = ["For Frodo.", "Let the Lord of the black land come forth! Let justice be done upon him!", "I summon you to fulfill your oath."]
boromir_quote = ["It is a gift.", "One does not simply walk into Mordor.", "It is a strange fate that we should suffer so much fear and doubt over so small a thing."]
sauron_quote = ["I see you..." "I SEE YOU...", "There is no life in the void, only death..."]
arwen_quote = ["It is mine to give to whom I will, like my heart.", "Do you remember when we first met?", "If you want him, come and claim him!"]
kill_hobbit_list = ["You tried to kill some hobbits but they escaped.", "You killed some hobbits.", "The hobbits tried to fight back but you killed them."]
kill_human_list = ["You tried to kill some humans but they escaped.", "You killed some humans.", "The humans fought back but you killed them."]
kill_elf_list = ["You tried to kill some elves but they escaped.", "You killed some elves.", "The elves fought back but you killed them.", "The elves fought back and escaped."]
kill_ent_list = ["You tried to kill some ents but they escaped.", "You killed some ents.", "The ents fought back but you killed them.", "The ents fought back and escaped."]
food_list = ["Lembas bread", "potato", "mushrooms", "pippin", "fish", "firewood", "coneys"]

while True:
    action_1 = input("What do you want to do? (options: Talk, Smoke, Fight, Quote, Travel, Explore, Inventory, Eat)")
    action = action_1.lower().strip()
    if action == "eat":
        yesno = False
        if "Lembas bread" in inventory:
            answer_ = input("Do you want to eat lembas bread?")
            answer = answer_.lower().strip()
            if answer == "yes":
                print("You ate lembas bread.")
                inventory.remove("Lembas bread")
                yesno = True
            else:
                print("You did not eat lembas bread.")
        if "potato" in inventory:
            answer_ = input("Do you want to eat a potato?")
            answer = answer_.lower().strip()
            if answer == "yes":
                print("You ate the potato.")
                inventory.remove("potato")
                yesno = True
            else:
                print("You did not eat the potato.")
        if "mushrooms" in inventory:
            answer_ = input("Do you want to eat mushrooms?")
            answer = answer_.lower().strip()
            if answer == "yes":
                print("You ate the mushrooms.")
                inventory.remove("mushrooms")
                yesno = True
            else:
                print("You did not eat the mushrooms.")
        if "second breakfast" in inventory:
            answer_ = input("Do you want to eat second breakfast?")
            answer = answer_.lower().strip()
            if answer == "yes":
                print("You ate second breakfast.")
                inventory.remove("second breakfast")
                yesno = True
            else:
                print("You did not eat second breakfast.")
        if "fish" in inventory:
            answer_ = input("Do you want to eat fish?")
            answer = answer_.lower().strip()
            if answer == "yes":
                if "firewood" in inventory:
                    answer_ = input("Do you want to cook the fish?")
                    answer = answer.lower.strip()
                    if answer == "no":
                        print("You ate raw fish and now you are sick.")
                        inventory.remove("fish")
                        yesno = True
                    else:
                        print("You cooked the fish and ate it.")
                        inventory.remove("fish")
                        inventory.remove("firewood")
                        yesno = True
                else:
                    print("You could not cook the fish.")
                    answer_ = input("Do you want to eat raw fish?")
                    if answer == "no":
                        print("You ate raw fish and now you are sick.")
                        inventory.remove("fish")
                        yesno = True
                    else:
                        print("You did not eat fish.")
        if "coneys" in inventory:
            answer_ = input("Do you want to eat coneys?")
            answer = answer_.lower().strip()
            if answer == "yes":
                if "firewood" in inventory:
                    answer_ = input("Do you want to cook the coneys?")
                    answer = answer.lower.strip()
                    if answer == "no":
                        print("You ate raw coneys and now you are sick.")
                        inventory.remove("coneys")
                        yesno = True
                    else:
                        print("You cooked the coneys and ate it.")
                        inventory.remove("coneys")
                        inventory.remove("firewood")
                        yesno = True
                else:
                    print("You could not cook the coneys.")
                    answer_ = input("Do you want to eat raw coneys?")
                    if answer == "no":
                        print("You ate raw coneys and now you are sick.")
                        inventory.remove("coneys")
                        yesno = True
                    else:
                        print("You did not eat coneys.")
        if yesno == False:
            answer_ = input("Do you want to search for food?")
            answer = answer_.lower().strip()
            if answer == "yes":
                food = random.choice(food_list)
                if food == "Lembas bread":
                    print("You saw an elf and he gave you lembas bread.")
                    answer_ = input("Eat it or save it?")
                    answer = answer_.lower().strip()
                    if answer == "eat" or answer == "eat it":
                        print("You ate the Lembas bread.")
                    else:
                        print("You put the Lembas bread in your inventory.")
                        inventory.append("Lembas bread")
                if food == "potato":
                    print("You found a potato")
                    answer_ = input("Eat it or save it?")
                    answer = answer_.lower().strip()
                    if answer == "eat" or answer == "eat it":
                        print("You ate the potato.")
                    else:
                        print("You put the potato in your inventory.")
                        inventory.append("potato")
                if food == "mushrooms":
                    print("You found some mushrooms.")
                    answer_ = input("Eat it or save it?")
                    answer = answer_.lower().strip()
                    if answer == "eat" or answer == "eat it":
                        print("You ate the mushrooms.")
                    else:
                        print("You put the mushrooms in your inventory.")
                        inventory.append("mushrooms")
                if your_character != pippin:
                    if food == "pippin":
                        print("You saw Pippin and he gave you second breakfast.")
                        answer_ = input("Eat it or save it?")
                        answer = answer_.lower().strip()
                        if answer == "eat" or answer == "eat it":
                            print("You ate the second breakfast.")
                        else:
                            print("You put the second breakfast in your inventory.")
                            inventory.append("second breakfast")
                if food == "fish":
                    print("You caught a fish.")
                    answer_ = input("Eat it or save it?")
                    answer = answer_.lower().strip()
                    if answer == "eat" or answer == "eat it":
                        print("You ate the raw fish and now you are sick.")
                    else:
                        print("You put the fish in your inventory.")
                        inventory.append("fish")
                if food == "firewood":
                    print("You did not find food but you found firewood.")
                    print("You put the firewood in your inventory.")
                    inventory.append("firewood")
                if food == "coneys":
                    print("You found some coneys.")
                    answer_ = input("Eat it or save it?")
                    answer = answer_.lower().strip()
                    if answer == "eat" or answer == "eat it":
                        print("You ate the raw coneys and now you are sick.")
                    else:
                        print("You put the coneys in your inventory.")
                        inventory.append("coneys")
            else:
                print("You did not search for food.")
                
                
    if action == "smoke":
        your_character.smoke()
    if action == "talk":
        conversation_1 = input("Who do you want to talk to? (Frodo, Sam, Legolas, Gandalf, Aragorn, Boromir, Arwen, Gollum, Thranduil, Galadriel, Orc, Sauron)")
        conversation = conversation_1.lower().strip()
        dialogue = random.choice(talk_list)
        bad_dialogue = random.choice(bad_talk_list)
        conversation_character = characters[conversation]
        if your_character != sauron:
            if conversation == "frodo":
                your_character.talk_to(frodo, dialogue)
            if conversation == "sam":
                your_character.talk_to(sam, dialogue)
            if conversation == "legolas":
                your_character.talk_to(legolas, dialogue)
            if conversation == "gandalf":
                your_character.talk_to(gandalf, dialogue)
            if conversation == "aragorn":
                your_character.talk_to(aragorn, dialogue)
            if conversation == "boromir":
                your_character.talk_to(boromir, dialogue)
            if conversation == "galadriel":
                your_character.talk_to(galadriel, dialogue)
            if conversation == "arwen":
                your_character.talk_to(arwen, dialogue)
            if conversation == "thranduil":
                your_character.talk_to(thranduil, dialogue)
            if conversation == "sauron" or conversation == "orc" or conversation == "gollum":
                your_character.talk_to(conversation_character, "I will defeat you!")
        else:
            if conversation == "frodo":
                your_character.talk_to(frodo, bad_dialogue)
            if conversation == "sam":
                your_character.talk_to(sam, bad_dialogue)
            if conversation == "legolas":
                your_character.talk_to(legolas, bad_dialogue)
            if conversation == "gandalf":
                your_character.talk_to(gandalf, bad_dialogue)
            if conversation == "aragorn":
                your_character.talk_to(aragorn, bad_dialogue)
            if conversation == "boromir":
                your_character.talk_to(boromir, bad_dialogue)
            if conversation == "sauron":
                your_character.talk_to(sauron, bad_dialogue)
            if conversation == "galadriel":
                your_character.talk_to(galadriel, bad_dialogue)
            if conversation == "arwen":
                your_character.talk_to(arwen, bad_dialogue)
            if conversation == "thranduil":
                your_character.talk_to(thranduil, bad_dialogue)
        if your_character != sauron:
            if conversation_character == sauron or conversation_character == orc:
                conversation_character.talk_to(your_character, random.choice(bad_talk_list))
            elif conversation_character == gollum:
                print("Gollum said: My precious...")
            elif dialogue == "How are you?":
                conversation_character.talk_to(your_character, random.choice(how_are_you))
            else:
                conversation_character.talk_to(your_character, random.choice(talk_list))
        else:
            conversation_character.talk_to(your_character, "I will defeat you!")
    if action == "fight":
        enemy_1 = input("Who do you want to fight? (Frodo, Sam, Legolas, Gandalf, Aragorn, Boromir, Sauron)")
        enemy = enemy_1.lower().strip()
        if enemy == "frodo":
            your_character.fight(frodo)
        if enemy == "sam":
            your_character.fight(sam)
        if enemy == "legolas":
            your_character.fight(legolas)
        if enemy == "gandalf":
            your_character.fight(gandalf)
        if enemy == "aragorn":
            your_character.fight(aragorn)
        if enemy == "boromir":
            your_character.fight(boromir)
        if enemy == "sauron":
            your_character.fight(sauron)
    if action == "quote":
        quoted_1 = input("Who do you want a quote from? (Frodo, Sam, Legolas, Gandalf, Aragorn, Boromir, Arwen, Sauron)")
        quoted = quoted_1.lower().strip()
        if quoted == "frodo":
            print("Frodo said:", random.choice(frodo_quote))
        if quoted == "sam":
            print("Sam said:", random.choice(sam_quote))
        if quoted == "legolas":
            print("Legolas said:", random.choice(legolas_quote))
        if quoted == "gandalf":
            print("Gandalf said:", random.choice(gandalf_quote))
        if quoted == "aragorn":
            print("Aragorn said:", random.choice(aragorn_quote))
        if quoted == "boromir":
            print("Boromir said:", random.choice(boromir_quote))
        if quoted == "sauron":
            print("Sauron said:", random.choice(sauron_quote))
        if quoted == "arwen":
            print("Arwen said:", random.choice(arwen_quote))
        time.sleep(1)
    if action == "travel":
        destination_1 = input("Where do you want to go? (Minas Tirith, Rivendell, The Shire, Mordor, Mirkwood, Fangorn, Rohan)")
        destination = destination_1.lower().strip()
        if destination == "minas tirith":
            your_character.go_to(minas_tirith)
            if your_character == aragorn:
                print("Guard of Gondor said: Welcome home my king!")
            if your_character == boromir:
                print("Guard of Gondor said: Welcome home!")
            if your_character == sauron:
                print("Everyone runs away in terror.")
                kill_human_1 = input("What would you like to do? (Kill, Leave)")
                kill_human = kill_human_1.lower().strip()
                if kill_human == "kill":
                    print(random.choice(kill_human_list))
                else:
                    print("You are leaving Minas Tirith...")
        if destination == "rivendell":
            your_character.go_to(rivendell)
            if your_character == arwen:
                print("Erestor said: Welcome home Lady Arwen.")
            if your_character == sauron:
                print("Everyone runs away in terror.")
                kill_elf_1 = input("What would you like to do? (Kill, Leave)")
                kill_elf = kill_elf_1.lower().strip()
                if kill_elf == "kill":
                    print(random.choice(kill_elf_list))
                else:
                    print("You are leaving Rivendell...")
        if destination == "the shire" or destination == "shire":
            your_character.go_to(shire)
            if your_character == frodo or your_character == sam or your_character == merry or your_character == pippin:
                print("Fatty Bolger said: Welcome home!")
            if your_character == gandalf:
                print("Hobbit children said: Fireworks Gandalf!")
            if your_character == sauron:
                print("Everyone runs away in terror.")
                kill_hobbit_1 = input("What would you like to do? (Kill, Leave)")
                kill_hobbit = kill_hobbit_1.lower().strip()
                if kill_hobbit == "kill":
                    print(random.choice(kill_hobbit_list))
                else:
                    print("You are leaving The Shire...")
        if destination == "mordor":
            your_character.go_to(mordor)
            if your_character == sauron:
                print("Orc said: Welcome home master.")
            else:
                print("Orc said: Get out of here you scum!")
                orc_answer_1 = input("What do you want to do? (Fight, Leave)")
                orc_answer = orc_answer_1.lower().strip()
                if orc_answer == "fight":
                    your_character.fight(orc)
                else:
                    print("You are leaving Mordor...")
        if destination == "mirkwood":
            your_character.go_to(mirkwood)
            if your_character == legolas:
                print("Guard of Mirkwood said: Welcome home prince Legolas!")
            if your_character == sauron:
                print("Everyone runs away in terror.")
                kill_elf_1 = input("What would you like to do? (Kill, Leave)")
                kill_elf = kill_elf_1.lower().strip()
                if kill_elf == "kill":
                    print(random.choice(kill_elf_list))
                else:
                    print("You are leaving Mirkwood...")
        if destination == "fangorn":
            your_character.go_to(fangorn)
            if your_character == merry or your_character == pippin:
                print("Treebeard said: Bru-ra-hoom. Welcome young hobbit.")
            if your_character == sauron:
                print("Everyone runs away in terror.")
                kill_ent_1 = input("What would you like to do? (Kill, Leave)")
                kill_ent = kill_ent_1.lower().strip()
                if kill_ent == "kill":
                    print(random.choice(kill_ent_list))
                else:
                    print("You are leaving Fangorn...")
        if destination == "rohan":
            your_character.go_to(rohan)
            if your_character == merry:
                print("Hama said: Welcome Meriadoc.")
            if your_character == sauron:
                print("Everyone runs away in terror.")
                kill_human_1 = input("What would you like to do? (Kill, Leave)")
                kill_human = kill_human_1.lower().strip()
                if kill_human == "kill":
                    print(random.choice(kill_human_list))
                else:
                    print("You are leaving Rohan...")
    if action == "explore":
        explore_place_1 = input("Where do you want to explore? (Cave or forest)")
        explore_place = explore_place_1.lower().strip()
        if explore_place == "cave":
            cave_list = ["You see something moving. Do you investigate? (Yes or No)", "You see a goblin. Do you fight or escape?"]
            cave_event = random.choice(cave_list)
            print("You went to a cave.")
            cave_choice_1 = input(cave_event)
            cave_choice = cave_choice_1.lower().strip()
            if cave_event == "You see something moving. Do you investigate? (Yes or No)" and cave_choice == "yes":
                moving_thing = random.choice(["The moving thing is Gollum.", "The moving thing is a goblin.", "The moving thing is a Balrog.", "The moving thing is Shelob."])
                if moving_thing == "The moving thing is Gollum.":
                    print(moving_thing)
                    fight_moving_thing_1 = input("Do you want to fight Gollum or leave him?")
                    fight_moving_thing = fight_moving_thing_1.lower().strip()
                    if fight_moving_thing == "yes" or fight_moving_thing == "fight":
                          your_character.fight(gollum)
                    if fight_moving_thing == "no" or fight_moving_thing == "leave" or fight_moving_thing == "leave it":
                        print("You left Gollum.")
                if moving_thing == "The moving thing is a goblin.":
                    print(moving_thing)
                    fight_moving_thing_1 = input("Do you want to fight the goblin or leave it?")
                    fight_moving_thing = fight_moving_thing_1.lower().strip()
                    if fight_moving_thing == "yes" or fight_moving_thing == "fight":
                          your_character.fight(goblin)
                    if fight_moving_thing == "no" or fight_moving_thing == "leave" or fight_moving_thing == "leave it":
                        print("You left the goblin.")
                if moving_thing == "The moving thing is a Balrog.":
                    print(moving_thing)
                    fight_moving_thing_1 = input("Do you want to fight the Balrog or leave it?")
                    fight_moving_thing = fight_moving_thing_1.lower().strip()
                    if fight_moving_thing == "yes" or fight_moving_thing == "fight":
                          your_character.fight(balrog)
                    if fight_moving_thing == "no" or fight_moving_thing == "leave" or fight_moving_thing == "leave it":
                        print("You left the Balrog.")
                if moving_thing == "The moving thing is Shelob.":
                    print(moving_thing)
                    fight_moving_thing_1 = input("Do you want to fight Shelob or leave her?")
                    fight_moving_thing = fight_moving_thing_1.lower().strip()
                    if fight_moving_thing == "yes" or fight_moving_thing == "fight":
                        if "Light of Earendil" in inventory:
                            print("Shelob was scared away by the Light oF Earendil.")
                        else:
                            your_character.fight(shelob)
                    if fight_moving_thing == "no" or fight_moving_thing == "leave" or fight_moving_thing == "leave her":
                        print("You left Shelob.")
            if cave_event == "You see something moving. Do you investigate (Yes or No)?" and cave_choice == "no":
                    print("You left the mysterious thing.")
            if cave_event == "You see a goblin. Do you fight or escape?" and cave_choice == "fight":
                    your_character.fight(goblin)
            if cave_event == "You see a goblin. Do you fight or escape?" and cave_choice == "escape":
                    goblin_attack_list = ["You escaped", "The goblin saw you. Now you must fight."]
                    goblin_attack = random.choice(goblin_attack_list)
                    if goblin_attack == "You escaped":
                        print(goblin_attack)
                    if goblin_attack == "The goblin saw you. Now you must fight.":
                        print(goblin_attack)
                        your_character.fight(goblin)
        if explore_place == "forest":
            print("You went to the forest...")
            forest_list = ["You saw an orc. Do you fight or escape?", "You saw an elf. Do you want to talk to the elf?"]
            forest_event = random.choice(forest_list)
            forest_choice_1 = input(forest_event)
            forest_choice = forest_choice_1.lower().strip()
            if forest_event == "You saw an orc. Do you fight or escape?" and forest_choice == "fight":
                    your_character.fight(orc)
            if forest_event == "You saw an orc. Do you fight or escape?" and forest_choice == "escape":
                    orc_attack_list = ["You escaped", "The orc saw you. Now you must fight."]
                    orc_attack = random.choice(orc_attack_list)
                    if orc_attack == "You escaped":
                        print(orc_attack)
                    if orc_attack == "The orc saw you. Now you must fight.":
                        print(orc_attack)
                        your_character.fight(orc)
            if forest_event == "You saw an elf. Do you want to talk to the elf?" and forest_choice == "yes":
                if your_character == legolas:
                    forest_elf_list = ["Thranduil", "Galadriel", "Haldir"]
                else:
                    forest_elf_list = ["Legolas", "Thranduil", "Galadriel", "Haldir"]
                forest_elf = random.choice(forest_elf_list)
                print("The elf is", forest_elf)
                dialogue = random.choice(talk_list)
                if forest_elf == "Thranduil":
                    your_character.talk_to(thranduil, dialogue)
                    if dialogue == "How are you?":
                        thranduil.talk_to(your_character, random.choice(how_are_you))
                    else:
                        thranduil.talk_to(your_character, random.choice(talk_list))
                if forest_elf == "Galadriel":
                    your_character.talk_to(galadriel, dialogue)
                    if dialogue == "How are you?":
                        galadriel.talk_to(your_character, random.choice(how_are_you))
                    else:
                        galadriel.talk_to(your_character, random.choice(talk_list))
                if forest_elf == "Haldir":
                    your_character.talk_to(haldir, dialogue)
                    if dialogue == "How are you?":
                        haldir.talk_to(your_character, random.choice(how_are_you))
                    else:
                        haldir.talk_to(your_character, random.choice(talk_list))
                    print("Haldir gave you some Lembas bread.")
                    inventory.append("Lembas bread")
                if forest_elf == "Legolas":
                    your_character.talk_to(legolas, dialogue)
                    if dialogue == "How are you?":
                        legolas.talk_to(your_character, random.choice(how_are_you))
                    else:
                        legolas.talk_to(your_character, random.choice(talk_list))
                    print("Legolas gave you some Lembas bread.")
                    inventory.append("Lembas bread")
                    
    if action == "inventory":
        print(inventory)
                
                
            
                
    time.sleep(1)
