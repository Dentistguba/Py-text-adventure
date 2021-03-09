gameInProgress = 1

##External modules>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import random # allows use of random number generator
import sys
import string
import os

##Colour text function (defaults first)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_WHITE = 0x07
FOREGROUND_BLACK = 0x00
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_WHITE = 0x70
BACKGROUND_BLACK = 0x00
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

import ctypes

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


#def windowColour(string):
#       os.system(string [0])
#       print string [1]

def printUnicode(string = 'ѦѦѦѦ i am a unicode string ѦѦѦѦ'):
    string.encode('utf-8')
    print string
    
#Prints lines>>>>>>>>>>>>>>>>>
def printDivider():
    print "------------------------------------------------------------------------------"
    print "------------------------------------------------------------------------------"

def startScreen():
    set_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
    print "                ______                                "
    print "============   | _____|  \\\     //  ============     "
    print "     ||        ||         \\\   //        ||          "
    print "     ||        ||___       \\\ //         ||          "
    print "     ||        | ___|       \\//          ||          "
    print "     ||        ||           /\\\          ||          "
    print "     ||        ||_____     // \\\         ||          "    
    print "     ||        |______|   //   \\\        ||          "
    print "___________________________________________________   "
    print "         ____________________________                 "
    print "                 _______________                      "
    print "                  ____                         _________     ____     __                        ___      ___          "    
    print "      /\         |   \\\      \            /   |  _______|   |    \   |  |    ==============    |   |    |   |        "    
    print "     /  \        |    \\\      \          /    | |           |  \  \  |  |          ||          |   |    |   |        "
    print "    /____\       |     ||      \        /     | |____       |  |\  \ |  |          ||          |   |    |   |        "
    print "   /      \      |     ||       \      /      |  ____|      |  | \  \|  |          ||          |   |    |   |        "
    print "  /        \     |     ||        \    /       | |           |  |  \     |          ||          |   |    |   |                      "
    print " /          \    |     ||         \  /        | |_______    |  |   \    |          ||          |   |____|   |                      "
    print "/            \   |____//           \/         |_________|   |  |    \___|          ||          \____________/"
    set_color(FOREGROUND_WHITE | BACKGROUND_BLACK)




## Classes>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##__________________________________________________________________________________________
class Location: # creates location class
    def __init__(self,aString,aString2,aString3,aString4): #constructor
        self.items = aString                               #items in room
        self.exits = aString2                              #exits associated with room
        self.name = aString3                               #"Friendly name" of room
        self.NPCs = aString4                               #NPC's in room

        roomsList.append(self)                             #adds room to list of total rooms
        print "------------------------------------------------------------------------------"
        print self.name + "created"                        #
        print self                                         #prints instance reference (for debug)
        print "------------------------------------------------------------------------------"
        
    def printAttributes(self):                             #prints imp info about instance
        print self.name + ","
        print ""
        print "which contains objects:"

        for x in self.items:
            print x.name 

        print ""
        print "Characters:"

        for x in self.NPCs:
            print x.name 
        
        
        print ""
        print "and has exits:"
        for x in self.exits:
            print x.name 

        print "------------------------------------------------------------------------------"
        print "------------------------------------------------------------------------------"
        
    def returnItems():
        return self.items
    
class Exit: # creates location class
    def __init__(self,aString,aString2,aString3,aString4,aString5,aBool=bool):
        
        self.roomA =      aString
        self.roomAName = aString2
        self.roomB =      aString3
        self.roomBName = aString4
        self.name =       aString5
        self.locked = aBool

        exitsList.append(self)

        print "exit created:"        
        print self
        print "between rooms:"
        print self.roomA
        print self.roomAName
        print ""
        print "and"
        print self.roomB
        print self.roomBName
        print "------------------------------------------------------------------------------"

        
    def printAttributes(self):
        print self.roomA
        print self.roomB
        print self.locked 

        
        self.random = random.randint (0,1)
        if self.random == 0:
            self.locked = False

        elif self.random == 1:
            self.locked = True

        print self.roomA

class Player: # creates player class
    def __init__(self,listA,stringA):
        self.items = listA
        self.room = stringA
        self.help = ["general", "commands"]

        print "player created"
        print ""
                
    def printAttributes(self):
        print "------------------------------------------------------------------------------"

        print "you have:"
        for x in self.items:
            print x.name
        print ""
        print "you are in:"
        print self.room.name
        print ""

        print "the room contains"
        print "items:"
        for x in self.room.items:
            print x.name
        print ""
        
        print "characters:"
        for x in self.room.NPCs:
            print x.name
        print ""

        print "and exits:"
        for x in self.room.exits:
            print x.name

        print "------------------------------------------------------------------------------"
            

    def pickup (self, item, itemlist):
            for x in itemlist:
                if item == string.lower(x.name):
                    print "------------------------------------------------------------------------------"
                    print "------------------------------------------------------------------------------"

                    print "you took " + item
                    print ""
                    print "<inventory:>"
                    self.items.append(x)
                    self.room.items.remove(x)

                    for x in self.items:
                        print x.name
                    print "------------------------------------------------------------------------------"
                    print "------------------------------------------------------------------------------"
                    return
            else:
                print item + "? none of that here i'm afraid"
                return

    def drop (self, item, itemlist):
        for x in itemlist:
            if item == string.lower(x.name):
               print "you dropped" + x.name
               self.items.remove(x)
               self.room.items.append(x)
               self.room.printAttributes()

    def eat (self, item):
        self.items.remove(item)
        print "you ate " + item.name
        print "it was "  + item.tastiness
        print "----------------------------------------------------------------------------"
        

    def talk (self, target):
        target.talk()

    def steal (self, target, targetName, item):
        
        print "----------------------------------------------------------------------------"
        print "----------------------------------------------------------------------------"
        print "you stole"

        for x in target.items:
            if x.name == item:
                target.items.remove (x)
                self.items.append (x)
                print x.name

        print "<inventory:>"
        for x in self.items:
            print x.name
        
        print "----------------------------------------------------------------------------"
        print "----------------------------------------------------------------------------"        
        

    def exitRoom (self,roomA,roomB):

        print "room exited"
        if self.room == roomA:
            self.room = roomB

        elif self.room == roomB:
            self.room = roomA
        print "you are in"
        self.room.printAttributes()
        
    
               
    def playerHelp(self):
        print "------------------------------------------------------------------------------"
        print "------------------------------------------------------------------------------"
        print "options below:"
        for x in player1.help:
            print x + '.'
        print ""
        playerreply = raw_input("what help do ya need?")

        if playerreply == 'general':
            print "this is a text based adventure game."
            print "to play type in commands"
            
        if playerreply == 'commands':
            print "following commands can be used (shown in square brackets)"
            print "[pickup]" "----" "picks up object from room, enter name of object when prompted"
            print "[drop]" "----" "drops object from room, enter name of object when prompted"
            print "[help]" "----" "this is the help"

        print "------------------------------------------------------------------------------"
        print "------------------------------------------------------------------------------"

    def exitGame(self):
        print "bye"
        sys.exit()
        
    def playerReply(self):
        set_color(FOREGROUND_WHITE | BACKGROUND_BLUE)
        print "What would you like to do?"
        set_color(FOREGROUND_GREEN | BACKGROUND_BLACK)
        playerreply = string.lower(raw_input())

        if playerreply == 'pickup':

            set_color(FOREGROUND_WHITE)
            if not self.room.items:
                print "no items in room"

            else:
                print "pickup what"
                for x in  self.room.items:
                    print x.name
                set_color(FOREGROUND_GREEN)
                self.pickup (string.lower(raw_input()), self.room.items)
            return

        if playerreply == 'drop':
            set_color(FOREGROUND_WHITE)
            print "drop what?"
            print "options:"

            for x in self.items:
                print x.name
                
            set_color(FOREGROUND_GREEN)
            playerreply = string.lower(raw_input())
            set_color(FOREGROUND_WHITE)

            for x in self.items:
                if x.name == playerreply:
                    self.drop(playerreply, self.items)
                    return
            else:
                print "you don't have that"
                return

        if playerreply == 'eat':
            for x in self.items:
                if isinstance(x,Food):
                    hasFood = True

            if hasFood == True:        
                print 'eat what?'
                print 'options'
                for x in self.items:
                    if isinstance(x,Food):
                        print x.name
                    
                playerreply = string.lower(raw_input())
                for x in self.items:
                    
                    if playerreply == string.lower(x.name): 
                        self.eat(x)
                        return
                else:
                    print "you don't have that"
                    return
            else:
                print "no food in inventory"
                return
                

        if playerreply == 'talk':
            if self.room.NPCs:
                print "who to?"
                print "options:"
                for x in self.room.NPCs:
                    print x.name
                
                playerreply = string.lower(raw_input())

                for x in self.room.NPCs:
                    if string.lower(x.name) == playerreply:
                        self.talk(x)
                        return
                else:
                    print "no one here by that name"
                    return

        if playerreply == 'steal':
            
            print "options:"
            for x in self.room.NPCs:
                print x.name

            playerreply = string.lower(raw_input("steal from who?"))
            
            for x in self.room.NPCs:
                if playerreply == string.lower(x.name):
                    
                    print "steal what?"

                    for i in x.items:
                        print "options:"
                        print i.name

                    itemChoice = string.lower(raw_input ())
                
                    for i in x.items:
                        if itemChoice == string.lower(i.name):
                            self.steal(x,x.name,itemChoice)
                            return
                    else:
                        print "they don't have that item"
                        return

            else:
                print "no-one by that name here"
                return




        if playerreply == 'leave':
            print "which exit?"
            for x in self.room.exits:
                print x.name

            playerreply = string.lower(raw_input())

            for x in self.room.exits:
                if playerreply == string.lower(x.name):
                    if x.locked == False:
                        self.exitRoom (x.roomA,x.roomB)
                        return

                    elif x.locked:
                        for i in self.items:
                            if i.name == string.lower('key'):
                                self.items.remove (i)
                                self.exitRoom (x.roomA,x.roomB)
                                x.locked = False
                                return
                                

                        else:
                            print "exit is locked"
                            print "------------------------------------------------------------------------------"           
                            print "------------------------------------------------------------------------------"
                            return
            else:
                print "that is not an exit"
                return
            return

        if playerreply == 'exit':
            playerreply = string.lower(raw_input("are you sure?"))
            if playerreply == 'yes':
                self.exitGame()
            if playerreply == 'no':
                print "ok"
                return
            

        if playerreply == 'help':
            player1.playerHelp()
        
        elif playerreply == 'blah':
            print "blah to you too"

        elif playerreply == 'fly':
            print "i'm afraid you don't have that ability"

        elif playerreply == 'get rich':
            print "don't we all, i'm afraid it won't be that easy"

        elif playerreply == 'play WOW'or playerreply == 'play world of warcraft':
            print "i wouldn't bother if i were you, warcraft 3 is much better"

        elif playerreply == 'enchant':
            print "what do you think this is, Morrowind?"

        elif playerreply == 'unify italy':
            print "that has been done"

        elif playerreply == 'play conker' or playerreply =='play conkers bad fur day':
            print "good choice sir, sadly that game doesn't exist here"

        elif playerreply == 'dunno' or playerreply == 'not sure' or playerreply == 'dont know':
            print "well you'll have to decide soon, try the help"

        elif playerreply == '':
            print "it appears you did not type anything"

        else:
            print "i don't understand that yet, sorry"

class NPC(object):
    def __init__(self,aString1,aString2,aString3,aString4):
        self.name = aString1
        self.items = aString2
        self.room = aString3
        self.greeting = aString4

        self.room.NPCs.append(self)
        charList.append(self)

    def printAttributes(self):
        print self.name
        print self.items
        print self.greeting

    def talk(self):
        print "------------------------------------------------------------------------------"
        print "------------------------------------------------------------------------------"

        print "hi my name is"
        print self.name + ","
        print self.greeting

        print "------------------------------------------------------------------------------"
        print "------------------------------------------------------------------------------"

        

class QuestNPC(NPC):
    def __init__(self,parentArgs,quests = {}):
        (a,b,c,d) = parentArgs[:4]

        super(NPC,self).__init__(a,b,c,d)
        self.quests = quests

    def questTalk():
        for x in self.quests:
            print x
        

    def talk(self):
        super(NPC,self).talk
        questTalk(self)
        printDivider()

class Quest(object):
    def __init__(self,name,description,complete = False):
        pass
        
        
    

class Item(object):
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.superClass = 'Item'

        itemList.append (self)

        print 'item created'
        print self

    def printAttributes(self):
        print self.name
        print self.description


class Food (Item):
    def __init__(self,parentArgs,tastiness = 'tasty'):
        (a,b) = parentArgs[:2]
            
        super(Food, self).__init__(a,b)
        self.tastiness = tastiness
        self.superClass = 'Food'

        print 'food'
        print self

        
    def eat(self):
        print self.name
        print self.description
        print self.tastiness
        print "eaten"
        
    

# Map creation >>>>>>
# instances are constructed below (and added to appropriate lists)
exitsList = []
exit1 = Exit (1,"room1",2,"room2",'exit 1',False)
exit2 = Exit (1,"room1",3,"room3",'exit 2',True)

itemList = []
cheese = Food (['cheese','this is cheese'])
plant = Item ('plant','this is a plant')
statuette = Item ('statuette','this is a weathered bronze statue')
key = Item ('key','this is a key')

eggs = Food(['eggs','these are some eggs'],'horrible')

roomsList = []
room1 = Location ([cheese], [exit1,exit2], "room 1",[])
room2 = Location ([plant], [exit1], "room 2",[])
room3 = Location ([statuette],[exit2],"room 3",[])

room1.printAttributes()
room2.printAttributes()

exit1.roomA = room1
exit1.roomB = room2
exit2.roomA = room1
exit2.roomB = room3

# NPC creation >>>>>>
charList = []
char1 = NPC ("jim",[eggs],room1,"ain't seen you round here before")
char2 = NPC ("bob",['bacon'],room2,"got ma cheese whizz boi?")
char3 = NPC ("archduke blahoof",['deed of ownership of the land'],room3,"good day citizen")
print "the characters in the world are"
for x in charList:
    print x.name

print "------------------------------------------------------------------------------"

# Player creation >>>>>>
# player instance = Player parent ([inventory],starting room)
player1 = Player ([cheese,key],room1)


startScreen()
player1.printAttributes()


## Main game loop  >>>>>>>>>
while gameInProgress == 1:
    set_color(FOREGROUND_WHITE)
    printDivider()
    print "game loop active"
    printUnicode (u"☭☭☭☭☭☭☭☭☭☭☭☭☭")
    printUnicode (u" ຝ  ")
    printUnicode (u" Ж")
    player1.playerReply ()  # this handles the player's reply


    





