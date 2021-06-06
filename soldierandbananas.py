k,n,w=input().split(" ")
k=int(k)
n=int(n)
w=int(w)
temp=0
while w >= 1 :
    temp=temp+w*k
    w=w-1
if temp > n :
    temp=temp-n
    print(temp)
else :
    print("0")
    
