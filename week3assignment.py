# WELCOME TO CHUPUTLUH
# Written in Python 3

# At the top of the file are declarations and variables needed.

# Scroll to the bottom and look for the main() function, that is
# where the program logic starts.

import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)

# an object describing our player
player = {
    "name": "p1",
    "lives": 3,
    "items" : [],
    "friends" : []
}

def printGraphic(name):
    if (name == "dog"):
        print ('        /\__/\                    ')
        print ('       / .   .    Woof!           ')
        print ('       |    <>            _       ')
        print ('       |   _/\ -----____  | |     ')
        print ('      /               `_| |      ')
        print ('   ___/_       ___|   |___/       ')
        print ('  /_/_____/____/_______|          ')
    
    if (name == "gem"):

        print ('        _______       ')
        print ('       /       )      ')
        print ('      /_____   |      ')
        print ('     ( .    ) /       ')
        print ('     |   . | /        ')
        print ('     |_____|/         ')



def escapeIsland():
    print("-------------------------------")
    print("You suddenly regain consciousness and find yourself lying in a bed in an unrecognizable wooden cabin. " \
    "Sitting up, you see " + str(player["lives"]) + " black rings around your left arm. " \
    "Lying back down, you close your eyes and try to remember how you got there.")
    input("press enter >")
    print("-------------------------------")
    print(" Is this a dream? Should you open your eyes or just try and go back to sleep?")
    print("options: [ open eyes , sleep ]")

    pcmd = input(">")

    while True:
        if (pcmd == "open eyes"):
            print("-------------------------------")
            print("You open your eyes again to see a man with a knife standing over you")
            print("You quickly roll off the bed to a standing position facing him.")
            print("What do you do next?")
            print("options: [ fight man , run away ] ")
            pcmd = input(">")

            while True:
                if (pcmd == "fight man"):
                    print("-------------------------------")
                    print("You grab an arrow lying on the ground and fling it at the man")
                    print("As soon as the arrow hits him, he disappears in a poof of dust. Weird.")
                    input("press enter >")
                    print("-------------------------------")
                    print("Nervous about staying in the cabin, you leave and head towards the woods nearby.")
                    print("Stopping for a moment, you close your eyes and take a deep breath.")
                    input("press enter >")
                    meet_stranger()
                    break
                elif (pcmd == "run away"):
                    print("-------------------------------")
                    print("You make a break for the nearest door and find yourself heading towards a wall of trees")
                    print("You run deep into the forest until you've finally lost the man, you close your eyes and take a deep breath.")
                    input("press enter >")
                    meet_stranger()
                    break
                else:
                    print("choice unclear, pick what you want to do next")
                    print("options: [ fight man, run away] ")
                    pcmd = input(">")
                    continue
            break

        elif (pcmd == "sleep"):
            print("-------------------------------")
            print("You sudden feel blinding pain and open your eyes to see someone standing over you with a knife" \
            " You've been stabbed in the chest.")
            lose_life()
            input("press enter >")
            escapeIsland()
            break

        else:
            print("choice unclear, pick what you want to do next")
            print("options: [ open eyes , sleep ]")
            pcmd = input(">")
            continue


def meet_stranger():
    print("-------------------------------")
    print("When you open your eyes, you see someone in the distance sawing a tree")
    input("press enter >")
    print("-------------------------------")
    print("How do you react to the stranger?")
    print("options: [ talk , ignore ] ")
    pcmd = input(">")
    
    while True:
        if (pcmd == "talk"):
            print("-------------------------------")
            print("You say hi to the man. He turns towards you and smiles.")
            input("press enter >")
            print("-------------------------------")
            print("'Hey, I'm Joe! Welcome to Island Chuhputluh, hope you make it out of here with all your rings!'")
            print("'And when in doubt, right is always right.' After speaking, Joe turns back to sawing the tree")
            input("press enter >")
            print("-------------------------------")
            print("'You're not too sure what he means but you smile and continue on, heading down an increasingly dim path until you can't see anything.")
            input("press enter >")
            forest_trail()
            break
        elif (pcmd == "ignore"):
            print("-------------------------------")
            print("You decide to walk past the stranger without saying anything, heading down an increasingly dim path until you can't see anything.")
            input("press enter >")
            forest_trail()
            break
        else:
            print("choice unclear, pick what you want to do next")
            print("options: [ talk , ignore ] ")
            pcmd = input(">")
            continue


def forest_trail():
    print("-------------------------------")
    print("A ray of sunshine suddenly beams down on you. You look around and find yourself at a crossroads.")
    print("Looking down at your arm, you see " + str(player["lives"]) + " rings printed on it.")
    input("press enter >")
    print("-------------------------------")
    print("There are two paths before you going left and right.")
    print("Which path would you like to take? Or do you want to rest for a bit?")
    print("options: [ left , right, rest ] ")
    pcmd = input(">")

    while True:
        if (pcmd == "right"):
            print("-------------------------------")
            print("You take the path on the right")
            input("press enter >")
            print("-------------------------------")
            print("As you are walking, you hear a large crack.")
            print("The last see you see is a huge oak tree crashing down on you.")
            lose_life()
            input("press enter >")
            city_scene()
            break
        elif (pcmd == "left"):
            print("-------------------------------")
            print("You take the path on the left and continue into an open plain")
            input("press enter >")
            city_scene()
            break
        elif (pcmd =="rest"):
            if ("bone" in player["items"]):
                print("-------------------------------")
                print("You rest some more, but nothing happens")
                input("press enter >")
            else:
                print("-------------------------------")
                print("While resting, you see a bone on the ground nearby. You pick it up and put it in your pocket.")
                player["items"].append("bone")
                input("press enter >")
            print("You've rested, what do you want to do next?")
            print("options: [ left , right, rest ] ")
            pcmd = input(">")
            continue
        else:
            print("choice unclear, pick what you want to do next")
            print("options: [ left , right ] ")
            pcmd = input(">")
            continue

def city_scene():
    print("-------------------------------")
    print("There's a flash of light and suddenly you're at the entrance of a bustling city market")
    print("You glance down at your arm and see " + str(player["lives"]) + " rings printed there")
    input("press enter >")
    print("-------------------------------")
    print("As you continue down the winding cobblestone roads, you sense someone is following behind you.")
    input("press enter >")
    print("-------------------------------")
    print("Do you turn back to see who it is or do you try and lose them in the crowd?")
    print("options: [ turn around, lose them ] ")
    pcmd = input(">")

    while True:
        if (pcmd == "turn around"):
            print("-------------------------------")
            print("You stop walking and slowly turn around.")
            input("press enter >")
            printGraphic("dog")
            print("It's a dog! He looks hungry, do you want to give him food?")
            input("press enter >")

            if ("bone" in player["items"]):
                print("options: [ give bone, ignore dog ]")
                pcmd = input(">")
                
                while True:
                    if (pcmd == "give bone"):
                        print("-------------------------------")
                        print("You give the dog the bone in your pocket. He wags his tail and keeps following you.")
                        player["friends"].append("dog")
                        input("press enter >")
                        food_market()
                        break
                    elif (pcmd == "ignore dog"):
                        print("-------------------------------")
                        print("You ignore the dog and keep walking. He walks away to sniff some trash.")
                        input("press enter >")
                        food_market()
                        break
                    else:
                        print("choice unclear, pick what you want to do next")
                        print("options: [ give bone , ignore dog ] ")
                        pcmd = input(">")
                        continue
                break
    
            else:
                print("-------------------------------")
                print("Oh wait! You don't have any food on you. The dog walks away to sniff some trash")
                input("press enter >")
                food_market()
        
        elif (pcmd == "lose them"):
            print("-------------------------------")
            print("You twist and turn into the crowd until the feeling of someone following you goes away.")
            input("press enter >")
            food_market()
            break
        else:
            print("choice unclear, pick what you want to do next")
            print("options: [ turn around, lose them ] ")
            pcmd = input(">")
            continue


def food_market():
    print("-------------------------------")
    print("You find yourself in a part of the city with many food vendors and booths selling various items.")
    print("Looking down at your arm, you see " + str(player["lives"]) + " rings printed.")
    input("press enter >")
    print("-------------------------------")
    print("You're getting really hungry and see a tasty loaf of bread at one of the stalls.")
    printGraphic("bread")
    input("press enter >")
    print("Buy the bread?")
    print("options: [ buy bread , pass ]")
    pcmd = input(">")

    while True:
        if (pcmd == "buy bread"):
            if "dog" in player["friends"]:
                print("-------------------------------")
                print ("As you reach for the loaf of bread, the stray dog following you starts to growl and tugs on your clothes.")
                print ("A strange feeling washes over you and you decide to pass on the bread and continue on.")
                input("press enter >")
                print("-------------------------------")
                print ("As you're leaving you glance behind the booth and are shocked to see a number of dead mice lying on top of half eaten pieces of bread.")
                input("press enter >")
                final_door()
            else:
                print("-------------------------------")
                print ("You buy the bread and start eating it. You begin to feel faint and fall to the ground.")
                lose_life()
                input("press enter >")
                final_door()
            break
        elif (pcmd == "pass"):
            print("-------------------------------")
            print ("You decide you're actually fine without the bread and continue walking down the street.")
            input("press enter >")
            final_door()
            break
        else:
            print("choice unclear, pick what you want to do next")
            print("options: [ buy bread , pass ] ")
            pcmd = input(">")
            continue

def final_door():
    print("-------------------------------")
    print("You suddenly find yourself at a door and in front of it is a table with a dice on top. You pick it up.")
    print("You feel an instinctive need to look down at your hands and see " + str(player["lives"]) + " rings printed on your left arm.")
    input("press enter to roll the dice >")

    difficulty = 5
    chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

    # if the roll is higher than 5... 75% chance
    if (chanceRoll >= difficulty):
        print("-------------------------------")
        print ("The door opens and you walk through it")
        input("press enter >")
        gameOver()
    else:
        print("-------------------------------")
        print ("The door opens and a stick of dynamite rolls at your feet and explodes.")
        lose_life()
        final_door()


def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))

    if (result <= difficulty):
        print ("trying again....")
        
        input("press enter >")
        rollDice(minNum, maxNum, difficulty) # this is a recursive call

    return result

def lose_life():
    player["lives"] -= 1

    if (player["lives"] <= 0):
        player["lives"] = 3
        escapeIsland()
    else:
        print("You feel yourself blacking out and lose consciousness.")

def gameOver():

    print("-------------------------------")
    print("You suddenly find yourself back in the library.")
    print("You look at the book in your hands and slowly put 'Island of Chuhputluh' back on the shelf.")
    return

# main! most programs start with this.
def main():
    # printGraphic("title") - call the function to print an image
    escapeIsland()

main() # this is the first thing that happens
