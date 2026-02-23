#English or French
n = int(input())
t_count = 0
s_count = 0
line_number = 0
while line_number < n:
    while n > 0:
        line = input()
        t_count = t_count + line.count('t') + line.count('T')
        s_count = s_count + line.count('s') + line.count('S')
        n = n - 1

    if t_count > s_count:
        print("English")
    else:
        print("French")
