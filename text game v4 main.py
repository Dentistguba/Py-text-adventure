from Location import Location
from Exit import Exit
from Player import Player
import random

room1 = Location (["cheese","tree","monkey"], ["north"], "room 1")
room2 = Location (["plant","painting"], ["south"], "room 2")

exit1 = Exit ()


room1.printAttributes()
room2.printAttributes()

player1 = Player ()

player1.printAttributes()

while player1.room == room1:
        
    print "game loop active"
    player1.playerReply ()
        
    player1.printAttributes ()
    room1.printAttributes ()
    





