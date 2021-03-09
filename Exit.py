import random

class Exit: # creates location class
    def __init__(self,aString,aString2):
        self.roomA = aString
        self.roomB = aString2

        printAttributes (self)
        
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
