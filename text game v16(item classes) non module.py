gameInProgress = '1' 

import random
import sys

class Location: # creates location class
    def __init__(self,aString,aString2,aString3,aString4):
        self.items = aString
        self.exits = aString2
        self.name = aString3
        self.NPCs = aString4

        roomsList.append(self)
        print "------------------------------------------------------------------------------"
        print self.name + "created"
        print self
        print "------------------------------------------------------------------------------"
        
    def printAttributes(self):
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
            self.locked = false

        elif self.random == 1:
            self.locked = true

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
                if item == x.name:
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
            if item == x.name:
               print "you dropped" + x.name
               self.items.remove(x)
               self.room.items.append(x)
               self.room.printAttributes()

    def eat (self, item):
        self.items.remove(item)
        print "you ate " + item.name
        print "it was "  + item.tastiness
        print "----------------------------------------------------------------------------"
        

    def talk (self, target, targetName):
        print "----------------------------------------------------------------------------"
        print "----------------------------------------------------------------------------"
        print '"hi, ' + 'my name is ' + targetName + ','
        print target.greeting + '"'
        print "----------------------------------------------------------------------------"
        print "----------------------------------------------------------------------------"

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
        
        playerreply = raw_input("what would you like to do")

        if playerreply == 'pickup':
            
            if not self.room.items:
                print "no items in room"

            else:
                print "pickup what"
                for x in  self.room.items:
                    print x.name
                self.pickup(raw_input(), self.room.items)
            return

        if playerreply == 'drop':
            print "drop active"
            self.drop(raw_input("drop what"), self.items)
            return

        if playerreply == 'eat':
            print 'eat what?'
            print 'options'
            for x in self.items:
                if isinstance(x,Food):
                    print x.name
                    
            playerreply = raw_input()
            
            if playerreply == x.name: 
                self.eat(x)
                return
            else:
                print "you don't have that"
                return
                

        if playerreply == 'talk':
            print "who to?"
            print "options:"
            for x in self.room.NPCs:
                print x.name
            
            playerreply = raw_input()

            for x in self.room.NPCs:
                print "checking talk target"
                if x.name == playerreply:
                    self.talk(x,x.name)
                    return

        if playerreply == 'steal':
            
            print "options:"
            for x in self.room.NPCs:
                print x.name

            playerreply = raw_input("steal from who?")

            if playerreply == x.name:
                print "steal what?"
            else:
                print "no-one by that name here"

            for i in x.items:
                print "options:"
                print i.name

            itemChoice = raw_input ()
            
            if itemChoice == i.name:
                self.steal(x,x.name,itemChoice)
                return
            else:
                print "they don't have that item"
                return


        if playerreply == 'leave':
            print "which exit?"
            for x in self.room.exits:
                print x.name

            playerreply = raw_input()

            for x in self.room.exits:
                if playerreply == x.name:
                    if x.locked == False:
                        self.exitRoom (x.roomA,x.roomB)
                        return

                    elif x.locked:
                        for i in self.items:
                            if i.name == 'key':
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
            playerreply = raw_input("are you sure?")
            if playerreply == 'yes':
                self.exitGame()
            if playerreply == 'no':
                print "ok"
                return
            

        if playerreply == 'help':
            player1.playerHelp()
        
        elif playerreply == 'blah':
            print "blah to you too"

        else:
            print "i don't understand that yet, sorry"

class NPC:
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

player1.printAttributes()



## Main game loop  >>>>>>>>>
while gameInProgress == '1':
        
    print  "game loop active" 
    player1.playerReply ()  # this handles the player's reply


    





