class Location: # creates location class
    def __init__(self,aString,aString2,aString3):
        self.items = aString
        self.exits = aString2
        self.name = aString3
        print self.name + "created"
        print self
        print "------------------------------------------------------------------------------"
        
    def printAttributes(self):
        print self.name + " contains:"
        print ""

        for x in self.items:
            print x + ","    
        
        print ""
        print "and has exits:"
        print ""
        for x in self.exits:
            print x + ","

        print "------------------------------------------------------------------------------"
        
    def returnItems():
        return self.items
