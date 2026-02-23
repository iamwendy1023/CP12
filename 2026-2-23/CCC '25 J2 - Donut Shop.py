#Donut shop
D = int(input())
E = int(input())

while E > 0:
    op = input()
    Q = int(input())
    if op == '+':
        D += Q
    else:
        D -= Q
    E -= 1

print(D)