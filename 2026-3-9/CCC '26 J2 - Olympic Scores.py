a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
factor = int(input())
a.sort()
total = a[1] + a[2] + a[3]
T = total * factor
print(T)