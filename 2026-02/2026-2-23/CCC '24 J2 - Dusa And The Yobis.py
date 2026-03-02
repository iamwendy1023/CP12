#Dusa and the Yobis

#read dusa
#read yobi
D = int(input())
Y = int(input())
while D > Y: #check if dusa can eat yubi
    D += Y#update dusa size
    Y = int(input())#read the next yubi
print(D)#print dusa size
