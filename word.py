n=int(input())
lst = []
for i in range(0,n) :
    lst.append(str(input()))
for i in range(0,n) :
    if len(lst[i]) >10 :
        print(lst[i][0]+str(len(lst[i])-2)+lst[i][len(lst[i])-1])
    else :
        print(lst[i])
