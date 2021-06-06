str=input()
a=[]
for i in str :
    if not(i in a):
        a.append(i)
if len(a)%2==0 :
    print("CHAT WITH HER!")
else :
    print("IGNORE HIM!")

