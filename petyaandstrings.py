str1=input()
str2=input()
temp=0
temp1=0
for i in range(1,len(str1)+1) :
    if str1[0:i].lower()!=str2[0:i].lower() :
        for j in range(97,123):
            if str1[i-1].lower()==chr(j):
                temp=j
            if str2[i-1].lower()==chr(j):
                temp1=j
        break
if temp==temp1:
    print("0")
elif temp<temp1:
    print("-1")
elif temp>temp1:
    print("1")


