N = int(input())
shu = {"Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000}
total = 0
while N > 0:
    pepper = input()
    total = total + shu[pepper]
    N = N - 1
print(total)