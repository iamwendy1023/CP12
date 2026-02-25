#For loop
import sys
sys.stdin = open("in.txt", "r")
sys.stdout = open("out.txt", "w")

n = int(input())
even_count = 0
odd_count = 0
for i in range(n):
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even number:",even_count)
print("Odd number:",odd_count)


