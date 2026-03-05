#pick a random target btw 1 and 100
#repeat until the user gets it right:
    #ask the user for input
    #compare the input with target and print the correct message
    # print go higher or lower based on the comparison
#the user found the number!
#count how many choices the user made to get it right
#ask the user for game level:
    #easy: 1-10
    #medium: 1-100
    #hard: 1-1000
import random
print("Choose level: easy (1-10), medium (1-100), hard (1-1000)")
level = input("Enter level (easy/medium/hard): ").lower()
if level == "easy":
    max_num = 10
elif level == "hard":
    max_num = 1000
else:
    max_num = 100

target = random.randint(1,100)
running = True
time = 0
while running == True:
    user = int(input("Enter your guess:"))
    time += 1
    if user > target:
        print("go lower")
    if user < target:
        print("go higher")
    if user == target:
        print("you got it!!!It took you",time, "guesses.")
        running = False

