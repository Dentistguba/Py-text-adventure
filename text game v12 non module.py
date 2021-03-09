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
        
        print self.name + "created"
        print self
        print "------------------------------------------------------------------------------"
        
    def printAttributes(self):
        print self.name + " contains objects:"
        print ""

        for x in self.items:
            print x + ","

        print ""
        print "Characters:"

        for x in self.NPCs:
            print x 
        
        
        print ""
        print "and has exits:"
        print ""
        for x in self.exits:
            print x 

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
            print x
        print ""
        print "you are in:"
        print self.room.name
        print ""

        print "the room contains"
        print "items:"
        for x in self.room.items:
            print x
        print ""
        print "and characters:"
        for x in self.room.NPCs:
            print x.name

        print "------------------------------------------------------------------------------"
            

    def pickup (self, item, itemlist):
            for x in itemlist:
                if item == x:
                    print "------------------------------------------------------------------------------"
                    print "------------------------------------------------------------------------------"

                    print "you took " + item
                    print ""
                    print "<inventory:>"
                    self.items.append(item)
                    self.room.items.remove(item)
                    print self.items
                    print "------------------------------------------------------------------------------"
                    print "------------------------------------------------------------------------------"
                    return
            else:
                print item + "? none of that here i'm afraid"
                return

    def drop (self, item, itemlist):
        for x in itemlist:
            if item == x:
               print "you dropped" + item
               self.items.remove(item)
               self.room.items.append(item)
               self.room.printAttributes()

    def talk (self, target, targetName):
        print "----------------------------------------------------------------------------"
        print "----------------------------------------------------------------------------"
        print '"hi' + 'my name is ' + targetName + ','
        print target.greeting + '"'
        print "----------------------------------------------------------------------------"
        print "----------------------------------------------------------------------------"

    def steal (self, target, targetName, item):
        
        print "----------------------------------------------------------------------------"
        print "----------------------------------------------------------------------------"
        print "you stole"

        target.items.remove (item)
        self.items.append (item)
        print item

        #testing stuff
        print target.items
        print self.items
        
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
                    print x
                self.pickup(raw_input(), self.room.items)
            return

        if playerreply == 'drop':
            print "drop active"
            self.drop(raw_input("drop what"), self.items)
            return

        if playerreply == 'talk':
            playerreply = raw_input("who to?")

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

                    for i in x.items:
                        print "options ?"
                        print i
                        itemChoice = raw_input ()
                        if itemChoice == i:
                            self.steal(x,x.name,itemChoice)

            return

        if playerreply == 'leave':
            for x in exitsList:
                print x.name

            playerreply = raw_input("which exit?")

            for x in exitsList:
                if playerreply == x.name:
                    if x.locked == False:
                        self.exitRoom (x.roomA,x.roomB)

                    elif x.locked:
                        for i in self.items:
                            if i == 'key':
                                self.items.remove (i)
                                self.exitRoom (x.roomA,x.roomB)
                                return

                            else:
                                print "exit is locked"
                                print "------------------------------------------------------------------------------"           
                                print "------------------------------------------------------------------------------"
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

# Map creation >>>>>>
# instances are constructed below (and added to appropriate lists)
exitsList = []
exit1 = Exit (1,"room1",2,"room2",'exit 1',False)
exit2 = Exit (1,"room1",3,"room3",'exit 2',True)

roomsList = []
room1 = Location (["cheese","tree","monkey"], [exit1], "room 1",[])
room2 = Location (["plant","painting"], [exit1], "room 2",[])
room3 = Location (["win","awesome"],[exit2],"room 3",[])

room1.printAttributes()
room2.printAttributes()

exit1.roomA = room1
exit1.roomB = room2
exit2.roomA = room1
exit2.roomB = room3

# NPC creation >>>>>>
charList = []
char1 = NPC ("jim",['eggs'],room1,"ain't seen you round here before")
char2 = NPC ("bob",['bacon'],room2,"got ma cheese whizz boi?")
char3 = NPC ("archduke blahoof",['deed of ownership of the land'],room3,"good day citizen")
print "the characters in the world are"
for x in charList:
    print x.name

print "------------------------------------------------------------------------------"

# Player creation >>>>>>
player1 = Player (['key','cards'],room1)

player1.printAttributes()



## Main game loop  >>>>>>>>>
while gameInProgress == '1':
        
    print  "game loop active" 
    player1.playerReply ()  # this handles the player's reply


    





