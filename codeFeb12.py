#Sushi problem
number1 = int(input("number of red plate: ")) #read a line, and will convert it to a number
number2 = int(input("number of green plate: "))
number3 = int(input("number of blue plate: "))
total = number1 * 3 + number2 * 4 + number3 * 5
print(total)
#Cupcake problem
number4 = int(input())
number5  = int(input())
total = number4 * 8 + number5 * 3
print(total - 28)
# a variable name can contain letter s and digits and _ only
# a variable name cannot bein with a digit
# final velocity
a = 3
u = int(input())
t = int(input())
v = u + a * t
print(v)
# Lemon bathtub
L = int(input())
K = int(input())
T = L // K
print(T)
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
#Roller Coaster Ride
N = int(input())
C = int(input())
P = int(input())
if N <= C*P:
    print("yes")
else:
    print("no")
#Deliv-2-droid
P = int(input())
C = int(input())
total = P * 50 - C * 10
if P > C :
    print(total + 500)
else:
    print(total)
#Boiling Water
B = int(input())
P = 5 * B - 400
print(P)
if B < 100:
    print(1)
elif B > 100:
    print(-1)
else:
    print(0)