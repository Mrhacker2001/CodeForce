s=input()
a=[]
temp=""
for i in s :
    if i != "+" and i :
        temp=str(temp)+str(i)
    if i == "+":
        a.append(int(temp))
        temp=""
a.append(int(temp))
for num in range(0,len(a)) :
    num1=num+1
    while num1 < len(a) :
        if a[num] > a[num1]:
            temp=a[num]
            a[num]=a[num1]
            a[num1]=temp
        num1=num1+1
for i in range(0,len(a)) :
    print(a[i],end='')
    if i != len(a)-1:
        print("+",end='')
  
