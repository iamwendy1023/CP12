#Vote count
V = input()
s = input()
b = s.count("A")
c = s.count("B")
if b > c:
    print("A")
elif b < c:
    print("B")
elif b == c:
    print("tie")