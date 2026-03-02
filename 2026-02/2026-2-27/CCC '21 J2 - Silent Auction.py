n = int(input())
winner = ""
highest_bid = 0
for i in range(n):
    name = input()
    bid = int(input())
    if bid > highest_bid:
        highest_bid = bid
        winner_name = name
print(winner_name)
