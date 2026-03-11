#List
#   0   1   2   3
b = [10,30,20,40]
print(b[3])
b[0] += 5
print(b)
#add 25 to the end of the list:
b.append(25)
print(b)
b.sort() #order:smaller to bigger
print(b)
#read a list of 3 numbers:
a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.sort()
print(a)
#removing the last number from a list:
a = [10,20,30,40,50]
print(a)
a.pop()
print(a)