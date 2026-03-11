n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
u = []
for i in range(n):
    if s[i] not in u:
        u.append(s[i])
for i in range(len(u)):
    for j in range(len(u)):
        if u[i] > u[j]:
            u[i], u[j] = u[j], u[i]
b = u[2]
c = 0
for i in range(n):
    if s[i] == b:
        c = c + 1
print(b, c)