n=int(input())
a=[]
for i in range(0,n):
    a.append(input())
temp=0
for i in a :
    if i=="X++" or i=="++X" :
        temp=temp+1
    elif i=="X--" or i=="--X" :
        temp=temp-1
print(temp)
