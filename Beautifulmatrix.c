#include<stdio.h>
int main()
    {
        int a[5][5],i,j,b[2];
        for(i=0;i<5;i++)
        {
            for(j=0;j<5;j++)
            {
                scanf("%d",&a[i][j]);
                if(a[i][j]==1)
                {
                    b[0]=i;
                    b[1]=j;
                }
            }
        }
        j=0;
        for(i=0;i<2;i++)
        {
            if(b[i]>2)
            {
                 while(b[i]>2)
                    {
                        b[i]-=1;
                        j+=1;
                    }
            }
            else
            {
                while(b[i]<2)
                    {
                        b[i]+=1;
                        j+=1;
                    }
            }
        }
         printf("%d",j);
        return 0;
    }
