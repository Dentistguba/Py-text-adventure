class Player: # creates player class
    def __init__(self):
        self.items = ["cards", "biscuits"]
        self.room = 'room1'
        self.help = ["general", "commands"]

        print "player created"
        print ""
                
    def printAttributes(self):

        print "you have:"
        for x in self.items:
            print x
        print ""
        print "you are in room"
        print self.room

    def pickup (self, item, itemlist):
            for x in itemlist:
                if item == x:
                    print "you took " + item
                    self.items.append(item)
                    self.room.items.remove(item)
                    print self.items
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
               
    def playerHelp(self):
        print "------------------------------------------------------------------------------------"
        print "------------------------------------------------------------------------------------"
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

        print "-------------------------------------------------------------------------------------"
        print "------------------------------------------------------------------------------------"
        
    def playerReply(self):
        
        playerreply = raw_input("what would you like to do")

        if playerreply == 'pickup':
            print "pickup active"
            self.pickup(raw_input("pickup what?"), self.room.items)
            return

        if playerreply == 'drop':
            print "drop active"
            self.drop(raw_input("drop what"), self.items)
            return

        if playerreply == 'help':
            player1.playerHelp()
        
        elif playerreply == 'blah':
            print "blah to you too"

        else:
            print "i don't understand that yet, sorry"
