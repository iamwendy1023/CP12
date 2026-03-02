#Dog Treats
S = int(input())
M = int(input())
L = int(input())
score = 1 * S + 2 * M + 3 * L
#> < >= <= ==equal  !=not equal
if score < 10:
    print("sad")
if score >= 10:
    print("happy")