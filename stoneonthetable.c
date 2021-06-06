#include<stdio.h>
int main()
    {
        int count,i=0,temp=0;
        scanf("%d",&count);
        char a[count];
        scanf("%s",&a);
        while(i<count)
        {
            if(a[i]==a[i+1])
                temp+=1;
            i+=1;
        }
        printf("%d",temp);
        return 0;
    }
