#Sounds fishy
import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt','w')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b < c < d:
    print("Fish Rising")
elif d < c < b < a:
    print("Fish Diving")
elif a == b == c == d:
    print("Fish At Constant Depth")
else:
    print("No Fish")