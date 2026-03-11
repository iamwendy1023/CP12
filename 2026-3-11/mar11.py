#Hangman starter code
targetWord = "interesting"
target = list(targetWord)
print(targetWord)
print(target)
user = ["_"] * len(target) #create a list of _ with the same length as target
print(user)
choice = input()
if choice in target: #check if sth. appears in a list
    print("good job")
    for i in range(len(target)):
        if target[i] == choice:
            user[i] = choice
else:
    print("bad job")