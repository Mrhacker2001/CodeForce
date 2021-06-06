#include<stdio.h>
int main()
    {
        char a[100],i=1;
        scanf("%s",&a);
        if (a[0]>='a' && a[0]<='z')
            printf("%c",a[0]-32);
        else
            printf("%c",a[0]);
        while(i<strlen(a))
            {
                printf("%c",a[i]);
                i=i+1;
            }
            
        return 0;
    }
