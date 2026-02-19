import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt','w')
#a = int(input())
#print(a * 2)
#Winning score
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
A = a * 3 + b * 2 + c * 1
B = d * 3 + e * 2 + f * 1
if A > B:
    print("A")
elif A < B:
    print("B")
elif A == B:
    print("T")