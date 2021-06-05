n=int(input())
lst=[]
for i in range(0,n) :
    for j in range(0,3) :
        a=int(input())
        lst.append(a)
print(lst);
number=0
count=1
increase=0
for i in range(0,n):
    if lst[i]==1 :
        number=number+1
    count=count+1
    if count == 3 :
        if number>=2 :
            increase=1+increase
        count=0
        number=0
    print(count,increase,number)
print (increase)
