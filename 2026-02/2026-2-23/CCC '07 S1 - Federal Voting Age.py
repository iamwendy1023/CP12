#Federal Voting Age

n = int(input())

while n > 0:
    y, m, d = map(int, input().split())
    if (y, m, d) <= (1989, 2, 27):
        print("Yes")
    else:
        print("No")
    n -= 1