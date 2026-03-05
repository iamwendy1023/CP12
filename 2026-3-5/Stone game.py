#a 2-player pick up stones game
#start with 7 stone
#players take turns
#on each turn a player must pick up exactly 1 or 2 stones
#the player who picks up the last stone wins
from turtledemo.round_dance import stop

stones = 7
turn = 1
running = True
while running:
    print("Stones:", stones,"Player",turn)
    choice = int(input("Enter your choice:"))
    if choice == 1:
        stones -=21
    if choice == 2:
        stones -= 2
    if stones <= 0:
        print("Player",turn,"won the game")
        running = False
    turn = 3 - turn
#How to handle changing terms
#turn = 1
#while True:
    #print("player",turn)
    #choice = int(input("Enter your choice:")




