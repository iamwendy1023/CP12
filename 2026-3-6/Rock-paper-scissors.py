import random
s = random.choice(['rock', 'paper', 'scissors'])
choices = input()
print(s)
while True:
    if choices == 'rock' and s == "paper":
        print("Player lose!")
    if choices == 'rock' and s == "scissors":
        print("Player wins!")
    if choices == 'paper'and s == "scissors":
        print("Player lose!")
    if choices == 'paper'and s == "rock":
        print("Player wins!")
    if choices == 'scissors'and s == "rock":
        print("Player lose!")
    if choices == 'scissors'and s == "paper":
        print("Player wins!")
    if choices == s:
        print("a draw!")
    choices = input()
    print(s)